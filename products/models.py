from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=155)
    friendly_name = models.CharField(max_length=155, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    User = get_user_model()
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=55, unique=True)
    name = models.CharField(max_length=155)
    subtitle = models.CharField(max_length=205)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    size = models.CharField(max_length=6, null=True, blank=True)
    intensity = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField(null=True, blank=True)
    date_added = models.DateField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    users_wishlist = models.ManyToManyField(
        User, related_name='user_wishlist', blank=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Models the fields for adding product reviews.
    """
    User = get_user_model()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews'
    )
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='user_reviews')
    message = models.TextField(help_text='Add your review here')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Review {self.message} by {self.username}'
