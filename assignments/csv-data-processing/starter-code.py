import csv


def read_csv_rows(file_path):
    """Read a CSV file and return a list of dictionaries."""
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def filter_by_department(rows, department):
    """Return only the rows whose department matches the given value."""
    return [row for row in rows if row["department"].lower() == department.lower()]


def average_score(rows):
    """Return the average score for the rows provided."""
    if not rows:
        return 0

    scores = [int(row["score"]) for row in rows if row.get("score")]
    if not scores:
        return 0

    return sum(scores) / len(scores)


if __name__ == "__main__":
    data = read_csv_rows("students.csv")
    print("Total records:", len(data))
    print("Average score:", average_score(data))
    for student in filter_by_department(data, "Science"):
        print(student["name"], student["score"])
