from django import template
import datetime

register = template.Library()

@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    return datetime.datetime.now().strftime(format_string)
#   return datetime.now().strftime(format_string) (no caso fazendo from datetime la em cima)

@register.simple_tag
def footer_message():
    return 'Desenvolvimento web com Django 3.0'
