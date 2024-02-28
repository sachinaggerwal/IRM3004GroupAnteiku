from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'culinaryCorner/homepage.html')

def about(request):
    return render(request, 'culinaryCorner/about.html')

def contact(request):
    return render(request, 'culinaryCorner/contact.html')

def faq(request):
    return render(request, 'culinaryCorner/faq.html')

def orders(request):
    return render(request, 'culinaryCorner/orders.html')