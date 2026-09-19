import json
import os

FILE_NAME = "students.json"


def load_students():
    """Load students from file. Return empty list if file doesn't exist."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("⚠️  Warning: Could not read data file. Starting fresh.")
        return []


def save_students(students):
    """Save students list to file."""
    try:
        with open(FILE_NAME, "w") as f:
            json.dump(students, f, indent=4)
    except IOError as e:
        print(f"❌ Error saving data: {e}")


def add_student(students):
    """Prompt user for details and add a new student."""
    print("\n--- Add Student ---")
    student_id = input("Enter Student ID: ").strip()
    if not student_id:
        print("❌ Student ID cannot be empty.")
        return

    # Check for duplicate ID
    if any(s["id"] == student_id for s in students):
        print(f"❌ A student with ID '{student_id}' already exists.")
        return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    grade = input("Enter Grade: ").strip()

    if not name:
        print("❌ Name cannot be empty.")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade,
    }
    students.append(student)
    save_students(students)
    print(f"✅ Student '{name}' added successfully.")


def view_students(students):
    """Display all students in a table."""
    print("\n--- All Students ---")
    if not students:
        print("No students found.")
        input("\nPress Enter to return to menu...")
        return

    print(f"{'ID':<10}{'Name':<20}{'Age':<6}{'Grade':<8}")
    print("-" * 44)
    for s in students:
        print(f"{s['id']:<10}{s['name']:<20}{s['age']:<6}{s['grade']:<8}")
    print(f"\nTotal: {len(students)} student(s)")

    input("\nPress Enter to return to menu...")


def delete_student(students):
    """Delete a student by ID."""
    print("\n--- Delete Student ---")
    if not students:
        print("No students to delete.")
        return

    student_id = input("Enter Student ID to delete: ").strip()
    for i, s in enumerate(students):
        if s["id"] == student_id:
            confirm = input(f"Delete '{s['name']}' (ID: {student_id})? (y/n): ").strip().lower()
            if confirm == "y":
                students.pop(i)
                save_students(students)
                print("✅ Student deleted.")
            else:
                print("Cancelled.")
            return
    print(f"❌ No student found with ID '{student_id}'.")


def main():
    students = load_students()

    menu = """
===== Student Record System =====
1. Add Student
2. View Students
3. Delete Student
4. Exit
=================================
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()