from django.shortcuts import render, redirect
from django.views import View
from .forms import SubscribeForm

class SubscribeView(View):
    template_name = 'subscribe/subscribe.html'
    form_class = SubscribeForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form':form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscribe:thank_you')
        context = {
            'form':form
        }
        return render(request, self.template_name, context)

class ThankYouView(View):
    template_name = 'subscribe/thank_you.html'

    def get(self, request):
        return render(request, self.template_name)
