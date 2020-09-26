"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from webapp.views import ProductsView, OneProductView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ReviewCreateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),

    path('', ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', OneProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_create_view'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('product/<int:pk>/review/add/', ReviewCreateView.as_view(), name='review_create'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
