from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from educational_modules.models import Lessons


class LessonsTestCase(APITestCase):

    def setUp(self) -> None:
        self.lessons = Lessons.objects.create(
            title="TEST",
            description="TEST2"
        )

    def test_create_education(self):
        """ Test Create """
        data = {
            "title": "test",
            "description": "test"
        }
        response = self.client.post(
            '/create/',
            data=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_education(self):
        """ Test List"""

        response = self.client.get(
            ''
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_education(self):
        """ Test Update """

        data = {
            "title": "Update test lesson",
            "description": "Update test lesson 2"
        }
        response = self.client.put(
            reverse('educational_modules:lesson-update', kwargs={'pk': self.lessons.id}),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_education(self):
        """ Test Delete """

        response = self.client.delete(
            reverse('educational_modules:lesson-delete', kwargs={'pk': self.lessons.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_education(self):
        """ Test retrieve """

        response = self.client.get(
            reverse('educational_modules:lesson-retrieve', kwargs={'pk': self.lessons.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
