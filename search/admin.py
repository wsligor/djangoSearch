from django.contrib import admin
from .models import Company, Groups, Sku


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slag', 'fullname', 'created', 'updated')
    prepopulated_fields = {'slag': ('name',)}


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slag', 'sort', 'cut', 'created', 'updated')
    prepopulated_fields = {'slag': ('name',)}


@admin.register(Sku)
class SkuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'gtin', 'prefix', 'company', 'group', 'created', 'updated')
    prepopulated_fields = {'slug': ('name',)}
