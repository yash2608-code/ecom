from django.db import models

# Create your models here.
class Admin(models.Model):
    Email=models.EmailField(max_length=100,default="Email")
    passwd=models.CharField(max_length=100,default="Password")
    Role=models.CharField(max_length=100,default="Role")
    Fotp=models.BigIntegerField(default=123456)
    t_c=models.BooleanField(default=False)
    Is_Created=models.DateTimeField(auto_now_add=True)
    Is_Activated=models.BooleanField(default=True)

class User(models.Model):
    Admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=100,default="Firstname")
    Lastname=models.CharField(max_length=100,default="Lastname")
    Address=models.CharField(max_length=100,default="Address")
    phone=models.BigIntegerField(default=123456790)
    bdate=models.DateField(auto_now_add=True)
    Gender=models.CharField(max_length=100,default="Gender")

class Seller(models.Model):
    Admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=100,default="Seller Firstname")
    Lastname=models.CharField(max_length=100,default="Seller Lastname")
    Address=models.CharField(max_length=100,default="Seller Address")
    phone=models.BigIntegerField(default=123456790)
    bdate=models.DateField(auto_now_add=True)
    Gender=models.CharField(max_length=100,default="Seller Gender")

class Categories(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    Seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    cat = models.ForeignKey(Categories,on_delete=models.CASCADE)
    pimg1 = models.ImageField(upload_to="product_images/")
    pimg2 = models.ImageField(upload_to="product_images/")
    pimg3 = models.ImageField(upload_to="product_images/")
    pname = models.CharField(max_length=200)
    pdes = models.TextField()
    price = models.FloatField(default=0.00)