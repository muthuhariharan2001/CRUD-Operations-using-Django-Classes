# views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    template_name = 'products/product_confirm_delete.html'