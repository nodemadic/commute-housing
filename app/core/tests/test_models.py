"""
Tests for models.
"""
# from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core.models import RentalListing


class ModelTests(TestCase):
    """Test User model."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')


class RentalListingModelTest(TestCase):
    """Test RentalListing model."""

    def setUp(self):
        RentalListing.objects.create(
            bathrooms=2,
            bedrooms=3,
            city="Allston",
            country="USA",
            currency="USD",
            days_on_zillow=0,
            home_status="FOR_RENT",
            home_status_for_HDP="FOR_RENT",
            home_type="APARTMENT",
            img_src="https://photos.zillowstatic.com/fp/eb5dbd9e055380301ec348f81f3f80a6-p_e.jpg",
            is_featured=True,
            is_non_owner_occupied=True,
            is_preforeclosure_auction=False,
            is_premier_builder=False,
            is_rental_with_base_price=False,
            is_showcase_listing=False,
            is_unmappable=False,
            is_zillow_owned=False,
            latitude=42.359856,
            listing_sub_type=None,
            living_area=1400,
            longitude=-71.13455,
            price=5000,
            price_for_HDP=5000,
            rent_zestimate=4999,
            should_highlight=False,
            state="MA",
            street_address="54-56 Athol St #1",
            unit="# 1",
            zipcode="02134",
            zpid=2057509307
        )

    def test_rental_listing_created(self):
        """Rental listings are saved correctly"""
        listing = RentalListing.objects.get(zpid=2057509307)
        self.assertEqual(listing.city, 'Allston')
