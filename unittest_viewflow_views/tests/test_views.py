from django.test import TestCase
from django.urls import reverse
from viewflow.models import Task, Process

from unittest_viewflow_views.flows import SampleFlow
from unittest_viewflow_views.tests.factories import SampleProcessFactory, TaskFactory, UserFactory


class TestSampleFlowStartView(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.url = reverse('unittest_viewflow:sampleflow:start')

    def test_get(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertTrue(response.status_code, 200)

    def test_post(self):
        self.client.force_login(self.user)
        data = {'_viewflow_activation-started': '1970-01-01', 'start_field': 'Information to start'}
        response = self.client.post(self.url, data=data)
        self.assertTrue(Process.objects.get())


class TestSampleFlowUpdateViewOne(TestCase):

    def setUp(self):
        self.process = SampleProcessFactory()
        self.task_owner = UserFactory()
        self.task = TaskFactory(process=self.process, flow_task=SampleFlow.update_one, owner=self.task_owner)
        self.url = reverse('unittest_viewflow:sampleflow:update_one',
                           kwargs={'process_pk':self.process.pk, 'task_pk': self.task.pk})

    def test_get(self):
        self.client.force_login(self.task_owner)
        response = self.client.get(self.url)
        self.assertTrue(response.status_code, 200)

    def test_post(self):
        self.client.force_login(self.task_owner)
        data = {'_viewflow_activation-started': '1970-01-01', 'update_one': 'Update One'}
        response = self.client.post(self.url, data=data)
        self.assertEqual(Task.objects.get(pk=self.task.pk).status, 'DONE')


class TestSampleFlowUpdateViewTwo(TestCase):

    def setUp(self):
        self.process = SampleProcessFactory()
        self.task_owner = UserFactory()
        self.task = TaskFactory(process=self.process, flow_task=SampleFlow.update_two, owner=self.task_owner)
        self.url = reverse('unittest_viewflow:sampleflow:update_two',
                           kwargs={'process_pk': self.process.pk, 'task_pk': self.task.pk})

    def test_get(self):
        self.client.force_login(self.task_owner)
        response = self.client.get(self.url)
        self.assertTrue(response.status_code, 200)

    def test_post(self):
        self.client.force_login(self.task_owner)
        data = {'_viewflow_activation-started': '1970-01-01', 'update_two': 'Update Two'}
        response = self.client.post(self.url, data=data)
        print(response.status_code)
        self.assertEqual(Task.objects.get(pk=self.task.pk).status, 'DONE')