from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

def HomeView(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


class AboutView(TemplateView):
    template_name = "about.html"