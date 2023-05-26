from django.core.mail import send_mail
import uuid
from django.conf import settings

def send_forget_password_mail(email,token):
    # print(email)
    # print(token)
    subject = 'Your Forget password link'
    message = f'Hi, click on the link to reset your password link will work 24 hours http://127.0.0.1:8000/changepassword/{token}/'
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_form,recipient_list)
    return True