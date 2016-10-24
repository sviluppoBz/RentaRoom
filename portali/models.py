from django.db	import models

class Portale(models.Model):
	codice	=	models.CharField(max_length=3)
	descri	=	models.CharField(max_length=20)
	contratto = models.BooleanField('CONTRATTO')
	
def	publish(self):
	self.save()
	
def	__str__(self):
	return	self.codice, self.descri, self.contratto
