from django.db import models

class Department(models.Model):
    title = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.title}'


class Worker(models.Model):
    name = models.CharField(max_length=25, blank=False)
    email = models.EmailField(blank=False)
    salary = models.IntegerField(default=0)
    department = models.ForeignKey(Department, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.email}'
