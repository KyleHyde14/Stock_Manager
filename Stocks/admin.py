from django.contrib import admin
from .models import *

admin.site.register(store)
admin.site.register(product)
admin.site.register(stock)
admin.site.register(amount_of_product)
admin.site.register(cart)
admin.site.register(cartItem)
