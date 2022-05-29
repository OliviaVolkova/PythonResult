from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from urls.models import User, UrlModel
from urls.utils import get_random_string


class Tests(TestCase):

    def setUp(self):
        username = 'login'
        password = "password"
        User.objects.create_user(username=username, password=password)

    def test_sign_in_available(self):
        response = self.client.get('/sign_in/')
        self.assertEqual(response.status_code, 200)

    def test_sign_up_available(self):
        response = self.client.get('/sign_up/')
        self.assertEqual(response.status_code, 200)

    def test_sign_in_unavailable(self):
        username = 'login'
        password = "password"
        self.client.login(username=username, password=password)
        response = self.client.get('/sign_in/')
        self.assertEqual(response.status_code, 302)

    def test_sign_up_unavailable(self):
        username = 'login'
        password = "password"
        self.client.login(username=username, password=password)
        response = self.client.get('/sign_up/')
        self.assertEqual(response.status_code, 302)

    def test_urls_unavailable(self):
        response = self.client.get('/all_urls/')
        self.assertEqual(response.status_code, 302)

    def test_login_template(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_sign_up_template(self):
        response = self.client.get('/sign_up/')
        self.assertTemplateUsed(response, 'sign_up.html')

    def test_base_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')

    def test_urls_template(self):
        username = 'login'
        password = "password"
        self.client.login(username=username, password=password)
        response = self.client.get('/all_urls/')
        self.assertTemplateUsed(response, 'all_urls.html')

    def test_redirect(self):
        user = User.objects.get(id=1)

        url = 'https://www.google.com/'
        UrlModel.objects.create(url=url, user=user, new_url=get_random_string(6))
        response = self.client.get('/' + UrlModel.objects.get(id=1).new_url)
        self.assertURLEqual(response.url, url)

    def test_urls_available(self):
        username = 'login'
        password = "password"
        self.client.login(username=username, password=password)
        response = self.client.get('/all_urls/')
        self.assertEqual(response.status_code, 200)

    def test_add_url(self):
        username = 'login'
        password = "password"
        self.client.login(username=username, password=password)
        self.client.post('/add/', {'url': 'https://www.google.com/'})
        self.assertTrue(UrlModel.objects.count() == 1)

    def test_sign_in_success(self):
        username = 'login'
        password = "password"
        self.client.login(username=username, password=password)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_sign_in(self):
        username = 'login'
        password = "wrong_password"
        self.client.login(username=username, password=password)
        response = self.client.get('/all_urls/')
        self.assertEqual(response.status_code, 302)

