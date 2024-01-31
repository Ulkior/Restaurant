from django import template

from kitchen.models import Category


register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.filter(parent=None)