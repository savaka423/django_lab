groupmates = [
    {
        "name": "Климай Полина",
        "group": "БСТ-2253",
        "age": 23,
        "marks": [2,3,4,4]
    },
    {
        "name": "Кондаков Артем",
        "group": "БСТ-2253",
        "age": 23,
        "marks": [2,5,4,5]
    },
    {
        "name": "Коновалов Сергей",
        "group": "БСТ-2253",
        "age": 28,
        "marks": [5,5,4,5]
    },
    {
        "name": "Кузнецов Вадим",
        "group": "БСТ-2253",
        "age": 28,
        "marks": [2,3,2,3]
    }
]

def print_students(groupmates):
    print(
        f"{'Имя студента':<30}"
        f"{'Группа':<10}"
        f"{'Возраст':<10}"
        f"{'Оценки':<20}"
    )

    for student in groupmates:
        print(
            f"{student['name']:<30}"
            f"{student['group']:<10}"
            f"{student['age']:<10}"
            f"{str(student['marks']):<20}"
        )

    print()

print_students(groupmates)

def filter_students_by_avg(groupmates, min_avg):
    passed_students = []   

    for student in groupmates:
    
        avg_mark = sum(student["marks"]) / len(student["marks"])

        if avg_mark > min_avg:
            passed_students.append(student)

    return passed_students

students = filter_students_by_avg(groupmates, 3.3)

print("Студенты со средним баллом выше 3.3:\n")
print_students(students)
