from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from tools.forms import URIForm
from tools.methods import URIToSplit


def url_to_domain_view(request):
    if request.method == "POST":
        if 'submit' in request.POST:
            form = URIForm(request.POST)
            if form.is_valid():

                url_parsed_list = URIToSplit(request.POST['uri'].split(), request.POST.get('subdomain', False)).new_list
                
                if url_parsed_list:

                    context = {
                        "form": form,
                        "urls": url_parsed_list,
                    }

                    request.session['urls'] = url_parsed_list
                    return redirect(reverse('url_to_download_view'))

            else:
                url_parsed_list = []
                context = {
                    "form": form,
                    "urls": url_parsed_list,
                }
            messages.add_message(request, messages.ERROR, "Please insert a valid url.")
            return redirect(reverse('url_to_domain_view'))


    else:
        form = URIForm()
        context = {
            "form": form,
            }
        return render(request, 'url-to-domain.html', context)