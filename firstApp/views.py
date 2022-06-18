from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# # Create your views here.
# def index(request):
#     return HttpResponse("This is view model inside the firstApp")



# def sports_view(request):  -----> 
#     return HttpResponse("This is sports View")



# def finance_view(request):
#     return HttpResponse("This is sports View")



# DynamicURLs


# articles = {
#     'sports':"This is sports View",
#     'finance':"This is finance View",
#     'politics':'"This is politics View"'
# }

# def dynamic_view(request,topics):
#     try:        
#         return HttpResponse(articles[topics])
#     except:
#         # result = "Page is not found"
#         # return HttpResponseNotFound(result)
#         raise Http404("404 generic error")
    


# def sum_view(reqest,num1,num2):
#     sum = num1 + num2
#     return HttpResponse(f'{num1} + {num2} = {sum} ')

# def num_page_view(request,numpage):

#     topic_list = list(articles.keys())
#     topic = topic_list[numpage]

#     return HttpResponseRedirect(reverse('topic_page',args=[numpage]))



