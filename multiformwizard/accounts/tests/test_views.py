from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.


class TestViews(TestCase):
    """Test for views.py in accounts app"""

    def setUp(self):
        """SetUp code for all tests"""
        self.client = Client()
        self.user = User.objects.create_user(
            email="jondoe@mail.com", username="johndoe", password="johndoe"
        )

    def test_login_view_get(self):
        """Tests if the login view renders the correct html template"""
        response = self.client.get(reverse("accounts:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

    def test_login_view_post_successful(self):
        """Tests if the login view correctly logs in the user"""
        response = self.client.post(
            reverse("accounts:login"),
            {"username": "johndoe", "password": "johndoe", "next": ""},
        )
        self.assertEqual(response.status_code, 302)

    def test_login_view_post_unsuccessful(self):
        """Tests if the login view is supplied incorrect details"""
        response = self.client.post(
            reverse("accounts:login"),
            {"username": "johndoe", "password": "johndow", "next": ""},
        )
        self.assertEqual(response.status_code, 200)

    def test_login_view_post_redirect_next_is_true(self):
        """Tests if the login view is suplied a redirect_next url"""
        response = self.client.post(
            reverse("accounts:login"),
            {"username": "johndoe", "password": "johndoe", "next": "/applications/"},
        )
        self.assertEqual(response.status_code, 302)

    def test_signup_get(self):
        """Tests if the signup view renders the correct template"""
        response = self.client.get(reverse("accounts:signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/signup.html")

    def test_signup_post(self):
        """Tests if the signup successfully creates a user"""
        response = self.client.post(
            reverse("accounts:signup"),
            {"username": "danmac", "password": "danmac", "rtpassword": "danmac"},
        )
        self.assertEqual(response.status_code, 302)

    def test_signup_post_user_already_exists(self):
        """Tests if the user already exists before signup"""
        response = self.client.post(
            reverse("accounts:signup"),
            {"username": "johndoe", "password": "johndoe", "rtpassword": "johndoe"},
        )
        self.assertEqual(response.status_code, 200)

    def test_signup_post_password_mismatch(self):
        """Tests if User passwords do not match"""
        response = self.client.post(
            reverse("accounts:signup"),
            {"username": "danmac", "password": "danmac", "rtpassword": "danma"},
        )
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """Tests if User logs out successfully"""
        response = self.client.get(reverse("accounts:logout"))
        self.assertEqual(response.status_code, 302)
        