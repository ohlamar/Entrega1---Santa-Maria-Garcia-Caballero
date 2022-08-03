from cbv.models import Agent
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateAgent(CreateView):
    model = Agent
    template_name = 'agent/create_agent.html'
    success_url= '/cbv/list-agent'
    fields= ['nickname','age', 'date']
    
    
class ListAgent(ListView):
    model = Agent
    template_name = 'agent/list_agent.html'
    
    
class DeleteAgent(LoginRequiredMixin, DeleteView):
    model = Agent
    template_name = 'agent/delete.html'
    success_url= '/cbv/list-agent'
    
    
class ModifyAgent(LoginRequiredMixin, UpdateView):
    model = Agent
    template_name = 'agent/modify.html'
    success_url= '/cbv/list-agent'
    fields= ['nickname','age', 'date']


class ViewAgent(DetailView):
    model = Agent
    template_name = 'agent/view_agent.html'