import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class MenuTestCase(APITestCase):
    
    def test_menu_create(self):
        data = {"name":"testcase","day":"2021-02-23","description":"testdescription"}    
        #url = reverse('menu:create')
        url = '/menu/create'
        response = self.client.post(url, data, "json")
        print (response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_menu_list(self):
        url = '/menu/list'
        response = self.client.get(url)
        print (response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
