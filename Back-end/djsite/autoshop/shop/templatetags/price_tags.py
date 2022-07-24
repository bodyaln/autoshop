from django.utils.safestring import mark_safe
from django import template
import markdown

register = template.Library()

@register.filter(name='priceedit')
def price_editter(price):
    if(price<1000):
        return price%1000
    else:
        high = price//1000
        low = price%1000
        if(low == 0):
            return (f'{high} 000')
        else:
            return (f'{high} {low}')

@register.filter(name='dist')
def price_editter(dist):
    if(dist<1000):
        return f'{dist%1000} км'
    else:
        return f'{dist//1000} тис. км'




