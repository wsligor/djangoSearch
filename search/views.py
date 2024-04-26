from django.shortcuts import render


# Create your views here.
def searchView(request):
    return render(request, 'base.html')
