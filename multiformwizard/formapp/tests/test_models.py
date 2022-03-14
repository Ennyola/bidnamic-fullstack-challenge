from datetime import datetime
from django.test import TestCase
from ..models import UserApplication
# Create your tests here.

class Testmodel(TestCase):
    def test_title_returned(self):
        application= UserApplication.objects.create(title="A new application",first_name="John",surname="Doe", d_o_b=datetime.today().date(), company_name="Bidnami", address="London", telephone="+123456789",bidding_settings="HIGH", google_id=12345678)
        self.assertEqual(application.title, str(application))