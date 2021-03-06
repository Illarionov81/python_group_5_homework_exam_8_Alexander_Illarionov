from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, ReviewForm
from webapp.models import Product, Review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review/review_add.html'
    form_class = ReviewForm

    def form_valid(self, form):
        user = self.request.user
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'),)
        review = form.save(commit=False)
        review.product = product
        review.author = user
        review.save()
        return redirect('product_view', pk=product.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, pk=self.kwargs.get('pk'),)
        return context


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'review/review_change.html'
    form_class = ReviewForm
    model = Review
    context_object_name = 'review'
    permission_required = 'webapp.change_review'

    def has_permission(self, **kwargs):
        review = get_object_or_404(Review, pk=self.kwargs.get('pk'), )
        return super().has_permission() or review.author == self.request.user

    def get_success_url(self):
        review = Review.objects.get(pk=self.object.pk)
        return reverse('product_view', kwargs={'pk': review.product.pk})


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    model = Review
    template_name = 'review/review_delete.html'
    context_object_name = 'review'
    permission_required = 'webapp.delete_review'

    def has_permission(self, **kwargs):
        review = get_object_or_404(Review, pk=self.kwargs.get('pk'), )
        return super().has_permission() or review.author == self.request.user

    def get_success_url(self):
        review = Review.objects.get(pk=self.object.pk)
        return reverse('product_view', kwargs={'pk': review.product.pk})


