from email.message import EmailMessage
import ssl
import smtplib

#sender's email address
email_sender = '11.deepakjha.dj@gmail.com' 

#app password that we had previously generated
email_password = '' 

#receiver's email address
email_receiver = ''

#subject of the email
subject = 'Hey, I am sending this email using Python!'

#content of the email
body = """Hello there!

I hope this email finds you well. I wanted to reach out and let you know that I am using a program I made in Python to send this message. I find it exciting to explore the possibilities of programming and how it can make our lives easier.

If you're interested, please do not hesitate to check out my GitHub profile, where I share some of the projects I've been working on. I'm always open to feedback and collaboration, so don't hesitate to reach out if you have any questions or suggestions.

Thank you for taking the time to read this message. Have a great day!

Best regards,
<Name>
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
