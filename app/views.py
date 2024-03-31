from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, reqeust):
        pass

    def post(self, request):
        pass


class JobDetailView(View):
    def get(self, request, job_id):
        pass

    def post(self, request, job_id):
        pass