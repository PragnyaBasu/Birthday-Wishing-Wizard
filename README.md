# Birthday Wisher Automation 🎉

This Python script automates sending birthday wishes via email to individuals listed in an Excel file. The script checks birthdays daily at midnight and sends personalized emails with the specified message.

---

## ✨ Features
- Reads birthdays and email details from an Excel file (`data.xlsx`).
- Automatically sends birthday emails using the **Gmail SMTP server**.
- Keeps track of birthdays sent each year to avoid duplicate wishes.
- Easy to set up and customize.

---

## 📋 Requirements

### Python Libraries
Ensure the following Python libraries are installed:

- `pandas`
- `datetime`
- `smtplib`
- `openpyxl` (for working with Excel files)

Install them via pip:

```bash
pip install pandas
pip install openpyxl
```
---

## 🚀 Setup Instructions

### Clone this repository:
```bash
git clone https://github.com/your_username/birthday-wisher-automation.git
cd birthday-wisher-automation
```

### Update Gmail credentials:
To enable the script to send emails, you need to configure your Gmail account credentials in the script:

* Locate the following variables in the script:
```
GMAIL_ID = 'your_email@gmail.com'
GMAIL_PSWD = 'your_password'
```
* Replace the placeholder values with your Gmail account credentials:
  
GMAIL_ID: Your Gmail address (e.g., your_email@gmail.com).

GMAIL_PSWD: Your Gmail password.

**Important:** For enhanced security, generate an App Password and use it in place of your actual Gmail password. App Passwords are unique, application-specific credentials that allow access without exposing your primary password.

* Save the changes to the script to apply the updates.

### Prepare the data.xlsx file:

Create an Excel file named data.xlsx in the same directory as the script.
Ensure it has the following columns:
* Name: Name of the individual.
* Email: Email address to send the wishes.
* Birthday: Date of birth in DD-MM-YYYY format.
* Dialogue: Custom message to include in the email.
* Year: Leave this column empty initially. It will store the years when wishes were sent.

| Name       | Email                | Birthday    | Dialogue                  | Year |
|------------|----------------------|-------------|---------------------------|------|
| John Doe   | john.doe@gmail.com   | 01-01-1990  | Happy Birthday, John!     |      |
| Jane Smith | jane.smith@gmail.com | 18-11-1985  | Wishing you a great day!  |      |

### Schedule the script to run daily:
Use Task Scheduler (Windows) or a Cron job (Linux) to run the script automatically at midnight.

---

## 🏃‍♀️ How to Run
Ensure the working directory is correct:
``` bash
os.chdir(r"path_to_directory_containing_script")
```
## Execute the script manually for testing:
```bash
python birthday_wisher.py
```
---

## 🛠️ Troubleshooting
#### SMTP Authentication Error:
* Enable "Allow less secure apps" in Gmail settings or use an App Password.
#### File Not Found Error:
* Ensure data.xlsx is in the same directory as the script.
#### Cron/Task Scheduler Issues:
* Check permissions or verify the Python environment used by the scheduler.
---

## Author
PRAGNYA BASU
---
