from django import template

register = template.Library()

@register.filter()
def leng(value):
    return len(value)/2

@register.filter()
def cost(value):
    return value*1000000

