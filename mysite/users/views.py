from django.shortcuts import render

# Create your views here.
def list_users(request):
    template_name = "user/index.html"
    context = {
        'title' : 'list users',
    }
    return render(request, template_name, context)