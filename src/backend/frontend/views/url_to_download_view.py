from django.shortcuts import redirect, render
from django.urls import reverse

from tools.methods import DisavowFile


def url_to_download_view(request):
    try:
        url_parsed_list = request.session["urls"]
    except KeyError:
        return redirect(reverse("url_to_domain_view"))

    if request.method == "POST":
        if "download-txt" in request.POST:
            download_file = DisavowFile("disavow_file.txt", url_parsed_list, "txt", request).download
            return download_file

        elif "download-csv" in request.POST:
            download_file = DisavowFile("disavow_file.csv", url_parsed_list, "csv", request).download
            return download_file

        else:
            return redirect(reverse("url_to_domain_view"))

    else:
        context = {
            "urls": url_parsed_list
        }
        return render(request, "url-to-download.html", context)
