from django.shortcuts import render
from .models import Product, Category


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')


def product_list(request):
    query = request.GET.get('q')
    category_filter = request.GET.get('category')
    sort_by = request.GET.get('sort')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category_filter:
        products = products.filter(category_id=category_filter)

    if sort_by:
        products = products.order_by(sort_by)

    categories = Category.objects.all()  # Retrieve all categories for the dropdown

    return render(request, 'pages/products_list.html', {'products': products, 'categories': categories})
