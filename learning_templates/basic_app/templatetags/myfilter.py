from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,args):
    """
    This cuts out all the 'args' from the string!
    """

    return value.replace(args,'')

# register.filter('cut',cut)