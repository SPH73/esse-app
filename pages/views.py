from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class MembershipPageView(TemplateView):
    template_name = 'membership.html'    