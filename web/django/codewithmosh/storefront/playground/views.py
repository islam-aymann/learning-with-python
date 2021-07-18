from django.db import transaction, connection
from django.db.models import Value, F, Count, Min, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.shortcuts import render

from store.models import Order, Product, Customer, Collection, OrderItem
from tags.models import TaggedItem


def say_hello(request):
    order_queryset = (
        Order.objects.order_by("placed_at")
            .select_related("customer")
            .prefetch_related("orderitem_set__product")[:5]
    )
    product_query = Product.objects.filter(collection_id=6).aggregate(
        count=Count("id"), min_price=Min("unit_price")
    )
    # customer_queryset = Customer.objects.annotate(
    #     full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT")
    # )

    customer_queryset = Customer.objects.annotate(
        full_name=Concat("first_name", Value(" "), "last_name")
    )

    orders_count_queryset = Customer.objects.annotate(orders_count=Count("order"))[:5]

    expression = ExpressionWrapper(F("unit_price") * 0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(discounted_price=expression)[:2]

    # Defining a custom model manager to get tags for a specific model
    queryset = TaggedItem.objects.get_tags_for(Product, 1)

    # Create
    # collection = Collection.objects.create(
    #     title="Video Games", featured_product=Product.objects.first()
    # )
    collection = Collection()
    collection.title = "Video Games"
    collection.featured_product = Product.objects.first()
    # collection.save()
    print(collection)

    # update
    # collection = Collection(pk=11)  # causes data lose
    collection = Collection.objects.get(pk=11)
    collection.title = "Games"
    collection.featured_product = None
    # collection.save()
    # Collection.objects.filter(pk=11).update(title="Games")  # most efficient way

    # delete
    # Collection.objects.filter(id__gt=5).delete()

    # atomic operations: all operations have to success actually store data in DB
    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()

    # raw SQL
    raw_queryset = Product.objects.raw("SELECT * FROM store_product")
    print(list(raw_queryset))

    # directly access the cursor
    # with connection.cursor() as cursor:
    #     cursor.execute("get_customers")  # execute custom procedures

    return render(
        request,
        "hello.html",
        {
            "name": "Islam",
            "orders": list(order_queryset),
            "product_query": product_query,
            "customers": list(customer_queryset),
            "queryset": list(queryset),
        },
    )
