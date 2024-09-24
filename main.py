def output(students):
    for name in students:
        print(f"{name}: {students[name]}")

def add_student(students):
    name = input("Введіть прізвище нового студента: ")
    if name in students:
        print(f"Студент з прізвищем {name} вже є в списку")
        return
    marks = input("Введіть оцінки: ").split()
    marks = list(map(int, marks))
    students[name] = marks
    print(f"Учень {name} доданий.")

def remove_student(students):
    name = input("Введіть прізвище студента, якого потрібно видалити: ")
    if name in students:
        del students[name]
        print(f"Учень {name} видалений")
    else:
        print(f"Учня {name} не знайдено")

def add_marks(students):
    name = input("Введіть прізвище учня, якому потрібно додати оцінки: ")
    if name in students:
        marks = input("Введіть нові оцінки, розділені пробілом: ").split()
        marks = list(map(int, marks))
        students[name].extend(marks)
        print(f"Оцінки додані для учня {name}.")
    else:
        print(f"Учня {name} не знайдено")

def sorted_students(students):
    sorted_students = sorted(students.keys())
    print("Список учнів у відсортованому порядку:")
    for student in sorted_students:
        print(student)

def max_sum(students):
    max_student = max(students, key=lambda name: sum(students[name]))
    print(f"Найбільшу суму оцінок має: {max_student} ({sum(students[max_student])})")

def min_sum(students):
    min_student = min(students, key=lambda name: sum(students[name]))
    print(f"Найменшу суму оцінок має: {min_student} ({sum(students[min_student])})")

students_dictionary = {
    "Семененко": [10, 11, 12, 9, 8, 10, 11, 12, 11, 10],
    "Марченко": [8, 9, 7, 12, 10, 9, 6, 8, 10, 9],
    "Тимошенко": [12, 11, 10, 11, 12, 11, 10, 12, 11, 12],
    "Кононенко": [6, 7, 8, 9, 5, 6, 7, 6, 5, 6],
    "Шевчук": [10, 9, 12, 10, 8, 11, 10, 9, 11, 10],
    "Кравченко": [8, 7, 9, 10, 7, 8, 10, 7, 9, 8],
    "Гаврилюк": [9, 10, 10, 12, 9, 10, 9, 11, 12, 10],
    "Павленко": [11, 12, 10, 9, 8, 10, 11, 10, 12, 9],
    "Кузьменко": [7, 8, 9, 8, 7, 9, 8, 6, 8, 7],
    "Мельник": [10, 11, 12, 10, 9, 12, 11, 10, 11, 12]
}

operations = {
    "вивести студентів": output,
    "додати студента": add_student,
    "видалити студента": remove_student,
    "додати оцінки": add_marks,
    "вивести ключі": sorted_students,
    "найбільша сума оцінок": max_sum,
    "найменша сума оцінок": min_sum,
    "вихід": lambda:print("Вихід з програми")
}

print(f"Введіть бажану операцію (вивести студентів / додати студента / видалити студента /"
          f"додати оцінки / вивести ключі / найбільша сума оцінок / найменша сума оцінок / вихід): ")

while True:
    operation = input("Введіть операцію: ").lower()
    if operation in operations:
        if operation == "вихід":
            operations[operation]()
            break
        operations[operation](students_dictionary)
    else:
        print("Невідома операція")