from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Product


class ProductsView(ListView):
    template_name = 'product/products_view.html'
    context_object_name = 'products_list'
    model = Product
    paginate_by = 5
    paginate_orphans = 0






