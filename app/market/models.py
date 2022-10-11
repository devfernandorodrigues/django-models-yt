from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    manufactured_at = models.DateField()
    expires_at = models.DateField()
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    @property
    def in_stock(self):
        return self.quantity > 0

    def increase_quantity(self):
        self.quantity += 1
        self.save()

    def decrease_quantity(self):
        self.quantity -= 1
        self.save()

    def __str__(self):
        return self.name
