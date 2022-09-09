from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    # Handle the page request to sort products
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Handle the page request to return a specific category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Handle the page request to query the database
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 
                               "Please enter a search criteria")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(subtitle__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'(sort)_(direction)'

    # Context to return to the page
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show a single product in detail """

    # Return the requested product or 404
    product = get_object_or_404(Product, pk=product_id)

    # Context to return to the page
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product from the front end """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
