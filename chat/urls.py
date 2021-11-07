from django.urls import path
from .views import home, messageList, messageCreate, messageDetail, messageUpdate, messageDelete

urlpatterns = [
    path('', home, name="home"),
    path('list/', messageList, name="message-list"),
    path('detail/<str:pk>/', messageDetail, name="message-detail"),
    path('create/', messageCreate, name="message-create"),
    path('update/<str:pk>/', messageUpdate, name="message-update"),
    path('delete/<str:pk>/', messageDelete, name="message-delete"),
]
