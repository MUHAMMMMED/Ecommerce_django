
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'admin'
        CUSTOMER = "CUSTOMER", "customer"
        MANAGER = "MANAGER", "manager"



    role = models.CharField(max_length=50, help_text='This is role user in system', choices=Role.choices)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    set_role = Role.ADMIN

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def is_admin(self):
        return self.role == self.Role.ADMIN

    def is_manager(self):
        return self.role == self.Role.MANAGER

    def is_customer(self):
        return self.role == self.Role.CUSTOMER



    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.role == User.Role.ADMIN:
                self.role = self.set_role
            return super().save(*args, **kwargs)
        return super().save(*args, **kwargs)







class managerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="MANAGER")


class Manager(User):
    set_role = User.Role.MANAGER
    REQUIRED_FIELDS = ['username']
    companies = managerManager()

    class Meta:
        proxy = True



class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="CUSTOMER")


class Customer(User):
    set_role = User.Role.CUSTOMER
    customer = CustomerManager()

    class Meta:
        proxy = True
