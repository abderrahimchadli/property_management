from rest_framework import viewsets
from .models import Property, Tenant, RentalPayment
from .serializers import PropertySerializer, TenantSerializer, RentalPaymentSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.core.mail import send_mail
from django.conf import settings
import datetime
from rest_framework.pagination import PageNumberPagination



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by('name')
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['property_type', 'rental_cost']
    ordering_fields = ['name', 'rental_cost']
    pagination_class = StandardResultsSetPagination


class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated]

class RentalPaymentViewSet(viewsets.ModelViewSet):
    queryset = RentalPayment.objects.all()
    serializer_class = RentalPaymentSerializer
    permission_classes = [IsAuthenticated]

def send_due_payment_notifications():
    due_payments = RentalPayment.objects.filter(is_paid=False, payment_date__lt=datetime.date.today())
    for payment in due_payments:
        tenant_email = payment.tenant.contact_details
        send_email(tenant_email, payment.tenant.name, payment.amount)

#to remove
def send_email(to_email, tenant_name, amount):
    subject = 'Payment Due Reminder'
    message = f'Dear {tenant_name}, your payment of ${amount} is overdue. Please pay as soon as possible.'
    from_email = settings.DEFAULT_FROM_EMAIL
    try:
        send_mail(subject, message, from_email, [to_email])
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
