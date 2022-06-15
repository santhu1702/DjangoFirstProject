from django.urls import  path
from django.views import View
from . import views

urlpatterns = [
    # path('',views.index,name='index')
    # path('sports',views.sports_view),
    # path('finance',views.finance_view)

    path('<topics>/',views.dynamic_view),
    path('<int:num1>/<int:num2>',views.sum_view)
]