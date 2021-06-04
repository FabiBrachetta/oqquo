from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IyZtHJdrYB0vG0iZZxUAuzfX0qoWli4t0cH7F5uNQ0e5ELUjAXyI34YNQ1JD8S4gpbS6n0eV33H0jZWBKoIJ6UI00u5z4NR4K',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)