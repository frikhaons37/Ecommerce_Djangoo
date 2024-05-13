from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


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
    digital = models.BooleanField(default=False,null=True, blank=True)
    libelle = models.CharField(max_length=100)
    description = models.TextField(default='Non définie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    img = models.ImageField(blank=True)
    imgH = models.ImageField(blank=True)

    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.libelle} - {self.prix} €"

    def imageURL(self):
        try:
            return self.img.url
        except AttributeError:
            return ''
	
class CartItem(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.produit.libelle} - {self.quantity}"
#----------------------------------------------------------------------------------------------------------------------------------
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True, unique=True)  # Assurez-vous que l'email est unique

  
    def __str__(self):
        return self.name

   
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def get_total(self):
		total = self.product.prix * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address