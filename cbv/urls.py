from django.urls import path
from . import views


urlpatterns = [
    
    path('create-agent/', 
         views.CreateAgent.as_view(), 
         name='create_agent'),
    
    path('list-agent/', 
         views.ListAgent.as_view(), 
         name='list_agent'),
    
    path('modify/<int:pk>/', 
         views.ModifyAgent.as_view(), 
         name='modify'),
    
    path('delete-agent/<int:pk>/', 
         views.DeleteAgent.as_view(), 
         name='delete_agent'),
    
    path('view-agent/<int:pk>/', 
         views.ViewAgent.as_view(), 
         name='view_agent'),
]