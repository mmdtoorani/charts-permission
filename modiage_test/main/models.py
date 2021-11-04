from django.contrib.auth.models import User
from django.db import models


class ChartModel(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    type = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.staff} | {self.number}"

    def staff_username(self):
        return self.staff.username
