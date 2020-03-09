from django.urls import path, include
from viewflow.flow.viewset import FlowViewSet

from unittest_viewflow_views.flows import SampleFlow

sample_flow_urls = FlowViewSet(SampleFlow).urls


app_name = 'unittest_viewflow'

urlpatterns = [
    path(r'sampleflow/', include((sample_flow_urls, 'sampleflow'), namespace='sampleflow')),
]
