from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from .models import Persona


class SaveImage(TemplateView):

	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		self.filename = self.kwargs['cedula']+'.jpg'
		return super(SaveImage, self).dispatch(*args, **kwargs)

	def post(self, request, *args, **kwargs):
		
		# save it somewhere
		f = open(settings.MEDIA_ROOT + '/webcamimages/'+ self.filename, 'wb')
		f.write(request.body)
		f.close()
		# return the URL
		return HttpResponse("/media/webcamimages/" + self.filename)

	def get(self, request, *args, **kwargs):
		return HttpResponse('No esta pasando el POST')


class PersonaCreateView(CreateView):

	model = Persona
	template_name = 'home/add_persona.html'

	def form_valid(self, form):
		form.instance.foto = 'webcamimages/'+ form.instance.cedula + ".jpg"
		return super(PersonaCreateView, self).form_valid(form)

class PersonaView(DetailView):

	model = Persona
	template_name = 'home/view_persona.html'

class PersonaList(ListView):

	model = Persona
	template_name = 'home/list_persona.html'