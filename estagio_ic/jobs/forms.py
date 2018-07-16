from django import forms

from jobs.models import JobOpportunity
from jobs.models import Application


class JobOpportunityRegisterForm(forms.ModelForm):
    class Meta:
        model = JobOpportunity
        fields = (
            'name', 'enterprise',
            'salary', 'weekly_workload',
            'description','requirements',
            'benefits',
        )

