from django import forms

from .models import Vendor, Food

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        #fileds : 使用 Model 的哪些欄位