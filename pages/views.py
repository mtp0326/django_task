from django.shortcuts import render
from django.http import HttpResponse
from listings.models import BlogPost


def index(request):
    listings = BlogPost.objects.order_by('created_at')

    context = {
        'listings': listings
    }
    return render(request, 'pages/blog_post_list.html', context)
