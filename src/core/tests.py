from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class HomeNotAuthenticatedTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('home'), follow=True)

    def test_redirect_status_code(self):
        redirect = self.client.get(reverse('home'))
        self.assertEqual(redirect.status_code, 302)

    def test_redirect_chain(self):
        self.assertEqual(len(self.response.redirect_chain), 1)
        self.assertEqual(self.response.redirect_chain,
                         [('http://testserver/login?next=/', 302)])

    def test_final_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_final_template_used(self):
        self.assertTemplateUsed(self.response, 'core/login.html')


class HomeAuthenticatedTestCase(TestCase):

    def setUp(self):
        User.objects.create_user('alanturing', 'alan@turi.ng', '4l4n7uR1ng')
        self.client.login(username='alanturing', password='4l4n7uR1ng')
        self.response = self.client.get(reverse('home'))

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/home.html')


class LoginTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('login'))

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/login.html')


class LogoutTestCase(TestCase):

    def setUp(self):
        User.objects.create_user('alanturing', 'alan@turi.ng', '4l4n7uR1ng')
        self.client.login(username='alanturing', password='4l4n7uR1ng')
        self.response = self.client.get(reverse('logout'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_redirect_chain(self):
        self.assertEqual(len(self.response.redirect_chain), 2)
        self.assertEqual(self.response.redirect_chain,
                         [('http://testserver/', 302),
                          ('http://testserver/login?next=/', 302)])
