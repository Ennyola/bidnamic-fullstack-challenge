from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth.models import User
from formapp.views import delete_application
# Create your tests here.

class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        # self.user = User.objects.create_user(email="jondoe@mail.com",username="johndoe",password="johndoe")
        
    def test_login_view_GET(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

    def test_login_view_POST(self):
        response = self.client.post(reverse("accounts:login"),{
            "username":"johndoe",
            "password":"johndoe"
        })
        self.assertEqual(response.status_code, 302)
    def test_login_view_POST_unsuccesful(self):
        response = self.client.post(reverse("accounts:login"),{
            "username":"johndoe",
            "password":"johndow"
        })
        self.assertEqual(response.status_code, 302)
        
    def test_signup_GET(self):
        response = self.client.get(reverse("accounts:signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/signup.html")
    
    def test_signup_POST(self):
        response = self.client.post(reverse("accounts:signup"),{
            "username":"johndoe",
            "password":"johndoe",
            "rt_password":"johndoe"
        })
        print(User.objects.all())
        self.assertEqual(response.status_code, 302)

        
    