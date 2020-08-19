from django.db.models import Q
from django.views.generic import TemplateView

from .models import Car


class CarView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        query = Q()
        for key, value in self.request.GET.items():
            if len(value) > 0:
                query &= Q(**{key: value})
        return {'cars': Car.objects.filter(query)}
