from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return render(request, 'website/index.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def receipe_view(request):
    return render(request, 'website/receipe.html')

def single_post_view(request):
    return render(request, 'website/single-post.html')