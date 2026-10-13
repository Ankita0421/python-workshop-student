import json
import os


def load_students(filename, Student):
    """Load students from a JSON file."""
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        students = []

        for item in data:
            student = Student(
                item["name"],
                item["age"],
                item["python"],
                item["mathematics"],
                item["communication"]
            )
            students.append(student)

        return students

    except (json.JSONDecodeError, KeyError, TypeError, OSError) as error:
        print("Error loading students:", error)
        return []


def save_students(students, filename):
    """Save students to a JSON file."""
    try:
        data = []

        for student in students:
            data.append({
                "name": student.name,
                "age": student.age,
                "python": student.python,
                "mathematics": student.mathematics,
                "communication": student.communication
            })

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    except (AttributeError, TypeError, OSError) as error:
        print("Error saving students:", error)
