from tldextract import extract
from django.http import HttpResponse

import os

class URIToSplit():
	def __init__(self, uri_list: list, subdomain=False):
		self.uri_list = uri_list
		self.subdomain = subdomain
		self.new_list = self.check_if_url_list_is_valid()

	def return_new_list(self, valid_url_list: list):
		if self.subdomain:
			return self.create_new_list_subdomains(valid_url_list)
		else:
			return self.create_new_list_no_subdomains(valid_url_list)

	def create_new_list_subdomains(self, valid_url_list: list):
		return [self.return_subdomain_domain_suffix(i).lower() for i in valid_url_list]

	def create_new_list_no_subdomains(self, valid_url_list: list):
		return [self.return_domain_suffix(i).lower() for i in valid_url_list]

	def return_domain_suffix(self, url: str):
		parsed_url = extract(url)
		return "{parsed_url.domain}.{parsed_url.suffix}".format(parsed_url=parsed_url)

	def return_subdomain_domain_suffix(self, url: str):
		parsed_url = extract(url)
		if parsed_url.subdomain == "" or parsed_url.subdomain == "www":
			subdomain = ""
		else:
			subdomain = "{x.subdomain}.".format(x=parsed_url)
		return "{}{parsed_url.domain}.{parsed_url.suffix}".format(subdomain, parsed_url=parsed_url)

	def check_suffix_true(self, url):
		parsed_url = extract(url)
		if len(parsed_url.suffix) > 0:
			return True
		else:
			return False

	def return_valid_domain(self, url):
		if self.check_suffix_true(url):
			return url

	def check_if_url_list_is_valid(self):
		if len(self.uri_list) == 0:
			return []
		else:
			valid_url_list = [self.return_valid_domain(url) for url in self.uri_list]
			# print("valid_url_list is " + str(valid_url_list))
			try:
				if len(valid_url_list) > 0:
					new_list = list(set(self.return_new_list(valid_url_list)))
					return new_list
					# return self.return_new_list()

			except TypeError:
				return []


class DisavowFile():
	def __init__(self, file:str, url_parsed_list:list, file_type:str, request):
		self.file = file
		self.url_parsed_list = url_parsed_list
		self.file_type = file_type
		self.download = self.download_file()

	def write_links_into_file(self):
		with open(self.file, 'w') as f:
			for url in self.url_parsed_list:
				f.write(f'domain:{url}\n')

	def write_links_into_csv_file(self):
		with open(self.file, 'w') as f:
			for url in self.url_parsed_list:
				f.write(f'domain:{url},')


	def download_file(self):
		if self.file_type == 'txt':
			self.write_links_into_file()
		else:
			self.write_links_into_file()
			
		with open(self.file, 'rb') as f:
			response = HttpResponse(f.read(), content_type='application/txt')
			response['Content-Disposition'] = f'attachment; filename={self.file}'
			response['Content-Type'] = 'application/text; charset=utf-16'
			# Remove file from application
			os.remove(self.file)
			# Download file
			return response