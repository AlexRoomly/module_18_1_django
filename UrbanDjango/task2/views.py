from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class index(TemplateView):
    template_name = 'index.html'

def index2(requst):
    return render(requst,'index2.html')