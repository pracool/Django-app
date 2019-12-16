from django import template
register=template.Library()

def cut(value,arg):
    """
    this cuts out
    :param value:
    :param arg:
    :return:
    """