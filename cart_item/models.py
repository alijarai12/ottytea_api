from django.db import models
from django.contrib.auth import get_user_model
from product.models import Tea

User = get_user_model()


class Cartitem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE, blank=True, null=True, related_name='cartitems')
    quantity = models.PositiveIntegerField(default=0)

    