"""
Test custom Django management commands.
"""
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2OpError
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase
from django.test import TestCase

from core.models import RentalListing
from core.management.commands import fetch_and_store_data


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready."""

        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError."""

        patched_check.side_effect = [Psycopg2OpError] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)

        patched_check.assert_called_with(databases=['default'])


class FetchAndStoreDataTest(TestCase):
    def setUp(self):
        self.mock_response = {
            "results": [
                {
                    "zpid": "1234",
                    "bathrooms": 2,
                    "bedrooms": 3,
                    "city": "Boston",
                    "country": "USA",
                    "currency": "USD",
                    "days_on_zillow": 10,
                    "home_status": "for rent",
                    "home_status_for_HDP": "for rent",
                    "home_type": "apartment",
                    "img_src": "https://example.com/image.jpg",
                    "is_featured": False,
                    "is_non_owner_occupied": False,
                    "is_preforeclosure_auction": False,
                    "is_premier_builder": False,
                    "is_rental_with_base_price": True,
                    "is_showcase_listing": False,
                    "is_unmappable": False,
                    "is_zillow_owned": False,
                    "latitude": 42.3601,
                    "listing_sub_type": "condo",
                    "living_area": 1000,
                    "longitude": -71.0589,
                    "price": 2000,
                    "price_for_HDP": 2000,
                    "rent_zestimate": 1900,
                    "should_highlight": False,
                    "state": "MA",
                    "street_address": "123 Main St",
                    "unit": "1",
                    "zipcode": "02134",
                }
            ]
        }

    @patch("http.client.HTTPSConnection")
    def test_fetch_and_store_data(self, mock_conn):
        mock_conn.return_value.getresponse.return_value.read.return_value = json.dumps(self.mock_response).encode("utf-8")

        call_command("fetch_and_store_data")

        listing = RentalListing.objects.first()
        self.assertEqual(listing.zpid, "1234")
        self.assertEqual(listing.bathrooms, 2)
        self.assertEqual(listing.bedrooms, 3)
        self.assertEqual(listing.city, "Boston")
        self.assertEqual(listing.country, "USA")
        self.assertEqual(listing.currency, "USD")
        self.assertEqual(listing.days_on_zillow, 10)
        self.assertEqual(listing.home_status, "for rent")
        self.assertEqual(listing.home_status_for_HDP, "for rent")
        self.assertEqual(listing.home_type, "apartment")
        self.assertEqual(listing.img_src, "https://example.com/image.jpg")
        self.assertEqual(listing.is_featured, False)
        self.assertEqual(listing.is_non_owner_occupied, False)
        self.assertEqual(listing.is_preforeclosure_auction, False)
        self.assertEqual(listing.is_premier_builder, False)
        self.assertEqual(listing.is_rental_with_base_price, True)
        self.assertEqual(listing.is_showcase_listing, False)
        self.assertEqual(listing.is_unmappable, False)
        self.assertEqual(listing.is_zillow_owned, False)
        self.assertEqual(listing.latitude, 42.3601)
        self.assertEqual(listing.listing_sub_type, "condo")
        self.assertEqual(listing.living_area, 1000)
        self.assertEqual(listing.longitude, -71.0589)
        self.assertEqual(listing.price, 2000)
        self.assertEqual(listing.price_for_HDP, 2000)
        self.assertEqual(listing.rent_zestimate, 1900)
        self.assertEqual(listing.should_highlight, False)
        self.assertEqual(listing.state, "MA")
        self.assertEqual(listing.street_address, "123 Main St")
        self.assertEqual(listing.unit, "1")
        self.assertEqual(listing.zipcode, "02134")
