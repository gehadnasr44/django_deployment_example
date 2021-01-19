from django.conf.urls import url
from app import views

app_name= 'app'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
    
]