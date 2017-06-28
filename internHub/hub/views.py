# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from .models import Job

def index(request):
    job_list = Job.objects.all().order_by('deadline')
    context = {
        'job_list': job_list,
    }
    return render(request, 'hub/index.html', context)

def job_view(request, job_id):
    job = Job.objects.get(id=job_id)
    context = {
        'job': job,
    }
    return render(request, 'hub/job.html', context)

def skill_filter(request, skill):
    job_list = Job.objects.filter(skill=skill)
    context = {
        'job_list': job_list,
    }
    return render(request, 'hub/index.html', context)
