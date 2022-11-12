from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.views.generic import DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


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
                messages.error(request,"Please enter a search criteria")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # Context to return to the page
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show a single product in detail
    and enable signed in users to add reviews
    """

    # Return the requested product or 404
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.order_by('-created_on')

    if request.user.is_authenticated:
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.username = request.user
            review = review_form.save(commit=False)
            review.product = product
            review.save()
            messages.success(request, 'Thank you for taking \
                the time to provide a review')

    # Context to return to the page
    context = {
        'product': product,
        'reviews': reviews,
        'reviewed': False,
        'review_form': ReviewForm(),
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product from the front end """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                            Please ensure the form is completed correctly')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product from the front end """
    # if not superuser redirect home
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the owners can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                            Please ensure the form is completed correctly')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


class DeleteProductView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Displays Delete Product page.
    gets : requested template by name
    returns : rendered view of the html template
    Returns user to homepage on form submission.
    """
    def get(self, request, product_id):
        """ get product request """
        # if not superuser redirect home
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only the owners can do that')
            return redirect(reverse('home'))
        else:
            # return product to page
            product = get_object_or_404(Product, pk=product_id)
            return render(request, 'products/delete_product_page.html',
                          {'product': product})

        # def post(self, request, product_id, *args, **kwargs):
        #     """ post delete view """
        #     product = get_object_or_404(Product, pk=product_id)
        #     product.delete()
        #     messages.success(
        #         request, f'Success, {product.name} has been deleted.')
        #     return redirect(
        #         reverse(reverse('home')))


@login_required
def delete_product(request, product_id):
    """ Delete a product from the front end """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the owners can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted')
    return redirect(reverse('products'))
