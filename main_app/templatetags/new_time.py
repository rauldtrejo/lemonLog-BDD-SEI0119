from django import template
from datetime import date

register = template.Library()

# This custom template tag allows us to calculate the difference between a posted comment or article and the current date.
@register.filter()
def date_difference(value):
    article_date = value
    today = date.today()
    age = today - article_date
    return age.days