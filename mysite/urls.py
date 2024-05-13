
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import accueil
from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView
from django.urls import path
from . import views
router = routers.SimpleRouter()
router.register('produit', ProductViewset, basename='produit')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('magasin/', include('magasin.urls')),
    path('client/', include('client.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    
    path('', accueil, name='accueil'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

        path('deconnexion/', views.deconnexion, name='deconnexion'),


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

