import operator

employees = [
    {"name": "Jane", "salary": 90000, "job_title": "developer"},
    {"name": "Bill", "salary": 50000, "job_title": "writer"},
    {"name": "Kathy", "salary": 120000, "job_title": "executive"},
    {"name": "Anna", "salary": 100000, "job_title": "developer"},
    {"name": "Dennis", "salary": 95000, "job_title": "developer"},
    {"name": "Albert", "salary": 70000, "job_title": "marketing specialist"},
]


def main():
    developers = [e for e in employees if e["job_title"] == "developer"]
    non_developers = [e for e in employees if e["job_title"] != "developer"]

    developer_avg_salary = sum(map(operator.itemgetter("salary"), developers)) / len(
        developers
    )
    non_developer_avg_salary = sum(
        map(operator.itemgetter("salary"), non_developers)
    ) / len(non_developers)
    print(developer_avg_salary)
    print(non_developer_avg_salary)


if __name__ == "__main__":
    main()
