from django.db import models

# Create your models here.


class Customer(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email_address = models.EmailField()
    joined_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Brand(models.Model):

    name = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class SubBrand(models.Model):

    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class Category(models.Model):

    name = models.CharField(max_length=25)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class SubCategory(models.Model):

    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class Product(models.Model):
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'UniSex')
    )
    name = models.CharField(max_length = 50)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT)  
    sub_brand = models.ForeignKey(SubBrand,on_delete=models.SET_NULL,blank=True, null=True)  
    cost_price = models.FloatField()
    marked_price = models.FloatField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)

    def __str__(self):
        return 

    def __unicode__(self):
        return 


class ProductPiece(models.Model):

    color = models.