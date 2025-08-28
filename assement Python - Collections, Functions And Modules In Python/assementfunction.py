
from datetime import datetime

attendance_data = {}


def mark_attendance():
    roll_no = input("Enter Roll Number: ").strip()
    name = input("Enter Student Name: ").strip()
    course = input("Enter Course: ").strip()
    date = input("Enter Date (dd-mm-yyyy) [Leave blank for today]: ").strip()
    
    if date == "":
        date = datetime.today().strftime("%d-%m-%Y")
    
    status = input("Mark Attendance (P/A): ").strip().upper()
    if status not in ["P", "A"]:
        print(" Invalid input! Use 'P' for Present or 'A' for Absent.")
        return
    
    # Initialize student if new
    if roll_no not in attendance_data:
        attendance_data[roll_no] = {"name": name, "course": course, "records": {}}
    
    # Prevent duplicate entry
    if date in attendance_data[roll_no]["records"]:
        print(f"⚠ Attendance already marked for {name} on {date}.")
        return
    
    # Save attendance
    attendance_data[roll_no]["records"][date] = status
    print(f" Attendance marked for {name} ({roll_no}) on {date} as {status}.")


def student_report():
    roll_no = input("Enter Roll Number: ").strip()
    
    if roll_no not in attendance_data:
        print(" Student not found!")
        return
    
    student = attendance_data[roll_no]
    total_classes = len(student["records"])
    present_count = sum(1 for s in student["records"].values() if s == "P")
    absent_count = total_classes - present_count
    attendance_percent = (present_count / total_classes * 100) if total_classes > 0 else 0
    
    print("\n--- Attendance Report ---")
    print(f"Name     : {student['name']}")
    print(f"Roll No  : {roll_no}")
    print(f"Course   : {student['course']}")
    print(f"Total Classes : {total_classes}")
    print(f"Present       : {present_count}")
    print(f"Absent        : {absent_count}")
    print(f"Attendance %  : {attendance_percent:.2f}%")
    print("Status        :", " Defaulter (<75%)" if attendance_percent < 75 else " Good Standing")


def class_report():
    print("\n--- Class Attendance Report ---")
    if not attendance_data:
        print("No records found yet!")
        return
    
    print(f"{'Roll No':<10}{'Name':<15}{'Course':<10}{'Total':<8}{'Present':<8}{'Absent':<8}{'%':<8}{'Status'}")
    print("-" * 70)
    
    for roll_no, student in attendance_data.items():
        total = len(student["records"])
        present = sum(1 for s in student["records"].values() if s == "P")
        absent = total - present
        percent = (present / total * 100) if total > 0 else 0
        status = " Defaulter" if percent < 75 else "ok!"
        
        print(f"{roll_no:<10}{student['name']:<15}{student['course']:<10}{total:<8}{present:<8}{absent:<8}{percent:<8.2f}{status}")


def main():
    while True:
        print("\n===== EduTrack - Attendance System =====")
        print("1. Mark Attendance")
        print("2. Student Attendance Report")
        print("3. Class Attendance Report")
        print("4. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            mark_attendance()
        elif choice == "2":
            student_report()
        elif choice == "3":
            class_report()
        elif choice == "4":
            print(" Exiting EduTrack. Goodbye!")
            break
        else:
            print(" Invalid choice! Please try again.")


if __name__ == "__main__":
    main()