from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EvangelismTeamMember(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name_plural = "Evangelism Team Members"


class NewConvert(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="new_convert")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    prayer_request = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name_plural = "New Converts"


class Task (models.Models):
    task_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="task_owner")
    task_executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="task_executor")
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Tasks"


class TaskMembers(models.Model):
    members = models.ManyToManyField(NewConvert, related_name="task_members")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task_members")
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self): 
        return self.task.title