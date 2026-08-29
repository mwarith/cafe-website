from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    points_balance = models.IntegerField(default=0)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    visits_count = models.IntegerField(default=0)
    referral_code = models.CharField(max_length=10, unique=True, blank=True, null=True)

    @property
    def customer_segment(self):
        if self.total_spent > 5000:
            return "VIP"
        elif self.visits_count > 10:
            return "Regular"
        return "New"