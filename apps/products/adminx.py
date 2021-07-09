import xadmin

from apps.products.models import Product, ProductList


class ProductAdmin(object):
    list_display = ["name", "manufacturer", "parameter", "stock"]
    search_fields = ["name", "manufacturer", "parameter", "stock"]
    list_filter = ["name", "manufacturer", "parameter", "stock"]
    list_editable = ["name", "manufacturer", "parameter", "stock"]


class ProductListAdmin(object):
    list_display = ["num"]
    search_fields = ["num"]
    list_filter = ["num"]
    list_editable = ["num"]


xadmin.site.register(Product, ProductAdmin)
xadmin.site.register(ProductList, ProductListAdmin)


