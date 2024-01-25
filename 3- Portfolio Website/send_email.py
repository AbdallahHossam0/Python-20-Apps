import smtplib
import ssl


def sendMail(message, userMail):
    host = "smtp.gmail.com"
    port = 465

    MAIL = "abdallah.hossam.st@gmail.com"
    PASSWORD = "qmst jcdf zjxp zend"

    context = ssl.create_default_context()

    message1 = f"""Subject: Thanks for your message
Hello. Your Message was received successfully. We hope to get in touch with you soon.
Best regards.
Abdallah Hossam-Eldin Hosni"""
    message2 = f"""Subject: Message from your website. \n
Message:{message}\nSender: {userMail}"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(MAIL, PASSWORD)
        server.sendmail(MAIL, userMail, message1)
        server.sendmail(MAIL, MAIL, message2)
