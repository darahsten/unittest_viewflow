Sample of unittest of Viewflow views in isolation
--------------------------------------------------
License
=======
This is a demo only. Meant for learning purposes only. You have freedom 
to do what you want with it.

Tests viewflow views in isolation using factory boy and a post generation hook.

Viewflow views are difficult to test in isolation because each view is dependent on
previous views. The official repository examples as of Mar 2020
https://github.com/viewflow/cookbook/blob/master/helloworld/demo/tests.py. Tests the views are part of
the flow.

It would not make sense to test template variables as an example in/as part of the flow. 
Your tests would explode in size. And would not.

Pre-requisites to following this.

1. Knowledge of Django https://docs.djangoproject.com/en/2.1/

2. Knowledge of Django-Viewflow http://docs.viewflow.io/

3. Knowledge of Factory boy https://factoryboy.readthedocs.io/en/latest/

In summary
----------

Create a task factory, then run necessary activations in that task factory with the post generation
hooks.

    import factory
    from django.contrib.auth import get_user_model
    from viewflow.models import Task

    from unittest_viewflow_views.flows import SampleFlow
    from unittest_viewflow_views.models import SampleProcess
    # Also include a userfactory import from wherever it is implemented.


    class SampleProcessFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = SampleProcess

        flow_class = SampleFlow


    class TaskFactory(factory.django.DjangoModelFactory):

        class Meta:
            model = Task

        process = factory.SubFactory(SampleProcessFactory)
        flow_task = SampleFlow.start

        # It is important that you supply this owner if you want to
        # reference it in the views.
        owner = factory.SubFactory(UserFactory)
        token = 'START'

        @factory.post_generation
        def run_activations(self, create, extracted, **kwargs):
            # This causes the necessary status transitions to
            # make the task executable
            activation = self.activate()

            # this if condition implies that this factory can be
            # used to generate also a flow.Start task which
            # does not have the assign method


Then, create the sample flow. 

    class TestSampleFlowUpdateViewOne(TestCase):

        def setUp(self):
            # important as you need to reverse with the pk of process
            self.process = SampleProcessFactory() 
            
            # pass in this user to the task as you will need to login as the same user
            self.task_owner = UserFactory()
            
            # this task corresponds to the flow view task you want to test. See repo for more.
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

Now you can test your views in isolation allowing you to focus your energies on testing things
where they belong.