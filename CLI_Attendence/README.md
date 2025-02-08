

# **Student Leave Warning System (CLI) 🚀**  

## **📌 Project Overview**  
This is a simple **Command Line Interface (CLI) Python project** that tracks student leaves. The user enters their **name, subject, and total leaves taken**. If the leave count exceeds **3**, an **automatic warning email** is sent to the student’s registered email using **SMTP**.  

## **🔧 Features**  
✅ CLI-based user input system.  
✅ Stores student name, subject, and leave count.  
✅ Sends an **automatic warning email** if leaves exceed 3.  
✅ Uses **SMTP** for email notifications.  

## **⚙️ Installation & Setup**  
### ** Install Dependencies**  
Ensure you have **Python 3.x** installed. Then, install required libraries:  
```bash
pip install smtplib
```
### ** Run the Program**  
```bash
python main.py
```

## **📩 SMTP Email Configuration**  
To send emails, update the SMTP settings in the script:  
```python
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"
```
⚠️ **Use App Passwords instead of your actual password** for security.  

## **📜 Example Usage**  
```
Enter Student Name: John Doe  
Enter Subject: Mathematics  
Enter Total Leaves Taken: 4  
⚠️ Warning Email Sent to John Doe's Email!  
```

## **📬 Email Example**  
**Subject:** Leave Warning Notification  
**Body:**  
>Jhon Doe for subject mathematics exceeded 3 leave, total leave : 4

## **💡 Future Improvements**  
🔹 Store leave data in a database.  
🔹 Add a graphical interface (GUI).  
🔹 Support multiple email providers.  

## Thank You
[My-PyNakama](https://github.com/abhinandan2540)

