from django import forms

from .models import Vendor, Food

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        #fileds : 使用 Model 的哪些欄位
        labels = {
            'vendor_name': _('攤販名稱'),
            'store_name' : _('店名'),
            'phone_number' : _('電話'),
            'address' : _('地址'),
        }