from django.views.generic import ListView

from .models import Padron


class PadronListViews(ListView):
    model = Padron
    template_name = "padron.html"
