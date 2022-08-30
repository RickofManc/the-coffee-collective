"""
Django imports to support Views
"""
from django.shortcuts import render, redirect


def view_bag(request):
    """ A view to return the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add quantity and size to the bag """

    quantity = int(request.POST.get('quantity'))
    size = int(request.POST.get('size'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        bag[item_id] += size
    else:
        bag[item_id] = quantity
        bag[item_id] = size

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

