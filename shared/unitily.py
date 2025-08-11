
import re
import threading
from django.template.loader import render_to_string

from django.core.mail import EmailMessage
from rest_framework.exceptions import ValidationError

email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

def check_email(user_email):
    if re.fullmatch(email_regex,user_email):
        return 'email'
    else:
        raise ValidationError(
            {
                "success":False,
                "message":"Kiritilgan Email yaroqli emas!"
            }

        )


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Email:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            to=[data['to_email']]
        )
        if data.get('content_type') == "html":
            email.content_subtype = 'html'
        EmailThread(email).start()


def send_email(email, code):
    from django.template.loader import render_to_string
    html_content = render_to_string(
        'email/authentication/activate_account.html',
        {"code": code}
    )
    Email.send_email(
        {
            "subject": "Royhatdan otish",
            "to_email": email,
            "body": html_content,
            "content_type": "html"
        }
    )
