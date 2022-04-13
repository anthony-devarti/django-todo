from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200, null=False, default='Something to do.')
    # category = models.ForeignKey(Category, on_delete)
    # priority = models.ForeignKey(Priority, on_delete)
    # due = models.DateTimeField()
    # reminder_timeframe = models.TimeField()
    status = models.CharField(max_length=200, null=False, default='active')
    # user = models.ForeignKey(User, on_delete)

class Category(models.Model):
    name = models.CharField(max_length=200, null=False, default='New Category')
    # color = models.CharField(max_length=200, default='blue')
    favorite = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete)

class Event(models.Model):
    description = models.CharField(max_length=200, null=False)
    # category = models.ForeignKey(Category, on_delete)
    # event_time = models.DateTimeField()
    # reminder_timeframe = models.DateTimeField()
    location = models.CharField(max_length=200, null=True)
    # user = models.ForeignKey(User, on_delete)

# class Priority(models.Model):
#     PRIORITY_LEVELS={
#         ('1', 'High'),
#         ('2', 'Medium'),
#         ('3', 'Low'),
#     }