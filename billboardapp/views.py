from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Posts
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from .forms import PostForm


def index (request):
    form = PostForm()
    all_posts = Posts.objects.filter(visible=True)
    current_time = datetime.now()
    return render(request, 'billboardapp/post.html', {'form': form, 'all_posts': all_posts, 'date_now': current_time })


@csrf_exempt
def addpost(request):
    if request.method == 'POST':
        
        form = PostForm(request.POST) 
        print(form)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            
            response_data = {}

            response_data['result'] = 'Create post successful!'
            response_data['postpk'] = post.pk
            response_data['text'] = post.text
            response_data['created'] = post.created_date.strftime('%B %d, %Y %I:%M %p')
            response_data['author'] = post.author

            print(response_data)
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")



@csrf_exempt
def deletePost(request):
    if request.method == 'POST':
        id = request.POST.get('postid')
        print(id)

        postToDelete = Posts.objects.get(pk=id)
        print(postToDelete)
        postToDelete.visible = False
        postToDelete.save()

        return HttpResponse(json.dumps({"Completed": "Post Removed"}),content_type="application/json")