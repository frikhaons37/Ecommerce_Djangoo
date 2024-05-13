from django.contrib import admin
from .models import Produit,Categorie
from .models import *

admin.site.register(Customer)
admin.site.register(Produit)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Categorie)
