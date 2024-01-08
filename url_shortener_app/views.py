from django.shortcuts import render
from .models import URLMapping
import random
import string

def shorten_url(request):
    shortened_url = None
    original_url = None
    if request.method == 'POST':
        long_url_input = request.POST.get('long_url')
        short_code_input = request.POST.get('short_code')

        if long_url_input:
            short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            new_mapping = URLMapping(original_url=long_url_input, short_code=short_code)
            new_mapping.save()
            shortened_url = f"{short_code}"

        if short_code_input:
            original_url = expand_url(short_code_input)
            
    return render(request, 'shorten_url.html', {'shortened_url': shortened_url, 'original_url': original_url})

def expand_url(short_code_input):
    try:
        mapping = URLMapping.objects.get(short_code=short_code_input)
        return mapping.original_url
    except URLMapping.DoesNotExist:
          return "Link does not exist."
