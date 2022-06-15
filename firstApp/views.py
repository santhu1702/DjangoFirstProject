from pydoc_data.topics import topics
from django.shortcuts import render
from django.http import HttpResponse


# # Create your views here.
# def index(request):
#     return HttpResponse("This is view model inside the firstApp")



# def sports_view(request):  -----> 
#     return HttpResponse("This is sports View")



# def finance_view(request):
#     return HttpResponse("This is sports View")



# DynamicURLs


articles = {
    'sports':"This is sports View",
    'finance':"This is finance View",
    'politics':'"This is politics View"'
}

def dynamic_view(request,topics):
    return HttpResponse(articles[topics])


def sum_view(reqest,num1,num2):
    sum = num1 + num2
    return HttpResponse(f'{num1} + {num2} = {sum} ')

