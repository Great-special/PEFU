from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser, EvangelismTeamMember, NewConvert, Task, TaskMembers


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
    
    
    
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    
    phone_number = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$', 
                message="Enter a valid phone number."
            )
        ],
        required=True,
        help_text="International format preferred."
    )

    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2',
            'phone_number'
        ]

    def clean_email(self):
        email = self.cleaned_data['email']
        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

class UserProfileUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']

class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_new_password1(self):
        password = self.cleaned_data['new_password1']
        # Add custom password strength validation
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        
        # Optional: Add more complex password validation
        if password.lower() == password or password.upper() == password:
            raise forms.ValidationError("Password must contain both uppercase and lowercase letters.")
        
        return password