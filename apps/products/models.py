from django.db import models
from datetime import datetime

from apps.users.models import BaseModel


class Type(BaseModel):
    name = models.CharField(max_length=20, verbose_name="名称")
    desc = models.CharField(max_length=200, verbose_name="描述")

    class Meta:
        verbose_name = "产品类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(verbose_name="型号", max_length=30)
    manufacturer = models.CharField(verbose_name="厂家", max_length=30)
    parameter = models.CharField(verbose_name="主要参数", max_length=200)
    price = models.IntegerField(verbose_name="售价", default=0)
    cost = models.IntegerField(verbose_name="成本", default=0)
    stock = models.IntegerField(verbose_name="库存", default=0)

    image = models.ImageField(upload_to="products/%Y/%m", verbose_name="图片", max_length=100)

    class Meta:
        verbose_name = "产品管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ProductList(BaseModel):
    num = models.CharField(verbose_name="编号", max_length=30,
                           default=datetime.now().strftime('Product_List_%Y%m%d%H%M%S'))
    desc = models.CharField(max_length=200, verbose_name="描述", blank=True, default="")
    products = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="产品")
    count = models.IntegerField(verbose_name="数量", default=1)
    discount = models.IntegerField(verbose_name="折扣", default=0)

    class Meta:
        verbose_name = "配置清单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.num

