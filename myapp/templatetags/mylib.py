from django import template

register = template.Library()


@register.inclusion_tag('two.html')
def includetwo():
    return {}


@register.inclusion_tag('three.html')
def includethree():
    return {}
