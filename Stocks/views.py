from django.shortcuts import render, redirect
from .forms import *
from .models import store, product, stock
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

def index(request):
    if request.user.is_authenticated:
        context = {
            'user': request.user,
            'form': CreateStoreForm,
            'stores': store.objects.all().filter(owner = request.user)
        }
        
        return render(request, 'Stocks/index.html', context)
    else:
        return redirect('/login')

@login_required    
def create_store(request):
    if request.method == 'POST':
        form = CreateStoreForm(request.POST)
        
        if form.is_valid():
            newStore = form.save(commit=False)
            newStore.owner = request.user
            newStore.save()

        return redirect('/')
    
@login_required
def stores_stock(request, store_id):
    currentStore = store.objects.get(id=store_id)
    stock = currentStore.stock
    form = AddProductForm(user=request.user)
    context = {
            'user': request.user,
            'form': form,
            'store': currentStore,
            'stock': stock
        }
    return render(request, 'Stocks/stock.html', context)

@login_required    
def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()

    return redirect(f'/products/{request.user.id}')

@login_required
def products(request, user_id):
    currentProducts = product.objects.all().filter(owner=user_id)
    context = {
            'user': request.user,
            'form': CreateProductForm,
            'products': currentProducts,
        }
    
    return render(request, 'Stocks/products.html', context)

@login_required    
def add_product(request, store_id):
    if request.method == 'POST':
        form = AddProductForm(request.user, request.POST)
        currentStock = store.objects.get(id=store_id).stock
        
        if form.is_valid():
            newProduct = form.save(commit=False)
            try:
                check = amount_of_product.objects.get(
                    product=newProduct.product, stock=currentStock)
                check.quantity += newProduct.quantity
                check.save()
            except:
                newProduct.stock = currentStock
                newProduct.save()

    return redirect(f'/stock/{store_id}')

@login_required
def modify_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        action = data['action']
        productId = data['productId']
        item = product.objects.get(id=productId)
        print(action, item.name)
        return JsonResponse({'success': True, 'message': f'{item.name} added to cart'})