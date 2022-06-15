from django.http import HttpResponse


def Home_view(request):
    return HttpResponse("this is homepage")
