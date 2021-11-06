from django.contrib.auth.models import User
from django.db import models


class ChartModel(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    number = models.PositiveIntegerField()
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def staff_username(self):
        return self.staff.username


# class StaffModel(User):
    # chart = models.ForeignKey(ChartModel, null=True, on_delete=models.SET_NULL)
    #
    # def __str__(self):
    #     return self.username
