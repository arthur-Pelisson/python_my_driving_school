from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.decorators import login_required, user_passes_test




class Planning(models.Model):
    student = models.ForeignKey(User,related_name='student_planning' ,on_delete=models.CASCADE)
    instructor = models.ForeignKey(User,related_name='instructor_planning' ,on_delete=models.CASCADE)
    hour = models.CharField(max_length=42)
    location = models.CharField(max_length=42)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date et heure du rendez vous")

    
    class Meta:
        ordering = ['date']
    

    def __str__(self):
        return self.instructor.username + ' - ' + self.student.username + ' ' + str(self.date)


class Forfait(models.Model):
    student = models.ForeignKey(User,related_name='student_forfait' ,on_delete=models.CASCADE)
    heur_payer = models.CharField(max_length=42)
    total_heur= models.CharField(max_length=42)


    def __str__(self):
        return self.student.username
