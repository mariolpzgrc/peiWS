from django import forms

class UsuarioForm(forms.ModelForm):
	contrasena = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Usuario