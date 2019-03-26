from django import forms


# create form that takes a bunch of urls
class URIForm(forms.Form):
	uri = forms.CharField(widget=forms.Textarea)
	subdomain = forms.BooleanField(initial=False,required=False)
