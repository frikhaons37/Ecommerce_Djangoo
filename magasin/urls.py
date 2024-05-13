from django.urls import path
from . import views
from django.contrib import admin, auth
from .views import CategoryAPIView,ProduitAPIView,FournisseurAPIView
from django.contrib.auth import views as auth_views


urlpatterns = [ 
     path('', views.index, name='index'),
     path('Home', views.home, name='home'),
#Produits
     path('majProduits', views.ajout, name='majProduits'),
     path('AjoutProduit', views.ajout, name='ajout'),
     path('deleteP/<int:id>/',views.deleteP,name='deleteP'),
     path('produit/<int:produit_id>/edit/', views.edit_produit, name='edit_produit'),

#Fournisseurs
     path('AjoutFournisseur/', views.nouveauFournisseur, name='AjoutFournisseur'),
     path('ListFournisseur/', views.liste_fournisseurs, name='ListFournisseur'),
     path('deleteF/<int:id>/',views.deleteF,name='deleteF'),
     path('fournisseur/<int:fournisseur_id>/edit/', views.edit_fournisseur, name='edit_fournisseur'),

#Commande
     path('ListCommande/', views.liste_commandes, name='ListCommande'),
     path('AjoutCommande/', views.nouveauCommande, name='AjoutCommande'),
     path('deleteC/<int:id>/',views.deleteC,name='deleteC'),
     path('commande/<int:commande_id>/edit/', views.edit_commande, name='edit_commande'),

#Categorie
    path('clothes/', views.clothes, name='clothes'),
    path('footwear/', views.footwear, name='footwear'),
    path('jewelry/', views.jewelry, name='jewelry'),
    path('perfume/', views.perfume, name='perfume'),
    path('cosmetics/', views.cosmetics, name='cosmetics'),
    path('glasses/', views.glasses, name='glasses'),
    path('bags/', views.bags, name='bags'),
#registrer
    path('register/',views.register, name = 'register'), 
#API REST
 path('api/category/', CategoryAPIView.as_view()),
 path('api/produits/', ProduitAPIView.as_view()),
 path('api/fournisseurs/', FournisseurAPIView.as_view()),

#############
    path('deconnexion/', views.deconnexion, name='deconnexion'),

##########
    
path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('logout',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name ='logout'),



    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
        path('imprimer/', views.imprimer, name='imprimer'),


]

