import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load email list from CSV
email_data = pd.read_csv("email_list.csv")
emails = email_data.iloc[:, 0].tolist()  # assumes emails are in first column

# Your email credentials
YOUR_EMAIL = "youremail@gmail.com"
YOUR_PASSWORD = "your-app-password"  # use Gmail App Password, not your login password

# Email subject and message
subject = "Job Application"

body = """
Dear Hiring Manager,

I am writing to apply for any suitable position at your organization. I hold a BA in English and Literature, a PG Diploma in Digital Marketing, and have working knowledge of marketer. My skills include digital marketing, SEO, Tally, accounting, lead generation, HTML, and CSS. I am also learning JavaScript, React JS, and Photoshop. I have 4 months of experience in digital marketing at Donoben. I look forward to the opportunity to contribute to your team.

Thank you,
Sanan
8078558322
https://drive.google.com/file/d/1RE2Wz5pxBgJqRXe3rZ7MimdiCqJhKjeJ/view?usp=drivesdk
"""

# Connect to Gmail SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(amaljinu599@gmail.com, Qwertyuiop8078558322)

# Send email to all recipients
for email in emails:
    msg = MIMEMultipart()
    msg['From'] =amaljinu599@gmail.com
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server.sendmail(amaljinu599@gmail.com, email, msg.as_string())
        print(f"✅ Sent successfully to {email}")
    except Exception as e:
        print(f"❌ Failed to send to {email}: {e}")

server.quit()
print("\nAll emails processed.")