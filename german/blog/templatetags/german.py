from django.template import Library

from zinnia.models.category import Category

register = Library()

@register.inclusion_tag('zinnia/tags/categories_simple.html', takes_context=True)
def get_categories_simple(context, template='zinnia/tags/categories.html'):
    """
    Return the published categories (simple output).
    """
    return {'template': template,
            'categories': Category.published.all(), }