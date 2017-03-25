from django import forms

class AddForm(forms.Form):
	a = forms.IntegerField()
	b = forms.IntegerField()
	c = forms.IntegerField()
	d = forms.CharField(max_length=30)
