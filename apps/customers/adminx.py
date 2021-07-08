import xadmin

from apps.customers.models import Company, KeyPerson, Opportunity


class CompanyAdmin(object):
    list_display = ["name", "category", "address", "add_time"]
    search_fields = ["name", "category"]
    list_filter = ["name", "category"]
    list_editable = ["name", "category"]


class KeyPersonAdmin(object):
    list_display = ["name", "mobile", "company", "position", "add_time"]
    search_fields = ["name", "mobile", "company"]
    list_filter = ["name", "mobile", "company"]
    list_editable = ["name", "mobile", "company", "position"]


class OpportunityAdmin(object):
    list_display = ["company", "person", "product", "status", "add_time"]
    search_fields = ["company", "person", "product", "status"]
    list_filter = ["person__name", "status"]
    list_editable = ["company", "product", "status"]


xadmin.site.register(Opportunity, OpportunityAdmin)
xadmin.site.register(KeyPerson, KeyPersonAdmin)
xadmin.site.register(Company, CompanyAdmin)




