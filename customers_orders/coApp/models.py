from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Order(models.Model):
    product = models.CharField(max_length=255)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)