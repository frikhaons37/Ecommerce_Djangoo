from django.shortcuts import get_object_or_404, render
from .models import Produit
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder

#Home
def Home(request):
    list=Produit.objects.all()
    return render(request, 'client/home.html',{'list':list})
#Produit
def product_details(request, product_id):

    product = get_object_or_404(Produit, pk=product_id)
    return render(request, 'client/details.html', {'product': product})
    #Affichage liste produit
def ListProduit(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    if 'q' in request.GET:
        q = request.GET['q']
        list_products = Produit.objects.filter(libelle__icontains=q)
        context = {'list': list_products, 'cartItems': cartItems}
    else:
        list_products = Produit.objects.all()
        context = {'list': list_products, 'cartItems': cartItems}
    
    return render(request, 'client/ListProduit.html', context)
#Categorie
def clothess(request):
    
    produits = Produit.objects.filter(categorie__name='clothes')

    return render(request, 'client/clothess.html', {'produits': produits})
def footwears(request):
    produits = Produit.objects.filter(categorie__name='footwear')
    return render(request, 'client/footwears.html', {'produits': produits})
def jewelrys(request):
    produits = Produit.objects.filter(categorie__name='jewerly')
    return render(request, 'client/jewelrys.html', {'produits': produits})
def perfumes(request):
    produits = Produit.objects.filter(categorie__name='perfume')
    return render(request, 'client/perfumes.html', {'produits': produits})
def cosmeticss(request):
    produits = Produit.objects.filter(categorie__name='cosmetics')
    return render(request, 'client/cosmeticss.html', {'produits': produits})
def glassess(request):
    produits = Produit.objects.filter(categorie__name='glasses')
    return render(request, 'client/glassess.html', {'produits': produits})
def bagss(request):
    produits = Produit.objects.filter(categorie__name='bags')
    return render(request, 'client/bagss.html', {'produits': produits})
#----------------------------------------------------------------------------------------------------------------------------------
def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'client/cart.html', context)


def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'client/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Produit.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)



