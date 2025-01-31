from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import EvangelismTeamMember, NewConvert, Task, TaskMembers
from .forms import EvangelismTeamMemberForm, NewConvertForm, TaskForm, TaskMembersForm

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