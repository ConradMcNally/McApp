from django.db import models

class Family(models.Model):
    first_name = models.CharField(max_length=70)
    second_name = models.CharField(max_length=70)
    dob = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

class Job(models.Model):
    company = models.CharField(max_length=70)
    role = models.CharField(max_length=70)
    pay = models.IntegerField()

    def __str__(self):
        return f"{self.role} at {self.company}"

class FamilyJobs(models.Model):
    family_id = models.ForeignKey(Family, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.family_id} works as a {self.job_id}"

