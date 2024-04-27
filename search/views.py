from django.shortcuts import render


# Create your views here.
def searchListView(request):
    return render(request, 'search/searchList.html')
