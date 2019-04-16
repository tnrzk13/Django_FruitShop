from django.contrib import admin
#import product model
from .models import Product
from .models import Offer

class ProductAdmin(admin.ModelAdmin): #specifies what should be visible in your products table
    list_display = ("name", "price", "stock")

class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")

# # Register your models here.
admin.site.register(Product, ProductAdmin) #can work with ProductAdmin, but your product table won"t show properly
admin.site.register(Offer, OfferAdmin)