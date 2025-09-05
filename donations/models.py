from django.db import models

class Donation(models.Model):
    name = models.CharField(max_length=100)
    batch = models.CharField(max_length=50)
    mobile_bank = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=20)
    txn_id = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount} BDT"
