from django.shortcuts import render, redirect
from .forms import *
from .models import store, product, cart, cartItem
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
def checkout(request):
    userCart = cart.objects.get(user=request.user)
    cartItems = cartItem.objects.filter(cart=userCart)
    origins = set(x.origin for x in cartItems)
    context = {
        'cart': userCart,
        'cartItems': cartItems,
        'origins': origins
    }
    return render(request, 'Stocks/checkout.html', context)

@login_required
def modify_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        action = data['action']


        if action == 'add':
            productId = data['productId']
            storeId = data['storeId']
            item = product.objects.get(id=productId)
            itemOrigin = store.objects.get(id=storeId)

            currentCart = cart.objects.get(user=request.user)
            currentCart.active = True
            try:
                newItem = cartItem.objects.get(cart=currentCart, product=item.id, origin=itemOrigin)
            except:
                newItem = None
            if not newItem:
                newItem = cartItem.objects.create(
                    cart = currentCart,
                    product = item,
                    quantity = 1,
                    unit_price = item.price,
                    origin = itemOrigin
                )
            else:
                if newItem.quantity >= 3:
                    return JsonResponse({
                        'success': False,
                        'message': 'You can add up to a maximum of 3 units of every product per store.'
                    })
                newItem.quantity += 1
                newItem.save()
            
            return JsonResponse({
                'success': True,
                'message': f'{newItem} from {newItem.origin} was added to cart, total in cart is {newItem.quantity} {newItem.total}'
            })

        elif action == 'remove':
            cartItemId = data['cartItemId']
            try:
                item_to_remove = cartItem.objects.get(id=cartItemId)
            except:
                return JsonResponse({'success': False})
            if item_to_remove.quantity <= 1:
                item_to_remove.delete()
                return JsonResponse({
                'success': True,
                'message': f'{item_to_remove} from {item_to_remove.origin} is no longer in your cart'
                })
            
            item_to_remove.quantity -= 1
            item_to_remove.save()
            
            return JsonResponse({
                'success': True,
                'message': f'1 unit of {item_to_remove} from {item_to_remove.origin} was removed from your cart'
            })
        
        elif action == 'delete':
            cartItemId = data['cartItemId']
            
            try:
                item_to_remove = cartItem.objects.get(id=cartItemId)
                item_to_remove.delete()
                return JsonResponse({
                'success': True,
                'message': f'all units of {item_to_remove} from {item_to_remove.origin} were removed of the cart'
                })
            except:
                return JsonResponse({'success': False})
                
@login_required
def simulate_purchase(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cartId = data['cartId']

        cart_to_purchase = cart.objects.get(id=cartId)

        items = cartItem.objects.filter(cart=cart_to_purchase)

        for x in items:
            storeItem = amount_of_product.objects.get(product=x.product, stock=x.origin.stock)
            globalItem = product.objects.get(id=x.product.id)
            storeItem.quantity -= x.quantity
            globalItem.sold += x.quantity
            storeItem.save()
            globalItem.save()
            x.delete()

        return JsonResponse({
            'success': True,
            'message': 'Purchase simulated correctly! all the items were removed from their respective stores.'
        })
