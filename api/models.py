from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    group = models.ForeignKey('api.Group', on_delete=models.SET_NULL,
                              blank=True, null=True, related_name='posts')

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления", auto_now_add=True,
                                   db_index=True)


class Group(models.Model):
    title = models.TextField(max_length=50, unique=True)

    def str(self):
        return self.title


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['following', 'user'],
                                    name='unique_follow'),
            models.CheckConstraint(check=~models.Q(following=models.F('user')),
                                   name='following_user_not_equal')
        ]
