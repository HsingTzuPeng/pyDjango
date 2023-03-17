from django.shortcuts import render
from .models import Vendor

# Create your views here.

def showtemplate(request):
    vendor_list = Vendor.objects.all()
    context = {'vendor_list': vendor_list}
    # print(vendor_list)
    return render(request, 'vendor/vendor_detail.html', context)