from django import forms

from user_actions.models import Student
from user_actions.models import Enterprise


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'name', 'pw', 'id_doc_number',
            'enroll_number', 'major_id',
            'qualifications','gpa',
            'description',
        )

class EnterpriseRegisterForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = (
            'name', 'pw', 'description',
        )
