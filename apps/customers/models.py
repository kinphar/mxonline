from django.db import models

from apps.users.models import BaseModel
from apps.products.models import Product


class Company(BaseModel):
    name = models.CharField(verbose_name="公司名称", max_length=50)
    address = models.CharField(verbose_name="公司地址", max_length=150)
    desc = models.TextField(verbose_name="备注", max_length=100, blank=True, default="")
    category = models.CharField(default="zd", verbose_name="类型", max_length=3,
                                choices=(("zd", "终端客户"), ("jcs", "集成商")))

    class Meta:
        verbose_name = "目标公司"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class KeyPerson(BaseModel):
    name = models.CharField(verbose_name="姓名", max_length=50)
    mobile = models.CharField(verbose_name="电话", max_length=11)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="就职公司")
    position = models.CharField(verbose_name="职位", max_length=50, default="未知")
    come_from = models.CharField(verbose_name="哪里人", max_length=50, blank=True)
    age = models.IntegerField(verbose_name="年龄", default=18, blank=True)
    desc = models.CharField(verbose_name="备注", max_length=100, blank=True, default="")
    image = models.ImageField(upload_to="customers/%Y/%m", verbose_name="照片", max_length=100, blank=True)

    class Meta:
        verbose_name = "关键人物"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    ("wbb", "未报备"),
    ("bbz", "报备中"),
    ("ybb", "已报备"),
    ("bbcq", "报备超期"),
    ("bbsb", "报备失败"),
    ("ycj", "已成交"),
)


class Opportunity(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="购买方")
    person = models.ForeignKey(KeyPerson, on_delete=models.CASCADE, verbose_name="关键人物")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="产品配置")
    status = models.CharField(default="wbb", verbose_name="状态", max_length=4, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = "销售机会"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.person.name

