import json
import os
from datetime import datetime

DATA_FILE = "data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {"subjects": {}}
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_subject(data):
    subject = input("Enter subject name: ").strip()
    if subject in data["subjects"]:
        print("Subject already exists.")
    else:
        data["subjects"][subject] = {
            "study_hours": [],
            "exam_date": None
        }
        print("Subject added successfully.")


def log_study_hours(data):
    subject = input("Enter subject name: ").strip()
    if subject not in data["subjects"]:
        print("Subject not found.")
        return

    try:
        hours = float(input("Enter study hours: "))
        date = datetime.now().strftime("%Y-%m-%d")
        data["subjects"][subject]["study_hours"].append({
            "date": date,
            "hours": hours
        })
        print("Study hours logged.")
    except ValueError:
        print("Invalid input.")


def set_exam_date(data):
    subject = input("Enter subject name: ").strip()
    if subject not in data["subjects"]:
        print("Subject not found.")
        return

    exam_date = input("Enter exam date (YYYY-MM-DD): ")
    data["subjects"][subject]["exam_date"] = exam_date
    print("Exam date set.")


def view_progress(data):
    if not data["subjects"]:
        print("No subjects added yet.")
        return

    for subject, details in data["subjects"].items():
        total_hours = sum(entry["hours"] for entry in details["study_hours"])
        exam = details["exam_date"] or "Not set"
        print(f"\nSubject: {subject}")
        print(f"Total Study Hours: {total_hours}")
        print(f"Exam Date: {exam}")


def main():
    data = load_data()

    while True:
        print("\n--- Student Study Tracker ---")
        print("1. Add Subject")
        print("2. Log Study Hours")
        print("3. Set Exam Date")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_subject(data)
        elif choice == "2":
            log_study_hours(data)
        elif choice == "3":
            set_exam_date(data)
        elif choice == "4":
            view_progress(data)
        elif choice == "5":
            save_data(data)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

        save_data(data)


if __name__ == "__main__":
    main()
