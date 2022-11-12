from django import template


register = template.Library()


# Register filter on templates
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculate subtotal within bag """
    return price * quantity
