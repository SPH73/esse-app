from django.views.generic.base import TemplateView

class DonationsPageView(TemplateView):
    template_name = 'donations/donate.html'
