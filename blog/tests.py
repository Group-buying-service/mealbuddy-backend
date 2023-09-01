from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post

class ParticipantsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_join_action(self):
        post = Post.objects.create(title='Test Post', content='Test content', writer=self.user, target_number=3)
        initial_join_number = post.join_number

        response = self.client.post(f'/api/participants/{post.pk}/', {'action': 'join'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['join_number'], initial_join_number + 1)

    def test_cancel_action(self):
        post = Post.objects.create(title='Test Post', content='Test content', writer=self.user, target_number=3)
        post.recruited_users.add(self.user)
        initial_join_number = post.join_number

        response = self.client.post(f'/api/participants/{post.pk}/', {'action': 'cancel'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['join_number'], initial_join_number - 1)

    def test_invalid_action(self):
        post = Post.objects.create(title='Test Post', content='Test content', writer=self.user, target_number=3)

        response = self.client.post(f'/api/participants/{post.pk}/', {'action': 'invalid'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_join_over_target(self):
        post = Post.objects.create(title='Test Post', content='Test content', writer=self.user, target_number=0)

        response = self.client.post(f'/api/participants/{post.pk}/', {'action': 'join'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_join_twice(self):
        post = Post.objects.create(title='Test Post', content='Test content', writer=self.user, target_number=3)
        post.recruited_users.add(self.user)

        response = self.client.post(f'/api/participants/{post.pk}/', {'action': 'join'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_cancel_unjoined(self):
        post = Post.objects.create(title='Test Post', content='Test content', writer=self.user, target_number=3)

        response = self.client.post(f'/api/participants/{post.pk}/', {'action': 'cancel'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)