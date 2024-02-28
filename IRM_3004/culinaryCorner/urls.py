from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('about/',views.about,name="about"),
    path('faq/',views.about,name="faq"),
    path('contact/',views.about,name="contact"),
    path('orders/',views.about,name="about")
]