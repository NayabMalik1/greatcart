from django import forms
from .models import Order, OrderProduct

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'phone', 'email',
            'address_line_1', 'address_line_2', 'city',
            'state', 'country', 'order_note'
        ]

