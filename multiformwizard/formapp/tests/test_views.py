from datetime import datetime
from email.mime import application
import json
from django.test import TestCase,Client
from django.urls import reverse

from formapp.views import delete_application
from ..models import UserApplication
# Create your tests here.

class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
    
    def test_application_GET(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "formapp/customerSubmitForm.html")
        
    def test_application_POST(self):
        response = self.client.post(reverse("index"),{
            "title":"Another application",
            "first_name":"John",
            "surname":"Doe", 
            "d_o_b":datetime.today().date(), 
            "company_name":"Bidnami", 
            "address":"London", 
            "telephone":"+123456789",
            "bidding_settings":"HIGH", 
            "google_id":12345678
        })
        application = UserApplication.objects.all().first()
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(application.title, "Another application")
        
    def test_list_all_applications(self):
        response = self.client.get(reverse("applications"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "formapp/showapplications.html")
        
    def test_delete_application(self):
        application= UserApplication.objects.create(title="A new application",first_name="John",surname="Doe", d_o_b=datetime.today().date(), company_name="Bidnami", address="London", telephone="+123456789",bidding_settings="HIGH", google_id=12345678)
        response = self.client.delete(reverse("delete-application", args=['1']), json.dumps({
            'id':1
        }))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(UserApplication.objects.count(),0)