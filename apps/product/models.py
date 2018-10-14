from django.db import models

# Create your models here.
class Product(models.Model):
    TAX_CODE = (
        ('1', 'food'),
        ('2', 'tobacco'),
        ('3', 'entertainment')
    )

    name = models.CharField(max_length=100)
    tax_code = models.CharField(max_length=20, choices=TAX_CODE, default='1')
    price = models.PositiveIntegerField(default=0)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def type(self):
        if self.tax_code == '1':
            return 'Food & Beverage'
        elif self.tax_code == '2':
            return 'Tobacco'
        elif self.tax_code == '3':
            return 'Entertainment'
        else:
            return 'Unknown'
    
    def tax(self):
        if self.tax_code == '1':
            return (10/100) * self.price
        elif self.tax_code == '2':
            return ((2/100) * self.price) + 10
        elif self.tax_code == '3':
            if self.price < 100:
                return 0
            else:
                return (self.price - 100) * (1/100)
        else:
            return 0

    def refund(self):
        if self.tax_code == '1':
            return True
        elif self.tax_code == '2':
            return False
        elif self.tax_code == '3':
            return False

    def amount(self):
        return self.price + self.tax()
