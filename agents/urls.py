from django.urls import path 
from . import views

urlpatterns=[
    path('<int:agent_id>',views.agent,name='agent'),
   

]