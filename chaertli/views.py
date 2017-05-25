from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import Chaertli, TextInhaut

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")	


class ChaertliListView(ListView):

	model = Chaertli
	template_name = "chaertli/list.html"		


class ChaertliDetailView(DetailView):
	
	context_object_name = "chaertli"
	model = Chaertli
	template_name = "chaertli/detail.html"	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context.update({
			"fragen": TextInhaut.objects.filter(
				sitae__chaertli=self.object,
				sitae__loesig=False,
			),
			"loesungen": TextInhaut.objects.filter(
				sitae__chaertli=self.object,
				sitae__loesig=True,
			),
		})
		return context