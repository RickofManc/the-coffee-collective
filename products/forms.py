from django import forms
from .models import Product, Category, Review
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """
    Uses Django form to create
    a form for product details
    """
    class Meta:
        model = Product
        fields = ['category', 'sku', 'name', 'subtitle', 'description', 'has_sizes', 'size', 'intensity', 'price', 'rating', 'date_added', 'image_url', 'image']

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'


class ReviewForm(forms.ModelForm):
    """
    Uses Django form to enable users
    to add product reviews within
    Post Detail view.
    """
    class Meta:
        model = Review
        fields = ('message',)
