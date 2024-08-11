from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'HomePage2.html', {})


def products_page(request):
    return render(request, "products_page.html")


def about_us(request):
    return render(request, "about_us.html")
