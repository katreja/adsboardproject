from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Iklan
from .forms import IklanForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        # query 
        all_iklan = Iklan.objects.all()
        return render(request, self.template_name, {'objects':all_iklan} )

class DetailIklanView(TemplateView):
    template_name = 'detail.html'
    id = None

    def get(self, request, id):
        # query satu object sesuai id
        iklan = Iklan.objects.get(id=id)
        return render(request, self.template_name, {'object':iklan})

class AddIklanView(TemplateView):
    template_name = 'add.html'

    def get(self, request):
        form = IklanForm()
        return render(request, self.template_name, {'form':form})

class AboutView(TemplateView):
    template_name = "about.html"

    def get(self, request):
        return render(request, self.template_name)