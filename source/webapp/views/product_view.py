from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q, Count, Avg
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductsView(ListView):
    template_name = 'product/products_view.html'
    context_object_name = 'products_list'
    model = Product
    paginate_by = 5
    paginate_orphans = 0

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        avg_marks = []
        for product in products:
            avg_mark = product.review.all().aggregate(avg_mark=Avg('mark'))
            if not avg_mark['avg_mark']:
                avg_mark['avg_mark'] = 0
            avg_marks.append({product.pk: avg_mark['avg_mark']})
        context['avg_marks'] = avg_marks
        print(avg_marks)
        return context




class OneProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product
    paginate_review_by = 5
    paginate_review_orphans = 0


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review, page, is_paginated = self.paginate_comments(self.object)
        product = self.object
        avg_mark = product.review.all().aggregate(avg_mark=Avg('mark'))
        context['avg_mark'] = avg_mark['avg_mark']
        context['reviews'] = review
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        return context

    def paginate_comments(self, project):
        review = project.review.all()
        if review.count() > 0:
            paginator = Paginator(review, self.paginate_review_by, orphans=self.paginate_review_orphans)
            page = paginator.get_page(self.request.GET.get('page', 1))
            is_paginated = paginator.num_pages > 1
            return page.object_list, page, is_paginated
        else:
            return review, None, False


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product/product_create.html'
    form_class = ProductForm
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


# PermissionRequiredMixin,
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/product_update.html'
    form_class = ProductForm
    # permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


# PermissionRequiredMixin,
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('products')
    # permission_required = 'webapp.delete_product'