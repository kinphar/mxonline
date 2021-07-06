import xadmin

from apps.customers.models import Company, KeyPerson, Opportunity


class CompanyAdmin(object):
    list_display = ["name", "category", "address"]
    search_fields = ["name", "category"]
    list_filter = ["name", "category"]
    list_editable = ["name", "category"]


class KeyPersonAdmin(object):
    list_display = ["name", "mobile", "company", "come_from"]
    search_fields = ["name", "mobile", "company", "come_from"]
    list_filter = ["name", "mobile", "company", "come_from"]
    list_editable = ["name", "mobile", "company", "come_from"]


class OpportunityAdmin(object):
    list_display = ["person", "company", "product", "status"]
    search_fields = ["person", "company", "product", "status"]
    list_filter = ["person", "company", "product", "status"]
    list_editable = ["status"]


xadmin.site.register(Company, CompanyAdmin)
xadmin.site.register(KeyPerson, KeyPersonAdmin)
xadmin.site.register(Opportunity, OpportunityAdmin)


