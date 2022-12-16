from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from products.models import Product


@login_required
def profile(request):
    """ Display the users profile with orders """
    profile = get_object_or_404(UserProfile, user=request.user)
    # Function to save changes to User Profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated')
        else:
            messages.error(request, 'Update failed. \
                           Please ensure the form is completed correctly')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    return render(request, template, context)


def single_order(request, order_number):
    """ Displays a single historic order to user """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation was sent on the order date.'
        ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)


@login_required
def wishlist(request):
    """ Display the users wish list page """
    if request.user.is_authenticated:
        products = Product.objects.filter(users_wishlist=request.user)
        return render(request, 'profiles/wishlist.html',
                      {'wishlist': products})
    else:
        messages.error(request, 'Sorry you must be \
            signed in to use a Wish List.')
        return redirect('home')


@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        messages.success(request, product.name + ' has been \
                         removed from your Wish List')
    else:
        product.users_wishlist.add(request.user)
        messages.success(request, 'Added ' + product.name + ' to \
                         your Wish List')
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
