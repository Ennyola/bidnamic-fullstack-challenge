from datetime import datetime
import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import FormApplication

# Create your tests here.


class TestViews(TestCase):
    """Test for views.py in form_app"""

    def setUp(self):
        """SetUp code for all tests"""
        self.client = Client()
        self.user = User.objects.create_user(
            email="jondoe@mail.com", username="johndoe", password="johndoe"
        )
        self.client_login = self.client.login(username="johndoe", password="johndoe")

    def test_index_form_application_get(self):
        """Tests if the  index form view renders the correct html template"""
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "form_app/customerSubmitForm.html")

    def test_index_form_application_post(self):
        """Tests if the view successfully creates an application"""
        response = self.client.post(
            reverse("index"),
            {
                "title": "Another application",
                "first_name": "John",
                "surname": "Doe",
                "d_o_b": datetime.today().date(),
                "company_name": "Bidnami",
                "address": "London",
                "telephone": "+123456789",
                "bidding_settings": "HIGH",
                "google_id": 12345678,
            },
        )
        application = FormApplication.objects.all().first()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(application.title, "Another application")

    def test_form_application_google_id_exists_post(self):
        """Tests if google ID exists already before an application is created"""
        FormApplication.objects.create(
            title="New Company Reveal",
            first_name="Joshua",
            surname="Stalling",
            d_o_b=datetime.today().date(),
            company_name="Google",
            address="34, Kingsway, Uk",
            telephone="+123456789",
            bidding_settings="HIGH",
            google_id=87654321,
        )
        response = self.client.post(
            reverse("index"),
            {
                "title": "Another application",
                "first_name": "John",
                "surname": "Doe",
                "d_o_b": datetime.today().date(),
                "company_name": "Bidnami",
                "address": "London",
                "telephone": "+123456789",
                "bidding_settings": "HIGH",
                "google_id": 87654321,
            },
        )

        self.assertEqual(response.status_code, 200)

    def test_list_applications(self):
        """Tests if the show_applications view renders the correct template"""
        response = self.client.get(reverse("applications"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "form_app/showApplications.html")

    def test_delete_application(self):
        """Tests if an application can be deleted successfully"""
        FormApplication.objects.create(
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
        response = self.client.delete(
            reverse("delete_application", args=["1"]), json.dumps({"id": 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(FormApplication.objects.count(), 0)
