from django.shortcuts import render
def index(request):
    return render(request, 'home.html')
def about_us(request):
    return render(request, 'aboutus.html')
