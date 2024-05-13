from audioop import reverse
from unittest import loader
from .models import Produit,Categorie
from .forms import ProduitForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import FournisseurForm
from .forms import CommandeForm
from .models import Fournisseur
from .models import Commandes
from django import forms
from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm,UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from magasin.serializers import CategorySerializer,ProduitSerializer,FournisseurSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth import logout
from django.shortcuts import redirect
#imprimer
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from client.models import OrderItem
#Home
def home(request):
    list=Produit.objects.all()
    return render(request, 'magasin/home.html',{'list':list})
#Produits
def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        list = Produit.objects.filter(libelle__icontains=q)
    else:
        list = Produit.objects.all()
    return render(request, 'magasin/vitrine.html', {'list': list})


def ajout(request):
      if request.method == "POST" :
            form = ProduitForm(request.POST,request.FILES)
            if form.is_valid():
                  form.save()   
                  return HttpResponseRedirect('/magasin')
      else :
            form = ProduitForm() #créer formulaire vide
      return render(request,'magasin/majProduits.html',{'form':form})

def deleteP(request,id):
    list=Produit.objects.get(id=id)
    list.delete()
    return redirect('index')

def edit_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'magasin/edit_produit.html', {'form': form})

           #Recherche par catégorie

def produits_par_categorie(request, categorie_id):
    categorie = Categorie.objects.get(pk=categorie_id)
    produits = Produit.objects.filter(categorie=categorie)
    return render(request, 'ListCategorie.html', {'produits': produits})
#fournisseur
class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'adresse', 'email', 'telephone']
def liste_fournisseurs(request):
    if 'q' in request.GET:
        q = request.GET['q']
        fournisseurs = Fournisseur.objects.filter(nom__icontains=q) | Fournisseur.objects.filter(telephone__icontains=q)
    else:
        fournisseurs = Fournisseur.objects.all()

    return render(request, 'magasin/ListFournisseur.html', {'fournisseurs': fournisseurs})
#imprimer
def imprimer(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'magasin/imprimer.html', {'fournisseurs': fournisseurs})



#############################
def nouveauFournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            # Récupérer à nouveau la liste des fournisseurs après l'ajout
            fournisseurs = Fournisseur.objects.all()
            return render(request, 'magasin/ListFournisseur.html', {'fournisseurs': fournisseurs})
    else:
        form = FournisseurForm()
    return render(request, 'magasin/AjoutFournisseur.html', {'form': form})
def edit_fournisseur(request, fournisseur_id):
    fournisseur = get_object_or_404(Fournisseur, pk=fournisseur_id)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, request.FILES, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('ListFournisseur')  
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'magasin/edit_fournisseur.html', {'form': form})
def deleteF(request,id):
    fournisseurs=Fournisseur.objects.get(id=id)
    fournisseurs.delete()
    return redirect('ListFournisseur')

#Commande
from datetime import datetime

def liste_commandes(request):
    if 'q' in request.GET:
        q = request.GET['q']
        try:
            date_q = datetime.strptime(q, '%Y-%m-%d').date()
            commandes = Commandes.objects.filter(dateCde=date_q) 
        except ValueError:
            # Gérer l'erreur si la chaîne de date n'est pas au format attendu
            commandes = Commandes.objects.none()
    else:
        commandes = Commandes.objects.all()

    return render(request, 'magasin/ListCommande.html', {'commandes': commandes})


def nouveauCommande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            commandes = Commandes.objects.all()
            return render(request, 'magasin/ListCommande.html', {'commandes': commandes})
    else:
        form = CommandeForm()
    return render(request, 'magasin/AjoutCommande.html', {'form': form})
def deleteC(request,id):
    commandes = Commandes.objects.all()
    commandes.delete()
    return redirect('ListCommande')
def edit_commande(request, commande_id):
    commande = get_object_or_404(Commandes, pk=commande_id)
    if request.method == 'POST':
        form = CommandeForm(request.POST, request.FILES, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('ListCommande')  
    else:
        form = CommandeForm(instance=commande)
    return render(request, 'magasin/edit_commande.html', {'form': form})
#Categorie
def clothes(request):
    produits = Produit.objects.filter(categorie__name='Clothes')
    return render(request, 'magasin/clothes.html', {'produits': produits})
def footwear(request):
    produits = Produit.objects.filter(categorie__name='Footwear')
    return render(request, 'magasin/footwear.html', {'produits': produits})
def jewelry(request):
    produits = Produit.objects.filter(categorie__name='Jewerly')
    return render(request, 'magasin/jewelry.html', {'produits': produits})
def perfume(request):
    produits = Produit.objects.filter(categorie__name='Perfume')
    return render(request, 'magasin/perfume.html', {'produits': produits})
def cosmetics(request):
    produits = Produit.objects.filter(categorie__name='Cosmetics')
    return render(request, 'magasin/cosmetics.html', {'produits': produits})
def glasses(request):
    produits = Produit.objects.filter(categorie__name='Glasses')
    return render(request, 'magasin/glasses.html', {'produits': produits})
def bags(request):
    produits = Produit.objects.filter(categorie__name='Bags')
    return render(request, 'magasin/bags.html', {'produits': produits})

#Register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Bonjour {username}, votre compte a été créé avec succès !')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
#logout
def deconnexion(request):
    logout(request)
    return redirect('accueil')
#Api--------------------------------------------------------------------------
class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
class ProduitAPIView(APIView):
    def get(self, request, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)
class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer

    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset

class   FournisseurAPIView(APIView):
    def get(self, request, *args, **kwargs):
        fournisseurs = Fournisseur.objects.all()
        serializer = FournisseurSerializer(fournisseurs, many=True)
        return Response(serializer.data)
def generate_pdf(request):
    fournisseurs = Fournisseur.objects.all()

    template_path = 'magasin/imprimer.html' 

    context = {'fournisseurs': fournisseurs}

    # Rendre le modèle HTML
    template = get_template(template_path)
    html = template.render(context)

    # Créer un objet PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ListFournisseur.pdf"'

    # Convertir le modèle HTML en PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Une erreur s\'est produite lors de la génération du PDF.')

    return response