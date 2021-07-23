from django import template

register = template.Library()

@register.filter()
def leng(value):
    return len(value)/2
# math.seil()