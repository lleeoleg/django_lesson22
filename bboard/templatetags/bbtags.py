from django import template
from django.template.defaultfilters import stringfilter
# from django.utils.html import escape
from django.utils.safestring import mark_safe


register = template.Library()


# @register.filter
@register.filter(name='cur')
# @register.filter(name='cur', expects_localtime=True)
# @stringfilter
def currency(value, name='тг.'):
    # return f'<strong>{value:.2f}</strong> {name}'
    result_string = f'<strong>{value:.2f}</strong> {name}'
    return mark_safe(result_string)


@register.simple_tag(takes_context=True) 
def lst(context, sep, *args):
    return mark_safe(f'{sep.join(args)} (Итого: <strong>{len(args)}</strong>)')
    
@register.inclusion_tag('tags/ulist.html')
def ulist(*args):
    return {'items': args}


@register.filter(name='dividestring')
def dividestring(value):
    if isinstance(value, str):
        return value[:len(value) // 2]
    return value 

@register.simple_tag
def mytag(value, sep=" "):
    if isinstance(value, str):
        parts = value.split(sep)
        return mark_safe("***".join(parts))
    return value




register.filter('currency', currency)
