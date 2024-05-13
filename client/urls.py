from django.urls import path
from . import views

urlpatterns = [ 
     path('Home', views.Home, name='homee'),
     #Produits
     path('', views.ListProduit, name='ListProduit'),
     path('product/<int:product_id>/', views.product_details, name='product_details'),

     #Categorie
    path('clothes/', views.clothess, name='clothess'),
    path('footwear/', views.footwears, name='footwears'),
    path('jewelry/', views.jewelrys, name='jewelrys'),
    path('perfume/', views.perfumes, name='perfumes'),
    path('cosmetics/', views.cosmeticss, name='cosmeticss'),
    path('glasses/', views.glassess, name='glassess'),
    path('bags/', views.bagss, name='bagss'),
    #Cart
    	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

     ]