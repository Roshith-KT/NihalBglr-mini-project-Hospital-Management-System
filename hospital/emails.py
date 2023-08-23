from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

def send_password_reset_otp(email, otp):
    subject = "HMS Patient Account Password Reset OTP"
    email_from = settings.EMAIL_HOST_USER
    message=f'OTP for password reset is {otp}'
    send_mail(subject,message,email_from,[email,])