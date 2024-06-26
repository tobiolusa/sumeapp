from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Profile
import pdfkit
from django.http import HttpResponse 
from django.template import loader
import io

def index(request): 
    return render(request, 'sumeapp/index.html')
    
    
def register(request):
    if request.method == "POST": 
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone_number = request.POST.get('phone_number', "")
        job_role = request.POST.get('job_role', "")
        summary = request.POST.get('summary', "")
        degree = request.POST.get('degree', "")
        school = request.POST.get('school', "")
        university = request.POST.get('university', "")
        previous_work = request.POST.get('previous_work', "")
        skills = request.POST.get('skills', "")
        
        profile = Profile(name=name, email=email, phone_number=phone_number, summary=summary, degree=degree, school=school, university=university, previous_work=previous_work,skills=skills)
        profile.save()
        return redirect(reverse('resume', args=[profile.id]))
    return render(request, 'sumeapp/register.html')


def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('sumeapp/resume.html')
    html = template.render({'user_profile': user_profile})
    options = {
        'page-size' : 'Letter',
        'encoding' : 'UTF-8',
        }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Dospositon'] = 'attachment'
    filename = "resume.pdf"
    return response



    