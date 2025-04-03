from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()


# @register.filter
@register.filter(name='cur')
# @register.filter(name='cur', expects_localtime=True)
# @stringfilter
def currency(value, name='тг.'):
    # return f'<strong>{value:.2f}</strong> {name}'
    result_string = f'<strong>{value:.2f}</strong> {name}'
    # return mark_safe(escape(result_string))
    return mark_safe(result_string)

# register.filter('currency', currency)


# @register.simple_tag
# def lst(sep, *args):
@register.simple_tag(takes_context=True)
def lst(context, sep, *args):
    # return f'{sep.join(args)} (итого: {len(args)})'
    return mark_safe(f'{sep.join(args)} (итого: <strong>{len(args)}</strong>)')


@register.inclusion_tag('tags/ulist.html')
def ulist(*args):
    return {'items': args}
