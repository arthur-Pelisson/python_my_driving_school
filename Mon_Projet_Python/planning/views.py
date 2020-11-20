from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from planning.models import Planning
from planning.models import Forfait

import pdb
# Create your views here.

def is_student(user):
    return user.groups.filter(name='Student').exists()

def is_instructor(user):
    return user.groups.filter(name='Instructor').exists()

def is_admin(user):
    return user.groups.filter(name='Admin').exists()
    
def is_secretary(user):
    return user.groups.filter(name='Secretary').exists()



@login_required
# @user_passes_test(is_student)
def planning(request):
    plannings_student = request.user.student_planning.all()
    plannings_instructor = request.user.instructor_planning.all()
    forfaits = request.user.student_forfait.all()
    context = {
        'plannings_student': plannings_student,
        'plannings_instructor': plannings_instructor,
        'forfaits': forfaits
    }
    return render(request, 'planning.html', context=context)