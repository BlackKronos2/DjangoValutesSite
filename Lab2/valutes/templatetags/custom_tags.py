from django import template

register = template.Library()

@register.simple_tag
def convert_currency(value, multiplier):
    try:
        #value = float(value)  # Преобразуем значения в число, если это возможно
        #multiplier = float(multiplier)
        #calculated_value = value * multiplier
        return f'm = {multiplier} v = {value}'
        #return round(calculated_value, 2)  # Округляем результат до двух знаков после запятой
    except (ValueError, TypeError):
        return 'Error!!!'  # Обработка ошибки для неправильных входных данных