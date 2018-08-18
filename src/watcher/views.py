from bs4 import BeautifulSoup
from django.shortcuts import render

from websites.models import Website

from .models import Check

import hashlib
import requests

def check_website(request, website_pk):
    website = Website.objects.get(pk=website_pk)
    website_url = website.url
    
    source = requests.get(website_url).text
    soup = BeautifulSoup(source, 'lxml')
    
    website_hash = hashlib.md5(str(soup).encode('utf-8')).hexdigest()

    try:
        last_check = Check.objects.filter(website_url=website_url).latest()
    except Check.DoesNotExist:
        last_check = None

    if last_check is not None:
        result = 'ok' if last_check.website_hash == website_hash else 'err'
    else:
        result = 'first check'

    Check.objects.create(
        website = website,
        website_url = website_url,
        website_hash = website_hash,
        result = result,
    ).save()

    return render(request, 'home.html', {})


