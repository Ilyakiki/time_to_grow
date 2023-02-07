from django.shortcuts import render
from .models import Product
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView
from itertools import chain
from django.utils.text import slugify
from cart.forms import CartAddProductForm
# Create your views here.

def where_buy(request):
    return render(request,'shop/where_you_can_buy.html')

def contacts(request):
    return render(request,'shop/contacts.html')
def homepage(request):
    return render(request,'shop/homepage.html')
def about_us(request):
    return render(request,'shop/about_us.html')
def FAQ(request):
    return render(request,'shop/FAQ.html')
class ListProducts(ListView):
    '''Список Товаров'''
    paginate_by = 10  # Пагинация
    template_name = 'shop/list_products.html'
    model = Product
    context_object_name = 'Products'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(available=True)
        return queryset

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ListProducts, self).get_context_data(**kwargs)
        context['form'] = CartAddProductForm
        return context


'''def show_all_products(request):
    products=Product.objects.all()
    products=products.filter(available=True)
    for product in products:
        product.save()
    return render(request,'shop/list_products.html',{'products':products})'''



class DetailProduct(DetailView):
    '''Детальное представление продукта'''
    template_name = 'shop/detail_product.html'
    model = Product
    def get_context_data(self,*args, **kwargs):
        '''self.object.structure= self.object.structure.split('\r\n')
        self.object.description_text=self.object.description_text.split('\r\n')
        self.object.method_of_application = self.object.method_of_application.split('\r\n')''' """дописать"""
        context = super(DetailProduct, self).get_context_data(**kwargs)
        context['object'].structure = context['object'].structure.split('\r\n')
        context['object'].description_text=context['object'].description_text.split('\r\n')
        context['object'].method_of_application = context['object'].method_of_application.split('\r\n')
        context['form'] = CartAddProductForm
        return context



class Search(ListView):
    template_name = 'shop/list_products.html'
    model = Product


    def get_queryset(self):
        queryset = super().get_queryset()
        p = self.request.GET.get('q').lower()  # Для того,чтобы в поисковой строке можно было вводить название в любом регистре
        my_obj_list = []

        for product in queryset:
            if p in product.name.lower():
                my_obj_list.append(product)

        none_qs = Product.objects.none()
        qs = list(chain(none_qs, my_obj_list))

        #filtered_qs = queryset.filter(name__icontains=p)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f'{self.request.GET.get("q")}&'
        return context