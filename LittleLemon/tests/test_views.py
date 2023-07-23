from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User(
            username='testuser', email='testuser@test.com', password='testpassword'
        )
        self.menus = [
            {   
                'id': 2,
                'title': 'Apple',
                'price': '15.00',
                'inventory': 30
            },
            {
                'id': 3,
                'title': 'Banana',
                'price': '20.00',
                'inventory': 40
            }
        ]
        for menu in self.menus:
            Menu.objects.create(**menu)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        menus = sorted(response.data, key=lambda x: x['id'])
        menus = [dict(menu) for menu in menus]
        self.assertEqual(menus, self.menus)

