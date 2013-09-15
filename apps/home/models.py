from django.db import models
import os

def get_image_name(instance, filename):
	f, ext = os.path.splitext(filename)
	archivo = '%s%s' % (instance.cedula, ext)
	return os.path.join('webcamimages', archivo)

class Persona(models.Model):
	"""docstring for Personal"""
	cedula = models.CharField(max_length=10)
	nombres = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=60)
	foto = models.ImageField(upload_to=get_image_name, blank=True, null=True)

	def __unicode__(self):
		return self.cedula

	@models.permalink
	def get_absolute_url(self):
		return ('persona', [str(self.id)])

	def _get_full_name(self):
		"Retorna los nombres completos de Persona"
		return '%s %s' % (self.nombres, self.apellidos)

	full_name = property(_get_full_name)