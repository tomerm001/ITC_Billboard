from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Posts
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
# Create your views here.

def index(request):
    all_posts = Posts.objects.all()
    current_time = datetime.now()
    context = {'all_posts': all_posts, 'date_now': current_time}
    print(context)
    return render(request, 'billboardapp/index.html', context)

@csrf_exempt
def addpost(request):
    if request.method == 'POST':

        post_title = request.POST.get('post_title')
        post_text = request.POST.get('post_text')
        post_author = request.POST.get('post_author')

        post = Posts(text=post_text, author=post_author, title=post_title)
        post.save()

        response_data = {}

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created'] = post.created_date.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


