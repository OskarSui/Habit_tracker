from django.db import models
from django.contrib.auth.models import User


class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    goal = models.IntegerField()
    frequency = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='habits', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['-created_at']


class Journal(models.Model):
    date = models.DateField()
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)


class Bonus(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points_required = models.PositiveIntegerField()

    def __str__(self):
        return self.name
