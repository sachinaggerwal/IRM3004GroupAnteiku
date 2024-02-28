from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'culinaryCorner/homepage.html')

def about(request):
    return render(request, 'culinaryCorner/about.html')