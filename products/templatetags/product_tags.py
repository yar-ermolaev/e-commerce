from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def merge_params(context, **kwargs):
    query_parameters = context['request'].GET.copy()
    if 'page' in query_parameters and 'page' in kwargs:
        query_parameters['page'] = kwargs['page']
        kwargs.pop('page')
    query_parameters.update(kwargs)
    return query_parameters.urlencode()
