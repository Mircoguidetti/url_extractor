from django.shortcuts import redirect
from django.urls import reverse

def home_view(request):
	return redirect(reverse('url_to_domain_view'))