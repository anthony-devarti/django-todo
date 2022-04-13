from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_text = models.CharField(max_length=200),
    pub_date = models.DateTimeField('date published'),
    description = models.CharField(max_length=200, null=False),
    # category = models.ForeignKey(Category, on_delete),
    # priority = models.ForeignKey(Priority, on_delete),
    due = models.DateTimeField(default='null'),
    reminder_timeframe = models.TimeField(default='null'),
    status = models.CharField(default='active'),
    # user = models.ForeignKey(User, on_delete),

class Category(models.Model):
    name = models.CharField(max_length=200, default='New Category'),
    color = models.CharField(default='blue'),
    favorite = models.BooleanField(default=False),
    # user = models.ForeignKey(User, on_delete)

class Event(models.Model):
    description = models.CharField(max_length=200, null=False)
    # category = models.ForeignKey(Category, on_delete),
    event_time = models.DateTimeField(null=False),
    reminder_timeframe = models.DateTimeField(default='null'),
    location = models.CharField(default='null'),
    # user = models.ForeignKey(User, on_delete)

class Priority(models.Model):
    PRIORITY_LEVELS={
        '1': 'High',
        '2': 'Medium',
        '3': 'Low',
    }