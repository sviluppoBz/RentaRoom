from	django	import	forms
from	.models	import	Portale
class	PortaleForm(forms.ModelForm):
	class	Meta:
		model	=	Portale
		fields	=	('codice',	'descri', 'contratto')