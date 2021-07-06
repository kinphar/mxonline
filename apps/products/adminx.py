import xadmin

from apps.products.models import Product


class ProductAdmin(object):
    list_display = ["name", "manufacturer", "parameter", "stock"]
    search_fields = ["name", "manufacturer", "parameter", "stock"]
    list_filter = ["name", "manufacturer", "parameter", "stock"]
    list_editable = ["name", "manufacturer", "parameter", "stock"]


xadmin.site.register(Product, ProductAdmin)

