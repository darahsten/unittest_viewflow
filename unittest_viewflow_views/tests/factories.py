import factory
from django.contrib.auth import get_user_model
from viewflow.activation import ViewActivation
from viewflow.models import Task

from unittest_viewflow_views.flows import SampleFlow
from unittest_viewflow_views.models import SampleProcess


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: 'user-{0}'.format(n))
    email = factory.Sequence(lambda n: 'user-{0}@example.com'.format(n))
    is_active = True
    password = factory.PostGenerationMethodCall('set_password', 'password')


class SampleProcessFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = SampleProcess

    flow_class = SampleFlow


class TaskFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Task

    process = factory.SubFactory(SampleProcessFactory)
    flow_task = SampleFlow.start
    owner = factory.SubFactory(UserFactory)
    token = 'START'

    @factory.post_generation
    def run_activations(self, create, extracted, **kwargs):
        activation = self.activate()
        if hasattr(activation, 'assign'):
            activation.assign()

