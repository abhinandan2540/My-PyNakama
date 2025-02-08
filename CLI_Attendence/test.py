from argparse import ArgumentParser
import os
import json
# for sending the email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv()

sender_mail = os.getenv("SENDER")
reciever_mail = os.getenv("RECIEVER")
app_password = os.getenv("APP_PASSWORD")


# reading,writing,saving student credentials

data_sheet = "SCS.txt"
if os.path.exists(data_sheet):
    with open(data_sheet, 'r') as file:
        students = json.load(file)
else:
    students = []


def sendStudentEmails(student_name, student_subject, student_total_leave):
    msg = MIMEMultipart()
    msg["From"] = sender_mail
    msg["To"] = reciever_mail
    msg["Subject"] = "warning!!! leaving exceeded!!!"
    msg.attach(MIMEText(
        f"{student_name} for subject {student_subject} exceeded limit of 3 leave, his total leave :  {student_total_leave}"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_mail, app_password)
        server.sendmail(sender_mail, reciever_mail, msg.as_string())
        server.quit()
        print("exceeded mail send sucessfully")
    except Exception as e:
        print(f"Error : {e}")


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

    if student_total_leave > 3:
        sendStudentEmails(student_name, student_subject, student_total_leave)


def updateStudentCredentials():
    studentName = input("Enter student name :")
    for student in students:
        if student['student_name'] == studentName:
            student['student_subject'] = input("student_subject :")
            student['student_total_leave'] = int(
                input("student_total_leave : "))
            save_data()
            print(f"{studentName} credentials updated...")

            if student['student_total_leave'] > 3:
                sendStudentEmails(
                    studentName, student['student_subject'], student['student_total_leave'])

        else:
            print(f"{studentName} not found")


def viewStudentCredentials():
    if students:
        for student in students:
            print(
                f"student_name : {student['student_name']}, student_subjects:{student['student_subject']}, student_total_leave: {student['student_total_leave']}")
            if (student['student_total_leave'] > 3):
                sendStudentEmails(
                    student['student_name'], student['student_subject'], student['student_total_leave'])
    else:
        print("no record found")


def main():
    parser = ArgumentParser()
    parser.add_argument("--add", action='store_true',
                        help="add_student_credentials")
    parser.add_argument("--view", action="store_true",
                        help="view_student_credentials")
    parser.add_argument("--update", action='store_true',
                        help="update_student_credentials")
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
    elif args.update:
        updateStudentCredentials()
    else:
        print(parser.print_help())


if __name__ == "__main__":
    main()
