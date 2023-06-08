"""
Database models.
"""
# from django.conf import settings

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


# Create your models here.

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""

        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'


class RentalListing(models.Model):
    """Individual rental listing"""

    bathrooms = models.IntegerField()
    bedrooms = models.IntegerField()
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    currency = models.CharField(max_length=10)
    days_on_zillow = models.IntegerField()
    home_status = models.CharField(max_length=200)
    home_status_for_HDP = models.CharField(max_length=200)
    home_type = models.CharField(max_length=200)
    img_src = models.URLField()
    is_featured = models.BooleanField()
    is_non_owner_occupied = models.BooleanField()
    is_preforeclosure_auction = models.BooleanField()
    is_premier_builder = models.BooleanField()
    is_rental_with_base_price = models.BooleanField()
    is_showcase_listing = models.BooleanField()
    is_unmappable = models.BooleanField()
    is_zillow_owned = models.BooleanField()
    latitude = models.FloatField()
    listing_sub_type = models.CharField(max_length=200, blank=True, null=True)
    living_area = models.IntegerField()
    longitude = models.FloatField()
    price = models.IntegerField()
    price_for_HDP = models.IntegerField()
    rent_zestimate = models.IntegerField()
    should_highlight = models.BooleanField()
    state = models.CharField(max_length=50)
    street_address = models.CharField(max_length=200)
    unit = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=10)
    zpid = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
