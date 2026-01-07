from django.shortcuts import render
from .models import Item
# Create your views here.

def home(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)

def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    context = {
        'item': item
    }
    return render(request, 'detail.html', context)

