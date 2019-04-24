from django.template import library
from Star.models import Picture,Article

register = library.Library()

@register.filter("pic")
def pic(obj,num):
    pic = Picture.objects.filter(star_id=obj.id)[num-1].picture
    return pic

@register.filter("des")
def description(obj,num):
    des = Picture.objects.filter(star_id=obj.id)[num-1].description
    return des

@register.filter("part")
def part(str):
    return str[:45]

@register.filter("pic1")
def pic1(obj):
    pic = Picture.objects.filter(star_id=obj.id).first().picture
    return pic