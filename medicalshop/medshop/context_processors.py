from .models import Category, Branch, Product, Area


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)


def product_links(request):
    plinks = Product.objects.all()
    return dict(plinks=plinks)


def branch_links(request):
    blinks = Branch.objects.all()
    return dict(blinks=blinks)


def area_links(request):
    alinks = Area.objects.all()
    return dict(alinks=alinks)
