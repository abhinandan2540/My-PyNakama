from argparse import ArgumentParser
import os
import json

# reading,writing,saving student credentials

data_sheet = "SCS.txt"
if os.path.exists(data_sheet):
    with open(data_sheet, 'r') as file:
        students = json.load(file)
else:
    students = []


def save_data():
    with open(data_sheet, 'w') as file:
        json.dump(students, file, indent=4)


def addStudentCredentials(student_name, student_subject, student_total_leave):
    student_credentials = {
        "student_name": student_name,
        "student_subject": student_subject,
        "student_total_leave": student_total_leave
    }
    students.append(student_credentials)
    save_data()
    print("student credentials added...")


def viewStudentCredentials():
    if students:
        for student in students:
            print(
                f"student_name : {student['student_name']}, student_subjects:{student['student_subject']}, student_total_leave: {student['student_total_leave']}")
    else:
        print("no record found")


def main():
    parser = ArgumentParser()
    parser.add_argument("--add", action='store_true',
                        help="add_student_credentials")
    parser.add_argument("--view", action="store_true",
                        help="view_student_credentials")
    parser.add_argument("--student_name", type=str, help="add_student_name")
    parser.add_argument("--student_subject", type=str,
                        help="add_student_subject")
    parser.add_argument("--student_total_leave", type=int,
                        help="add_student_total_leave")

    args = parser.parse_args()
    if (args.add and args.student_name and args.student_subject and args.student_total_leave):
        addStudentCredentials(
            args.student_name, args.student_subject, args.student_total_leave)
    elif args.view:
        viewStudentCredentials()
    else:
        print(parser.print_help())


if __name__ == "__main__":
    main()
