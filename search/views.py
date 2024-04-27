from django.shortcuts import render
from .models import Sku


# Create your views here.
def searchListView(request):
    sku = Sku.objects.all()
    return render(request, 'search/searchList.html', {'sku': sku})
