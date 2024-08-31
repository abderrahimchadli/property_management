from celery import shared_task
from .models import RentalPayment
from django.core.mail import send_mail
from django.conf import settings
import datetime

@shared_task
def send_due_payment_notifications():
    # First, we find all the overdue and unpaid rent.
    due_payments = RentalPayment.objects.filter(is_paid=False, payment_date__lt=datetime.date.today())
    for payment in due_payments:
        tenant_email = payment.tenant.contact_details
        # Time to give a friendly Reminder to those who forgot to pay
        send_email(tenant_email, payment.tenant.name, payment.amount)

def send_email(to_email, tenant_name, amount):
    subject = 'Payment Due Reminder'
    message = f'Dear {tenant_name}, your payment of ${amount} is overdue. Please pay as soon as possible.'
    from_email = settings.DEFAULT_FROM_EMAIL
    try:
        send_mail(subject, message, from_email, [to_email])
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
