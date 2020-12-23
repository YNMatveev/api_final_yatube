from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Comment, Post

User = get_user_model()

USERNAME = 'Tester'
PASSWORD = 'Secretword'


class ApiURLTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username=USERNAME,
                                            password=PASSWORD)
        cls.token = RefreshToken.for_user(cls.user).access_token
        cls.user_auth = 'Authorization: Bearer ' + str(cls.token)
        cls.test_post = Post.objects.create(text='Тестовый пост',
                                            author=cls.user)
        cls.test_comment = Comment.objects.create(text='Тестовый коммент',
                                                  author=cls.user,
                                                  post=cls.test_post)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=self.user_auth)

    def test_auth_url(self):
        self.client.credentials()
        data = {"username": USERNAME, "password": PASSWORD}
        response = self.client.post(reverse('token_obtain_pair'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_list_url(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_detail_url(self):
        url = reverse('post-detail', kwargs={'pk': self.test_post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_list_url(self):
        url = reverse('comment-list', kwargs={'post_id': self.test_post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_detail_url(self):
        url = reverse('comment-detail', kwargs={'post_id': self.test_post.id,
                                                'pk': self.test_comment.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_follow_list_url(self):
        url = reverse('follow-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_group_list_url(self):
        url = reverse('group-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
