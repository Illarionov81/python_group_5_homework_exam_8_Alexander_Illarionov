from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, ReviewForm
from webapp.models import Product, Review


# PermissionRequiredMixin,
class ReviewCreateView(CreateView):
    model = Review
    template_name = 'review/review_add.html'
    form_class = ReviewForm
    # permission_required = 'webapp.add_issuetracker'

    # def has_permission(self, **kwargs):
    #     project = get_object_or_404(Project, pk=self.kwargs.get('pk'),)
    #     try:
    #         user = project.users.get(pk=self.request.user.pk)
    #     except ObjectDoesNotExist:
    #         user = False
    #     return super().has_permission() and user

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'),)
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('product_view', pk=product.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, pk=self.kwargs.get('pk'),)
        return context


# PermissionRequiredMixin,
class ReviewUpdateView(UpdateView):
    template_name = 'review/review_change.html'
    form_class = ReviewForm
    model = Review
    context_object_name = 'review'
    # permission_required = 'webapp.change_issuetracker'

    # def has_permission(self, **kwargs):
    #     task = get_object_or_404(IssueTracker, pk=self.kwargs.get('pk'),)
    #     project = task.project
    #     try:
    #         user = project.users.get(pk=self.request.user.pk)
    #     except ObjectDoesNotExist:
    #         user = False
    #     return super().has_permission() and user

    def get_success_url(self):
        review = Review.objects.get(pk=self.object.pk)
        return reverse('product_view', kwargs={'pk': review.product.pk})


# PermissionRequiredMixin,
class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/review_delete.html'
    context_object_name = 'review'
    # permission_required = 'webapp.delete_issuetracker'

    def get_success_url(self):
        return reverse("product_view", kwargs={'pk': self.object.product.pk})
