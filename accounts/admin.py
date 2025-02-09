from django.contrib import admin
from .models import *
from django.utils.html import format_html
from import_export import resources # type: ignore
from import_export.admin import ExportActionMixin # type: ignore

# Register your models here.
admin.site.site_header = "Ice cream Shop"
admin.site.site_title = "Ice cream shop Admin Panel"
admin.site.index_title = "Admin Panel"


class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_preview","id","productImage","productName","categoryID","quantity","priceIn","instock","priceOut","productDate"]
    list_filter = ["productDate"]
    search_fields = ["productName"]
    date_hierarchy = "productDate"

    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        if obj.productImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.productImage.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'

class ExpCategory(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('categoryName','CategoryImage')


class CategoryAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["image_preview","id","CategoryName","CategoryImage","Date_created"]
    list_filter = ["Date_created"]
    search_fields = ["CategoryName"]
    date_hierarchy = "Date_created"
    resourece_class = ExpCategory
    readonly_fields = ["image_preview"] 

    def image_preview(self, obj):
        if obj.CategoryImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.CategoryImage.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","name","phone","email","date_created"]
    list_filter = ["date_created"]
    search_fields = ["name"]
    date_hierarchy = "date_created"
admin.site.register(Customer)
admin.site.register(Category, CategoryAdmin)
admin.site.register(tblProducts, ProductAdmin)
admin.site.register(tblClients)
admin.site.register(tblSocialMedia)
admin.site.register(tblTopMenu)
admin.site.register(tblGallery)
admin.site.register(tblSlides)
admin.site.register(tblProductDetail)
admin.site.register(tblFooter)
admin.site.register(tblSubFooter)
admin.site.register(Contact)
admin.site.register(Gallery)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(tblTopMenu2)