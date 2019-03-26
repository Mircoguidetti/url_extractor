from django.contrib import admin
from django.urls import path

from frontend.views import (
	url_to_domain_view, 
	url_to_download_view,
	home_view,
	)


urlpatterns = [
	path('', home_view, name = 'home_view'),
    path('tools/url-to-domain/', url_to_domain_view, name="url_to_domain_view"),
    path('tools/url-to-download/', url_to_download_view, name="url_to_download_view"),
]
