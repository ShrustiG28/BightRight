from django.db import models

from users.models import UserProfile


class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    split_details = models.TextField(blank=True)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.email}"
