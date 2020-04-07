from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm
from shop.forms import CustomerQuestionForm


def product_list(request, category_slug=None):
    template = 'shop/product/list.html'
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    page = request.GET.get('page')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        paginator = Paginator(products, 9)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    else:
        paginator = Paginator(products, 9)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    return render(request, template,
                  {'category': category, 'categories': categories, 'products': products, 'page': page})


def product_detail(request, id, slug):
    cart_product_form = CartAddProductForm()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})


# Other pages
def test(request):
    return render(request, 'test.html')


def terms(request):
    return render(request, 'shop/other/terms_of_use.html')


# def contacts(request):
#     return render(request, 'shop/other/contact.html')

def contacts(request):
    form = CustomerQuestionForm(request)
    if request.method == 'POST':
        form = CustomerQuestionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'shop/other/contact_done.html')
    else:
        form = CustomerQuestionForm()
    return render(request, 'shop/other/contact.html', {'form': form})
