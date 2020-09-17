from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User

from .models import Post

class BlogTests(TestCase):


    @classmethod
    def setUpTestData(cls):
        #Create user
        testuser1 = User.objects.create_user(username="testuser1",password="abc123")
        testuser1.save()


        #create a blog post

        test_post = Post.objects.create(author=testuser1,
                                        title='Blog title',
                                        body='Body content.....'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author,'testuser1')
        self.assertEqual(title,'Blog title')
        self.assertEqual(body,'Body content.....')

    def test_created_at(self):
        post = Post.objects.get(id=1)
        created_at = f'{post.created_at}'
        updated_at = f'{post.updated_at}'
        print(created_at)
        print(updated_at)
        self.assertNotEqual(created_at,updated_at)