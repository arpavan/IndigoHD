from django.contrib import admin

# Register your models here.
from .models import Customers
from .models import KeywordCategoryUrlMap
from .models import CategoryCustomerMap

admin.site.register(Customers)
admin.site.register(CategoryCustomerMap)
admin.site.register(KeywordCategoryUrlMap)
