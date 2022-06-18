from django.urls import  path
from django.views import View
from . import views

urlpatterns = [
    # path('',views.index,name='index')
    # path('sports',views.sports_view),
    # path('finance',views.finance_view)

#     path('<str:topics>/',views.dynamic_view,name="topic_page"),
#     # path('<int:num1>/<int:num2>',views.sum_view),                         ----->>>> Dynamic Urls Part 
#     path('<int:numpage>/',views.num_page_view)
# ]   

    path('',views.SampleHtml_view)

]