from django import forms

from .models import SampleProcess


class SampleCreateForm(forms.ModelForm):

    class Meta:
        model = SampleProcess
        fields = ['start_field', ]


class SampleUpdateFormOne(forms.ModelForm):

    class Meta:
        model = SampleProcess
        fields = ['update_one', ]


class SampleUpdateFormTwo(forms.ModelForm):

    class Meta:
        model = SampleProcess
        fields = ['update_two', ]
