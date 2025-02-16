from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def project_detail(request, project_id):
    template_name = f'projects/project-{project_id}.html'
    return render(request, template_name)

def hire_me(request):
    return render(request, 'hire-me.html')

def projects(request):
    return render(request, 'projects.html')

def privacy(request):
    return render(request, 'privacy.html')

def faq(request):
    return render(request, 'faq.html')

def payment(request):
    return render(request, 'payment.html')

def base_view(request):
    return render(request, 'base.html')