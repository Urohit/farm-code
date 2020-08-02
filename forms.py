from django.forms import ModelForm
from .models import Investment

class ProductForm(ModelForm):
    class Meta:
        model = Investment
        fields = '__all__'
        
