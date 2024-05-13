from django.db import models
from django.utils import timezone
from datetime import date

class Commandes(models.Model):
    dateCde = models.DateField(null=True, default=timezone.now)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)
    produits = models.ManyToManyField('Produit')

    def __str__(self):
        return str(self.id) + "-Commande le " + str(self.dateCde)
class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)

    def __str__(self):
        return self.nom
class Categorie(models.Model):
    TYPE_CHOICES=[
        ('clothes','Clothes'),
        ('footwear','Footwear'),
        ('jewerly','Jewerly'),
        ('perfume','Perfume'),
        ('cosmetics','Cosmetics'),
        ('glasses','Glasses'),
        ('bags','Bags'),
    ]
    name = models.CharField(max_length=50, default='clothes', choices=TYPE_CHOICES)
    def __str__(self):
        return f"{self.name}"

class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField(default='Non définie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    img = models.ImageField(blank=True)
    imgH = models.ImageField(blank=True)

    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"Libellé: {self.libelle}, Description: {self.description}, Prix: {self.prix},Image: {self.img},Categorie:{self.categorie},Fournisseur:{self.fournisseur}"
class ProduitNC(Produit):
    duree_garantie = models.CharField(max_length=100)

    def __str__(self):
        return f"Libellé: {self.libelle}, Description: {self.description}, Prix: {self.prix}, Type: {self.get_type_display()}, Image: {self.img}, Catégorie: {self.categorie}, Fournisseur: {self.fournisseur}, Durée de garantie: {self.duree_garantie}"