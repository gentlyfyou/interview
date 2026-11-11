import smtplib
import imaplib
import email
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailClient:
    def __init__(self, login: str, password: str, smtp_server: str = "smtp.gmail.com", imap_server: str = "imap.gmail.com"):
        self.login = login
        self.password = password
        self.smtp_server = smtp_server
        self.imap_server = imap_server

    def send_email(self, recipients: list, subject: str, message: str) -> None:
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, 587) as server:
                server.starttls()
                server.login(self.login, self.password)
                server.sendmail(self.login, recipients, msg.as_string())
            print("Письмо успешно отправлено!")
        except smtplib.SMTPException as e:
            print(f"Ошибка SMTP при отправке письма: {e}")

    def receive_email(self, mailbox: str = "inbox", header_subject: str = None):
        mail = None
        try:
            mail = imaplib.IMAP4_SSL(self.imap_server)
            mail.login(self.login, self.password)
            mail.select(mailbox)

            criterion = f'(HEADER Subject "{header_subject}")' if header_subject else 'ALL'
            result, data = mail.uid('search', None, criterion)

            if not data[0]:
                print("Писем с такими параметрами не найдено.")
                return None

            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            
            return email_message
            
        except imaplib.IMAP4.error as e:
            print(f"Ошибка IMAP при получении письма: {e}")
            return None
        finally:
            if mail is not None:
                try:
                    mail.logout()
                except Exception:
                    pass


if __name__ == '__main__':
    user_login = input("Введите ваш email (логин): ")
    user_password = getpass.getpass("Введите пароль от почты (ввод не будет отображаться): ")
    
    client = EmailClient(login=user_login, password=user_password)