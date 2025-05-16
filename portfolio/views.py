from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Skill, Project, Experience, Education, Article, SocialLink

def home(request):
    context = {
        'about': About.objects.first(),
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
        'experiences': Experience.objects.all(),
        'education': Education.objects.all(),
        'articles': Article.objects.all(),
        'socials': SocialLink.objects.all(),
    }
    return render(request, 'portfolio/home.html', context)