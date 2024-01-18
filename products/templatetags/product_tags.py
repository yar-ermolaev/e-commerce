from django import template
from django.utils.http import urlencode


register = template.Library()


@register.simple_tag(takes_context=True)
def merge_params(context, **kwargs):
    query_parameters = context['request'].GET.dict()
    query_parameters.update(kwargs)
    return urlencode(query_parameters)
