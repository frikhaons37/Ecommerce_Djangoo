from django.forms import ModelForm
from .models import Produit
from .models import Fournisseur
from .models import Commandes
class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__" 

class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'  


class CommandeForm(ModelForm):
    class Meta:
        model = Commandes
        fields = '__all__'  