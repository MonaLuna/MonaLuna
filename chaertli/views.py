from django.http import HttpResponse
from django.views.generic import ListView

from .models import Chaertli

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")	


class ChaertliListView(ListView):

	model = Chaertli
	template_name = "chaertli/list.html"		