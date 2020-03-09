from django.shortcuts import render

# Create your views here.
from viewflow.flow.views import CreateProcessView, UpdateProcessView

from unittest_viewflow_views.forms import SampleCreateForm, SampleUpdateFormOne, SampleUpdateFormTwo


class SampleCreateView(CreateProcessView):
    form_class = SampleCreateForm
    template_name = "unittest_viewflow_views/sampleprocess_form.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SampleUpdateViewOne(UpdateProcessView):
    form_class = SampleUpdateFormOne
    template_name = "unittest_viewflow_views/sampleprocess_update.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SampleUpdateViewTwo(UpdateProcessView):
    form_class = SampleUpdateFormTwo
    template_name = "unittest_viewflow_views/sampleprocess_update.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



