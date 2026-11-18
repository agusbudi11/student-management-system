
students = []

def add_student():
    name = input("Enter student name: ")
    nim = input("Enter student NIM: ")

    student = {
        "name": name,
        "nim": nim
    }

    students.append(student)
    print("Student added successfully!")

def show_students():
    print("\n=== STUDENT LIST ===")

    if not students:
        print("No student data available.")
        return

    for student in students:
        print(f"Name: {student['name']}")
        print(f"NIM: {student['nim']}")
        print("-------------------")

def search_student():
    nim = input("Enter NIM to search: ")

    for student in students:
        if student["nim"] == nim:
            print("Student found!")
            print(student)
            return

    print("Student not found.")

def delete_student():
    nim = input("Enter NIM to delete: ")

    for student in students:
        if student["nim"] == nim:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")

def main():
    while True:
        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose menu: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you for using this program!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
