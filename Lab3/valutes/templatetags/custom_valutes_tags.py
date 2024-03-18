from django import template

register = template.Library()

@register.filter(name='money_format')
def money_format(value):
    value = str(value)
    value = value.replace(',', '.')
    try:
        return '{0:.2f} руб'.format(float(value))
    except (TypeError, ValueError):
        return f'{value} руб.'