from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_ROLES = (
        ('CLIENT', 'Cliente'),
        ('SELLER', 'Vendedor'),
    )

    role = models.CharField(
        max_length=10,
        choices=USER_ROLES
    )

    def is_seller(self):
        return self.role == 'SELLER'

    def is_client(self):
        return self.role == 'CLIENT'

class SellerProfile(models.Model):
    SELLER_TYPES = (
        ('AMBULANTE', 'Ambulante'),
        ('PUERTA', 'Puerta a puerta'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='seller_profile'
    )

    seller_type = models.CharField(
        max_length=20,
        choices=SELLER_TYPES
    )

    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'Perfil vendedor - {self.user.username}'
