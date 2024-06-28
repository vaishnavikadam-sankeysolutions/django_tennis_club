from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from django.template import loader

# Create your views here.

def main(request):
  return render(request, 'main.html')

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def testing(request):
  mydata = Member.objects.all()
  template = loader.get_template('template.html')
  context = {
    'mydata': mydata,
  }
  return HttpResponse(template.render(context, request))