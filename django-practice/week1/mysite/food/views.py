#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def favourite_foods(request):
    foods = ["rice", goats", "chicken", "gnuts", "beans", "fish"]
    output = ""
    for food in foods:
        if lon(food)>4
           output += f"i love {food} today!<br>" #<br> means line break
    return HttpResponse(output)       