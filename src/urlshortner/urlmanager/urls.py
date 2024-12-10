from django.urls import path
from .views import ViewHandler
urlpatterns = [
    path("shorten/" , ViewHandler.as_view() , name='shorten'),
    path("shorten/<str:pk>/", ViewHandler.as_view(), name='shorten'),

]