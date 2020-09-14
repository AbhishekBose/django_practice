from django.test import TestCase

# Create your tests here.
from .models import Todo


class TodoModelTest(TestCase):

    # @classmethod
    # def setUpTestData(self):
        # Todo.objects.create(title="first todo",body="a body here")

    def setUp(self):
        Todo.objects.create(title="first todo",body="a body here")

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name,"first todo")

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEquals(expected_object_name, 'a body here')