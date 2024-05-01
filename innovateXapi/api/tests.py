from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class TranslateViewTests(APITestCase):
    def test_translation_success(self):
        """
        Test successful POST request to the translation API.
        """
        url = reverse('translate')  # Make sure this is the correct name for your URL configuration
        data = {"message": "Hello, world!"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('reply', response.data)  # Checks if 'reply' key is in the response

    def test_translation_failure(self):
        """
        Test POST request with invalid data to ensure it returns a 400 status.
        """
        url = reverse('translate')
        data = {"msg": "Hello, world!"}  # Incorrect key to trigger serialization failure
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('message' in response.data)  # Check if the correct error is being returned


class ParaphraseViewTests(APITestCase):
    def test_paraphrase_success(self):
        """
        Test successful POST request to the paraphrase API.
        """
        url = reverse('paraphrase')  # Make sure this is the correct name for your URL configuration
        data = {"message": "Hello, world!"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('reply', response.data)  # Checks if 'reply' key is in the response

    def test_paraphrase_failure(self):
        """
        Test POST request with invalid data to ensure it returns a 400 status.
        """
        url = reverse('paraphrase')
        data = {"msg": "Hello, world!"}  # Incorrect key to trigger serialization failure
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('message' in response.data)  # Check if the correct error is being returned