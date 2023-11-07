from django.shortcuts import render
from ecommerce_app.models import Product
from django.db.models import Q


# Create your views here.
def search(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(pname__contains=query) | Q(pdescription__contains=query))


    return render(request,'search.html',{'products':products,'query':query})

