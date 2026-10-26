from django.urls import path
from website.views import *

urlpatterns = [
    path('' , index_view),
    path('contact' , contact_view),
    path('receipe' , receipe_view),
    path('single_post' , single_post_view),

]