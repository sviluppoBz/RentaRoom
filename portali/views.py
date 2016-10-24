from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import	Portale
from .forms	import	PortaleForm

def	listaPortali(request):
	Portales = Portale.objects.filter().order_by('descri')
	return	render(request,	'portali/listaPortali.html',	{'Portales':	Portales})
	
def	ilPortale(request, pk):
	portale	=	get_object_or_404(Portale,	pk=pk)
	return	render(request,	'portali/ilPortale.html',	{'portale':	portale})	

def	nuovoPortale(request):
	if request.method == "POST":
		form=PortaleForm(request.POST)
		if form.is_valid():
			portale = form.save(commit=False)
			portale.save()
			return redirect('listaPortali')
	else:
		form = PortaleForm()
	return	render(request,	'portali/modiPortale.html',	{'form':	form})

def	modiPortale(request,	pk):
	portale	=	get_object_or_404(Portale,	pk=pk)
	if	request.method	==	"POST":
		form	=	PortaleForm(request.POST,	instance=portale)
		if	form.is_valid():
			portale	=	form.save(commit=False)
			portale.save()
			return redirect('listaPortali')
	else:
		form = PortaleForm(instance=portale)
	return	render(request,	'portali/modiPortale.html',	{'form': form})
