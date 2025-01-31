from django import forms
from .models import EvangelismTeamMember, NewConvert, Task, TaskMembers
from django.core.validators import RegexValidator

class PhoneNumberValidator(RegexValidator):
    regex = r'^\+?1?\d{9,15}$'
    message = 'Enter a valid phone number.'

class EvangelismTeamMemberForm(forms.ModelForm):
    phone_number = forms.CharField(
        validators=[PhoneNumberValidator()],
        help_text='Enter phone number with country code'
    )

    class Meta:
        model = EvangelismTeamMember
        fields = ['full_name', 'phone_number', 'address']

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if len(full_name) < 3:
            raise forms.ValidationError("Full name must be at least 3 characters long.")
        return full_name

class NewConvertForm(forms.ModelForm):
    phone_number = forms.CharField(
        validators=[PhoneNumberValidator()],
        help_text='Enter phone number with country code'
    )

    class Meta:
        model = NewConvert
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'prayer_request']

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name and last_name and first_name == last_name:
            raise forms.ValidationError("First name and last name cannot be the same.")
        
        return cleaned_data

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'task_executor', 'completed']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Task title must be at least 5 characters long.")
        return title

class TaskMembersForm(forms.ModelForm):
    class Meta:
        model = TaskMembers
        fields = ['task', 'members']

    def clean(self):
        cleaned_data = super().clean()
        task = cleaned_data.get('task')
        members = cleaned_data.get('members')

        if task and members:
            # Optional: Add custom validation logic for task members
            if members.count() > 10:  # Example constraint
                raise forms.ValidationError("Maximum 10 members allowed per task.")
        
        return cleaned_data