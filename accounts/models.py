from django.db import models
from ckeditor.fields import RichTextField # type: ignore
from ckeditor_uploader.fields import RichTextUploadingField # type: ignore
# Create your models here.
class Customer(models.Model):    
    name = models.CharField(max_length=200, null=True) 
    phone = models.CharField(max_length=200, null=True)    
    email = models.CharField(max_length=200, null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True) 
    def __str__ (self):         
        return self.name
    
class Category(models.Model):
    CategoryName = models.CharField(max_length=200, null=True)
    CategoryImage = models.ImageField(upload_to ='images/')
    Date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__ (self):         
        return self.CategoryName
class tblProducts(models.Model):
    productName = models.CharField(max_length=200, null=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    quantity = models.CharField(max_length=200, null=True)
    priceIn = models.CharField(max_length=200, null=True)
    priceOut = models.CharField(max_length=200, null=True)
    instock = models.CharField(max_length=200, null=True)
    productImage = models.ImageField(upload_to ='ProductImages/')
    productDate = models.DateTimeField(auto_now_add=True, null=True)

class tblGallery(models.Model):
    galleryName = models.CharField(max_length=200, null=True)
    galleryID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    quantity = models.CharField(max_length=200, null=True)
    priceIn = models.CharField(max_length=200, null=True)
    priceOut = models.CharField(max_length=200, null=True)
    instock = models.CharField(max_length=200, null=True)
    productImage = models.ImageField(upload_to ='ProductImages/')
    productDate = models.DateTimeField(auto_now_add=True, null=True)

class tblClients(models.Model):
    clientName = models.CharField(max_length=200, null=True)
    clientImage = models.ImageField(upload_to="pics")
    clientDescription = RichTextUploadingField(null=True)

    def __str__ (self):
        return f'{self.clientName}'
    
class tblSocialMedia(models.Model):
    socialMediaName = models.CharField(max_length=200, null=True)
    socialMediaURL = models.CharField(max_length=200, null=True)
    socialMediaImage = models.ImageField(upload_to="SocialMedia")

    def str (self):
        return self.socialMediaImage
    
class tblTopMenu(models.Model):
    topMenuName = models.CharField(max_length=200, null=True)
    topMenuImage = models.ImageField(upload_to="TopMenu")

    def __str__ (self):
        return self.topMenuName
class tblTopMenu2(models.Model):
    topMenuName = models.CharField(max_length=200, null=True)
    topMenuImage = models.ImageField(upload_to="TopMenu")

    def __str__ (self):
        return self.topMenuName


class tblSlides(models.Model):
    slideName = models.CharField(max_length=200, null=True)
    slideImage = models.ImageField(upload_to ='images/',null=True)
    slideDescription = RichTextUploadingField(null=True)
    active = models.CharField(max_length=20, null=True)

    def __str__ (self):
        return f'{self.slideName}'
class tblProductDetail(models.Model):
    productDetailName = models.CharField(max_length=200, null=True)
    productDetailDate = models.DateTimeField (auto_now_add=True, null=True)
    productID = models.ForeignKey(tblProducts, on_delete=models.CASCADE, null=True)
    productSize =  RichTextUploadingField(null=True)
    productColor = RichTextUploadingField(null=True)

class tblFooter(models.Model):
    footerName = models.CharField(max_length=200, null=True)

    def __str__ (self):
        return self.footerName
    
class tblSubFooter(models.Model):
    footerID = models.ForeignKey(tblFooter, on_delete=models.CASCADE, null=True)
    subFooterName = models.CharField(max_length=200, null=True)
    subFooterURL = models.CharField(max_length=200, null=True)

    
    def __str__ (self):
        return f'{self.footerID} {self.footerID.footerName}'
    
class About(models.Model):
    AboutName = models.CharField(max_length=200, null=True)
    AboutImage = models.ImageField(upload_to ='images/')
    Date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__ (self):         
        return self.AboutName
    
class Contact(models.Model):
    ContactName = models.CharField(max_length=200, null=True)
    ContactImage = models.ImageField(upload_to ='images/')
    Date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__ (self):         
        return self.ContactName
    
class Gallery(models.Model):
    GalleryName = models.CharField(max_length=200, null=True)
    GalleryImage = models.ImageField(upload_to ='images/')
    Date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__ (self):         
        return self.GalleryName
    
class Product(models.Model):
    ProductName = models.CharField(max_length=200, null=True)
    ProductPrice = models.CharField(max_length=200, null=True)
    ProductImage = models.ImageField(upload_to ='images/')
    Date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__ (self):         
        return self.ProductName
    
class Service(models.Model):
    ServiceName = models.CharField(max_length=200, null=True)
    ServiceImage = models.ImageField(upload_to ='images/')
    Date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__ (self):         
        return self.ServiceName