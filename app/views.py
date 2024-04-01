from django.shortcuts import render, redirect
from django.views import View
from .models import Job, Location, Skills, Author
from django.contrib import messages


class HomeView(View):
    template_name = 'app/home.html'

    def get(self, reqeust):
        jobs = Job.objects.all().order_by('-created_at')
        context = {
            'jobs':jobs
        }
        return render(reqeust, self.template_name, context)


class JobDetailView(View):
    template_name = 'app/job_detail.html'

    def get(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)

        except:
            return redirect('app:home')
        context = {
            'job':job
        }
        return render(request, self.template_name, context)
