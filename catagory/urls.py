from django.urls import path
from catagory.views import *

urlpatterns = [
    path('catagory' , catagory_view , name='catagory'),
    path('catagory_post' , catagory_post_view , name='catagory-post')
]