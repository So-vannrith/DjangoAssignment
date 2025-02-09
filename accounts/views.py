from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return HttpResponse('Home_page')

def ViewValue(request):
    UnitPrice = 1500
    Quantity = 5
    TotalPrice = UnitPrice * Quantity
    Context = {
        'TP': TotalPrice,
        'Product' : 'Hi Product',
        'DP' : 'Hi Detail Product',
        'AUB' : 'hi Ice cream shop',
    }
    return render(request, 'accounts/Index.html', Context)

def ListCategory(request):
    category = Category.objects.all()
    context = {
        'categorys' :category,
    }
    return render(request, 'accounts/ListCategory.html', context)


def Index(request):
    Client = tblClients.objects.all()
    SocialMedia = tblSocialMedia.objects.all()
    Product = tblProducts.objects.all()
    category = Category.objects.all()
    topMenu = tblTopMenu.objects.all()
    topMenu2 = tblTopMenu2.objects.all()
    Services = Service.objects.all()
    
    
    context = {
        'Clients':Client,
        'SocialMedias':SocialMedia,
        'Products':Product,
        'Categories':category,
        'topMenus': topMenu,
        'topMenus2': topMenu2,
        'Services' : Services
       
    }
    return render(request, 'accounts/index.html', context)

def index(request):
    return HttpResponse(request, 'accounts/index.html')
 
def about(request):   
    
    topMenu = tblTopMenu.objects.all()
    topMenu2 = tblTopMenu2.objects.all()
    # Product = tblProducts.objects.all()
    context = {
        # 'Products':Product,
        'topMenus': topMenu,
        'topMenus2': topMenu2,
    }

    return render(request, 'accounts/about.html',context)

def gallery(request):   
    
    topMenu = tblTopMenu.objects.all()
    topMenu2 = tblTopMenu2.objects.all()
    gallery = tblGallery.objects.all()
    context = {
        'gallerys':gallery,
        'topMenus': topMenu,
        'topMenus2': topMenu2,
    }

    return render(request, 'accounts/about.html',context)
# def about(request):
#     return render(request, 'accounts/about.html')

def contact(request):
    topMenu = tblTopMenu.objects.all()
    topMenu2 = tblTopMenu2.objects.all()
    # Product = tblProducts.objects.all()
    context = {
        # 'Products':Product,
        'topMenus': topMenu,
        'topMenus2': topMenu2,
    }

    return render(request, 'accounts/contact.html', context)

def gallery(request):
    topMenu = tblTopMenu.objects.all()
    topMenu2 = tblTopMenu2.objects.all()
    gallery = tblGallery.objects.all()
    context = {
        'gallerys':gallery,
        'topMenus': topMenu,
        'topMenus2': topMenu2,

    }

    return render(request, 'accounts/gallery.html', context)

def product(request):
    topMenu = tblTopMenu.objects.all()
    topMenu2 = tblTopMenu2.objects.all()
    Product = tblProducts.objects.all()
    context = {
        'Products':Product,
        'topMenus': topMenu,
        'topMenus2': topMenu2,
    }

    return render(request, 'accounts/product.html', context)

def service(request):
    Services = Service.objects.all()
    topMenu = tblTopMenu.objects.all()
    topMenu2 = tblTopMenu2.objects.all()
    Client = tblClients.objects.all()
    context = {
        'Clients':Client,
        'topMenus': topMenu,
        'topMenus2': topMenu2,
        'Services' : Services
       
    }

    return render(request, 'accounts/service.html', context)