from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    complate_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"