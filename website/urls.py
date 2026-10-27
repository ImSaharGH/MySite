from django.urls import path
from website.views import *

urlpatterns = [
    path('' , index_view , name='home'),
    path('contact' , contact_view , name='contact'),
    path('receipe' , receipe_view , name='receipes'),
    path('single_post' , single_post_view , name='posts'),

]