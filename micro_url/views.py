from rest_framework import viewsets, status
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse


from .models import URLService
from .serializers import URLServiceSerializer


class URLServiceViewSet(viewsets.ModelViewSet):
    """
    Get a list of URL's that have been shortened
    Create a new Short URL
    Read a URL
    Update a URL
    and Delete a URL
    """

    queryset = URLService.objects.all()
    serializer_class = URLServiceSerializer
    ordering = ('original_url',)


def redirect_original(request, short_id):
    """
    Redirect a URL based on the short_id param to the original URL
    and increment the count
    :param self:
    :return:
    """
    url = get_object_or_404(URLService, pk=short_id)  # get full original URL from ID
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.original_url)
