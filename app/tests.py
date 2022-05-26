"""
# Create your tests here.
from django.db import models
from django.test import TestCase, Client
import pytest
from taskTodo.models import *
# Create your tests here.
class Test_TODO(TestCase):

    def setUp(self):
        
        self.c = Client()

    def test_index_url(self):
        response=self.c.get('/')
        assert response.status_code==200

    def test_nav_bar(self):
        response=self.c.get('/')
        assert b'todo' in response.content.lower()
        assert b'view task' in response.content.lower()

    def test_create_task(self):
        payload = {'name': 'user01', 'task': 'testcase'}
        response = self.c.post('/', data=payload, allow_redirects = True)
        assert payload['name']==Todo.objects.first().name
        assert 1==Todo.objects.count()
        

    def test_task_view_url(self):
        response=self.c.get('/task_view/')
        assert response.status_code==200

    def test_task_view_content(self):
        tasks=Todo(name='tester',task='testing')
        tasks.save()
        response=self.c.get('/task_view/')
        assert b"tester" in response.content.lower()

    def test_task_not_completed(self):
        tasks=Todo(name='tester',task='testing')
        tasks.save()
        response=self.c.post('/cross/1/', allow_redirects = True)
        assert Todo.objects.first().completed == True

    def test_task_completed(self):
        tasks=Todo(name='tester',task='testing')
        tasks.save()
        response=self.c.post('/uncross/1/', allow_redirects = True)
        assert Todo.objects.first().completed == False
"""