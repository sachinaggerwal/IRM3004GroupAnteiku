from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('about/',views.about,name="about"),
    path('faq/',views.faq,name="faq"),
    path('contact/',views.contact,name="contact"),
    path('orders/',views.orders,name="about")
]