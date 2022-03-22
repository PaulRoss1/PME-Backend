from django.urls import path, include
from event import views


urlpatterns = [
    path('today-events/<str:date>/', views.TodayEventsList.as_view()),
    path('search/', views.search),
    path('<str:slug>/<int:id>', views.EventDetail.as_view()),
    path('<str:category>/<str:time_frame>/', views.EventsList.as_view()),    
]