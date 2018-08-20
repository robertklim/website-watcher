from bs4 import BeautifulSoup
from django.shortcuts import render, redirect

from websites.models import Website

from .models import Check

import hashlib
import requests

def check_user_websites(request):
    user = request.user
    websites = Website.objects.filter(user=user)
    for website in websites:
        check_website(request, website.pk)
    return redirect('/websites')

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

    return redirect('/websites')


