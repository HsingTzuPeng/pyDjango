from django.db import models

# Create your models here.


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=20)  # 攤販的名稱
    store_name = models.CharField(max_length=10)  # 攤販店家的名稱
    phone_number = models.CharField(max_length=20)  # 攤販的電話號碼
    address = models.CharField(max_length=100)  # 攤販的地址

    # CharField().max_length 是必要的參數，設定最多可以儲存的長度


class Food(models.Model):
    food_name = models.CharField(max_length=30)  # 食物名稱
    price_name = models.DecimalField(max_digits=3, decimal_places=0)  # 食物價錢
    #  DecimalField()儲存十進制的數字，後面參數分別代表 最大長度、小數點後位數

    food_vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE)  # 代表這食物是由哪一個攤販所做的
    # ForeignKey，在 Django中是 多對一(many-to-one)的關聯，第一個參數代表對應到哪個類別，此為 Vendor
    # on_delete 代表的是當對應的類別被刪除後，這些對應到別人的資料要怎麼被處理，而 CASCADE 就是一倂刪除

# 每一個class都是繼承django.db.models.Model
# 所以類別名稱後方的()就是塞 models.Model
