from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import (
    login, 
    authenticate, 
    logout, 
    update_session_auth_hash
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .models import EvangelismTeamMember, NewConvert, Task, TaskMembers
from .forms import (
    EvangelismTeamMemberForm, 
    NewConvertForm, TaskForm, 
    TaskMembersForm,
    UserRegistrationForm, 
    UserProfileUpdateForm, 
    CustomPasswordChangeForm
)

# EvangelismTeamMember Views

def landing_page(request):
    return render(request, 'landing.html')


@login_required
def evangelism_team_member_list(request):
    team_members = EvangelismTeamMember.objects.all()
    return render(request, 'evangelism/team_member_list.html', {'team_members': team_members})

@login_required
def evangelism_team_member_detail(request, pk):
    team_member = get_object_or_404(EvangelismTeamMember, pk=pk)
    return render(request, 'evangelism/team_member_detail.html', {'team_member': team_member})

@login_required
def evangelism_team_member_create(request):
    if request.method == 'POST':
        form = EvangelismTeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team member created successfully.')
            return redirect('team_member_list')
    else:
        form = EvangelismTeamMemberForm()
    return render(request, 'evangelism/team_member_form.html', {'form': form})

@login_required
def evangelism_team_member_update(request, pk):
    team_member = get_object_or_404(EvangelismTeamMember, pk=pk)
    if request.method == 'POST':
        form = EvangelismTeamMemberForm(request.POST, instance=team_member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team member updated successfully.')
            return redirect('team_member_list')
    else:
        form = EvangelismTeamMemberForm(instance=team_member)
    return render(request, 'evangelism/team_member_form.html', {'form': form})

@login_required
def evangelism_team_member_delete(request, pk):
    team_member = get_object_or_404(EvangelismTeamMember, pk=pk)
    if request.method == 'POST':
        team_member.delete()
        messages.success(request, 'Team member deleted successfully.')
        return redirect('team_member_list')
    return render(request, 'evangelism/team_member_confirm_delete.html', {'team_member': team_member})

# NewConvert Views
@login_required
def new_convert_list(request):
    new_converts = NewConvert.objects.all()
    return render(request, 'evangelism/new_convert_list.html', {'new_converts': new_converts})

@login_required
def new_convert_detail(request, pk):
    new_convert = get_object_or_404(NewConvert, pk=pk)
    return render(request, 'evangelism/new_convert_detail.html', {'new_convert': new_convert})

@login_required
def new_convert_create(request):
    if request.method == 'POST':
        form = NewConvertForm(request.POST)
        if form.is_valid():
            new_convert = form.save(commit=False)
            new_convert.user = request.user
            new_convert.save()
            messages.success(request, 'New convert added successfully.')
            return redirect('new_convert_list')
    else:
        form = NewConvertForm()
    return render(request, 'evangelism/new_convert_form.html', {'form': form})

@login_required
def new_convert_update(request, pk):
    new_convert = get_object_or_404(NewConvert, pk=pk)
    if request.method == 'POST':
        form = NewConvertForm(request.POST, instance=new_convert)
        if form.is_valid():
            form.save()
            messages.success(request, 'New convert updated successfully.')
            return redirect('new_convert_list')
    else:
        form = NewConvertForm(instance=new_convert)
    return render(request, 'evangelism/new_convert_form.html', {'form': form})

@login_required
def new_convert_delete(request, pk):
    new_convert = get_object_or_404(NewConvert, pk=pk)
    if request.method == 'POST':
        new_convert.delete()
        messages.success(request, 'New convert deleted successfully.')
        return redirect('new_convert_list')
    return render(request, 'evangelism/new_convert_confirm_delete.html', {'new_convert': new_convert})

# Task Views
@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'evangelism/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'evangelism/task_detail.html', {'task': task})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_owner = request.user
            task.save()
            messages.success(request, 'Task created successfully.')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'evangelism/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'evangelism/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully.')
        return redirect('task_list')
    return render(request, 'evangelism/task_confirm_delete.html', {'task': task})

# TaskMembers Views
@login_required
def task_members_create(request):
    if request.method == 'POST':
        form = TaskMembersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task members added successfully.')
            return redirect('task_list')
    else:
        form = TaskMembersForm()
    return render(request, 'evangelism/task_members_form.html', {'form': form})

@login_required
def task_members_delete(request, pk):
    task_members = get_object_or_404(TaskMembers, pk=pk)
    if request.method == 'POST':
        task_members.delete()
        messages.success(request, 'Task members removed successfully.')
        return redirect('task_list')
    return render(request, 'evangelism/task_members_confirm_delete.html', {'task_members': task_members})

@login_required
def dashboard(request):
    user = request.user
    if user.user_type == 'admin':
        context = {
            'team_member_count': EvangelismTeamMember.objects.count(),
            'new_convert_count': NewConvert.objects.count(),
            'completed_tasks': Task.objects.filter(completed=True).count(),
            'pending_tasks': Task.objects.filter(completed=False).count(),
            'recent_tasks': Task.objects.order_by('-date_created')[:5]
        }
    else:
        context = {
            'new_convert_count': NewConvert.objects.filter(user=user).count(),
            'completed_tasks': Task.objects.filter(completed=True, task_executor=user).count(),
            'pending_tasks': Task.objects.filter(completed=False, task_executor=user).count(),
            'recent_tasks': Task.objects.order_by('-date_created')[:5]
        }
    return render(request, 'evangelism/dashboard.html', context)


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save()
            
            # Log the user in immediately after registration
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}! Your account has been created.')
                return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'auth/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'auth/login.html')

@login_required
def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('landing_page')

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('dashboard')
    else:
        form = UserProfileUpdateForm(instance=request.user)
    
    return render(request, 'auth/profile_update.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'auth/change_password.html', {'form': form})

# Custom Password Reset Views
class CustomPasswordResetView(PasswordResetView):
    template_name = 'auth/password_reset.html'
    email_template_name = 'auth/password_reset_email.html'
    success_url = '/password_reset/done/'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'auth/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'auth/password_reset_confirm.html'
    success_url = '/password_reset/complete/'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'auth/password_reset_complete.html'