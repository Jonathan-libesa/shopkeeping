from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def home(request):
    product=Product.objects.all()
    context={'product':product}
    return render(request,'home.html',context)


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})
