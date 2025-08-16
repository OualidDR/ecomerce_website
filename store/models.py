from django.db import models
import datetime


#categuries of Products
class Category(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta :
        verbose_name_plural = 'Categories'




#Customers
class Customer(models.Model) :
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50)
    email        = models.EmailField(max_length=254)
    phone        = models.CharField(max_length=50)
    password     = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'





#all of oure products
class Product(models.Model) :
    product_name        = models.CharField(max_length=50)
    product_price       = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    product_description = models.CharField(max_length=50, default='', blank=True, null=True)
    product_catgory     = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    product_image       = models.ImageField(upload_to='uploads/product/')
    #add sel stuff
    is_sale             = models.BooleanField(default=False)
    sell_price          = models.DecimalField(max_digits=10, decimal_places=4, default=0)

    def __str__(self):
        return self.product_name





#customer orders
class Order(models.Model) :
    product     = models.ForeignKey(Product, on_delete=models.CASCADE, )
    customer    = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=1)
    address     = models.CharField(max_length=100,default='', blank=True)
    phone       = models.CharField(max_length=50,default='', blank=True)
    date        = models.DateField(default=datetime.date.today)
    status      = models.BooleanField(default=False)

    def __str__(self):
        return self.product









