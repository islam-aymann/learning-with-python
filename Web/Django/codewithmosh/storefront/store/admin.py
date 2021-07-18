from django.contrib import admin

from . import models

admin.site.register(
    (
        models.Customer,
        models.Order,
        models.Address,
        models.Product,
    )
)
