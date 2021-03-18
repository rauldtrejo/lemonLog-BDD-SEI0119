import datetime
from django import template
from datetime import date

register = template.Library()

@register.filter()
def date_difference(value):
    article_date = value
    today = date.today()

    age = today - article_date

    return age.days