import stripe

from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import OrderLineItem
from products.models import Product
from bag.contexts import bag_contents


def checkout(request):
    """ Function to display the checkout template """
    # call Stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # If session data received process as below
    if request.method == 'POST':
        # request bag session
        bag = request.session.get('bag', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],          
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Products.objects.get(id=item_id)
                    # if the item has no sizes
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    # if the item has sizes
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                # Error message if product does not exist (rare)
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in out database."
                        "Please contact us for further assistance."
                    ))
                    order.delete()
                    return redirect(reverse('view_bag'))
            # Option for user to save their details
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'Sorry, there was an error with your form. \
                Please recheck you information.')
    # Else if session data not received process as below
    else:
        # request bag session
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        # Execute function
        order_form = OrderForm()
    
    # Alert msg if public key not enabled
    if not stripe_public_key:
        messages.warning(request, 'Stripe Public Key is missing. \
            Did you forget to export it in your environment or set in variables?')
    
    # Items to render on template
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)