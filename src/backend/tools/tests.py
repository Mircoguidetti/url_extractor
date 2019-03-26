from django.test import TestCase

from tools.methods import URIToSplitKev


class URLToSplitTestCase(TestCase):
	def setUp(self):
		# url list input - post data
		self.uri_list = [
			"https://www.rebootonline.com/asdsadsd",
			"https://rebootonline.com/asdsadsd",
			"rebootonline.com/asdsadsd",
			"www.rebootonline.com/asdsadsd",
			"aspsd.rebootonline.com/asdsadsd",
			"https://wew.easpsd.rebootonline.com/sdsdsd",
			"wew.easpsd.rebootonline.com/sdsdsd"
		]

		# what the list should be if subdomain == True
		# www needs to be striped
		self.uri_subdomain_list = [
			"rebootonline.com",
			"rebootonline.com",
			"rebootonline.com",
			"rebootonline.com",
			"aspsd.rebootonline.com",
			"wew.easpsd.rebootonline.com",
			"wew.easpsd.rebootonline.com"
		]

		# what the list should be if subdomain == False
		self.uri_no_subdomain_list = [
			"rebootonline.com",
			"rebootonline.com",
			"rebootonline.com",
			"rebootonline.com",
			"rebootonline.com",
			"rebootonline.com",
			"rebootonline.com"
		]

	def test_return_domain_and_suffix(self):
		split_urls = URIToSplitKev(self.uri_list, False)  
		self.assertEqual(split_urls.new_list, self.uri_no_subdomain_list)

	def test_return_subdomain_doamin_and_suffix(self):
		split_urls = URIToSplitKev(self.uri_list, True)
		self.assertEqual(split_urls.new_list, self.uri_subdomain_list) 






