from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    todo_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200, null=False, default='Something to do.')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    # priority = models.ForeignKey('Priority', on_delete=models.CASCADE, null=True)
    # due = models.DateTimeField()
    # reminder_timeframe = models.TimeField()
    STATUS_CHOICES = {
        ('a', 'active'),
        ('d', 'done'),
        ('r', 'removed')
    }
    status = models.CharField(
        max_length=200, 
        null=False,
        choices=STATUS_CHOICES,
        default='active')

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    Priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Low',
    )
    def __str__(self):
        return self.todo_text

class Category(models.Model):
    name = models.CharField(max_length=200, null=False, default='New Category')
    # COLOR_CHOICES = [
    #     ('y', 'yellow'),
    #     ('u', 'blue'),
    #     ('g', 'green'),
    # ]
    # color = models.CharField(
    #     max_length=10,
    #     choices=COLOR_CHOICES,
    #     default='blue',
    # )
    favorite = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

class Event(models.Model):
    description = models.CharField(max_length=200, null=False)
    ##uncommenting this next line breaks the app
    # category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    event_time = models.DateTimeField(null=True)
    # reminder_timeframe = models.DateTimeField()
    location = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.description
