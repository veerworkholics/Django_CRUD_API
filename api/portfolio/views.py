import json
from django.shortcuts import render

from django.http import HttpResponse
from .models import Job
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return HttpResponse("welcome to my portfolio")

@csrf_exempt
def job(request):
    if request.method =="GET":
        result = []
        jobs = Job.objects.all()
        for job in jobs:
            data = {
                "company":job.company,
                "description":job.description,
            }
            result.append(data)
        return HttpResponse(json.dumps(result))

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        company = data['company']
        description = data['description']
        job = Job(company = company, description = description)
        job.save()
        return HttpResponse("Company Added successfully")
    
    if request.method == "DELETE":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        company = data['company']
        job = Job.objects.filter(company=company).delete()
        return HttpResponse("Company deleted successfully")

    #  if request.method == "POST":
    #     body_unicode = request.body.decode('utf-8')
    #     data = json.loads(body_unicode)
    #     id = data['id']
    #     company = data['company']
    #     description = data['description']
    #     job = Job(id =id, company = company, description = description)
    #     job.save()
    #     return HttpResponse("Company deleted successfully")
        

