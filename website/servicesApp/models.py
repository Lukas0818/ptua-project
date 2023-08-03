from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    RENT = 'rent'
    SALE = 'sale'
    
    TYPE_CHOICES = [
        (RENT, 'Rent'),
        (SALE, 'Sale'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default=SALE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class UserRentService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name
    

class ReturnRequest(models.Model):
    rented_service = models.OneToOneField(UserRentService, on_delete=models.CASCADE)
    approved = models.BooleanField(null=True)

    def __str__(self):
        return f"Return request for {self.rented_service.service.name}"
