from django.db import models
from registration.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.address = self.address.capitalize()
        super().save(*args, **kwargs)
    
class product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=100)
    on_sale = models.BooleanField(default=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.description = self.description.capitalize()
        super().save(*args, **kwargs)
    
class stock(models.Model):
    store = models.OneToOneField(store, on_delete=models.CASCADE)
    products = models.ManyToManyField(product, through='amount_of_product')

    def __str__(self):
        return f'Stock from -{self.store}'
    
class amount_of_product(models.Model):
    stock = models.ForeignKey(stock, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    sold = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('stock', 'product')

    def __str__(self):
        return f'{self.product.name} -{self.stock.store}'
    
class cart(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} Cart"

class cartItem(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.product

@receiver(post_save, sender=store)
def create_stock(sender, instance, created, **kwargs):
    if created:
        stock.objects.create(store=instance)