from django import forms

class CrearSuscriptorForm(forms.Form):

    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()
    acepta_mails = forms.BooleanField()
    

class CrearPosteoForm(forms.Form):

    id_post = forms.IntegerField()
    nombre = forms.CharField(max_length=50)
    fecha_publicacion = forms.DateField()
    descripcion = forms.CharField(max_length=100)

#discos a reseñar

class WeForm(forms.Form):
    publicacion = forms.DateField()
    suscriptor = forms.CharField(max_length=40)
    critica = forms.CharField(max_length=200)

class TheCarForm(forms.Form):
    publicacion = forms.DateField()
    suscriptor = forms.CharField(max_length=40)
    critica = forms.CharField(max_length=200)

class WOTPForm(forms.Form):
    publicacion = forms.DateField()
    suscriptor = forms.CharField(max_length=40)
    critica = forms.CharField(max_length=200)

class RHCPForm(forms.Form):
    publicacion = forms.DateField()
    suscriptor = forms.CharField(max_length=40)
    critica = forms.CharField(max_length=200)

class PhoenixForm(forms.Form):
    publicacion = forms.DateField()
    suscriptor = forms.CharField(max_length=40)
    critica = forms.CharField(max_length=200)