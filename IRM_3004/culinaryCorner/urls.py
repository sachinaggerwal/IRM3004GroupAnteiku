from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="homepage"),
    path('about/',views.about,name="cc_about")
    path('faq/',views.about,name="cc_faq")
    path('contact/',views.about,name="cc_contact")
    path('orders/',views.about,name="cc_about")
]