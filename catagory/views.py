from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def catagory_post_view(request):
    return render(request, 'catagory/catagory-post.html')

def catagory_view(request):
    return render(request, 'catagory/catagory.html')