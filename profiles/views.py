from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserWishList
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
def user_wish_list(request):
    """ Display the users wish list """
    if request.user.is_authenticated:
        return render(request, 'profiles/wishlist.html')
    else:
        messages.error(request, 'Sorry you must be \
            signed in to use a Wish List.')
        return redirect('home')


def add_to_wishlist(request, pk):
    """ view to display orders to user """
    # check to see if the user is signed in
    if request.user.is_authenticated:
        # retrieve user and product models
        user = UserProfile.objects.get(user=request.user)
        product = get_object_or_404(Product, pk=pk)
        # check to see if user has added the item to their wish list
        if UserWishList.objects.filter(user=user, product=product).exists():
            wishlist_item = UserWishList.objects.get(
                user=user, product=product)
            wishlist_item.delete()
            messages.info(request, "removed from Wish List")
            return redirect(reverse(
                'all_products'), kwargs={'not_shopping': True})
        else:
            # if item is not in wish list then add the item
            wishlist_item = UserWishList.objects.create(
                user=user, product=product)
            messages.success(request, f"{wishlist_item} added to Wish List")
            return redirect(
                reverse('products'), kwargs={'not_shopping': True})
    else:
        # redirect back to all products if the user isn't logged in
        messages.error(request, 'You must be signed in to use a Wish List.')
        return redirect(reverse('products'), kwargs={'not_shopping': True})
