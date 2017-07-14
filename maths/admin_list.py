from django import template


register = template.Library()
register.filter('division_intro', division_intro)