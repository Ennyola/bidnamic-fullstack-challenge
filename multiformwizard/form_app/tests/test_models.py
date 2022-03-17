from datetime import datetime
from django.test import TestCase
from ..models import FormApplication

# Create your tests here.


class TestModels(TestCase):
    """Test for models.py in form_app"""

    def test_title_returned(self):
        """ "
        Tests if model title is returned whenever it is queried
        """
        application = FormApplication.objects.create(
            title="A new application",
            first_name="John",
            surname="Doe",
            d_o_b=datetime.today().date(),
            company_name="Bidnami",
            address="London",
            telephone="+123456789",
            bidding_settings="HIGH",
            google_id=12345678,
        )
        self.assertEqual(application.title, str(application))
