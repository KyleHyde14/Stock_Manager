from django import forms
from .models import store, product, amount_of_product

class CreateStoreForm(forms.ModelForm):
    class Meta:
        model = store
        exclude = ['owner']
        fields = ['name', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Store name'
        self.fields['address'].widget.attrs['placeholder'] = 'Store address'

class CreateProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = product
        exclude = ['sold', 'owner']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Product name'
        self.fields['price'].widget.attrs['placeholder'] = 'Price in dollars'
        self.fields['price'].widget.attrs['inputmode'] = 'numeric'
        self.fields['description'].widget.attrs['placeholder'] = 'A description about the product'
    
class AddProductForm(forms.ModelForm):
    quantity = forms.IntegerField(initial=1)
    class Meta:
        model = amount_of_product
        exclude = ['stock', 'sold']
        fields = '__all__'
    
    def __init__(self, user, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = product.objects.filter(owner=user)
        self.fields['quantity'].widget.attrs['min'] = 1

