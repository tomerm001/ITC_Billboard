from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Posts, Comments
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


# main funtion to render page
def index (request):

    # get form template for posts and comments
    postform = PostForm()
    commentform = CommentForm()

    # query all posts that are visible/not deleted
    all_posts = Posts.objects.filter(visible=True)

    # get specific logged in user
    logged_user = request.user

    # get time comment or post are added to database
    current_time = datetime.now()

    return render(request, 'billboardapp/post.html', {'form': postform, 'commentform': commentform, 'all_posts': all_posts, 'date_now': current_time, 'user': logged_user })


# function to add new post to database
def addpost(request):
    if request.method == 'POST':

        form = PostForm(request.POST) 

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            
            # build data for response
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

# function to delete/make invisible specific post
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


# function to add comments to database
def addcomment(request):
    if request.method == 'POST':
        
        # get specific request
        ajaxdata = request.POST#.get('form')
   
        # add data to form
        form = CommentForm(ajaxdata) 
        
        if form.is_valid():

            specific_post = Posts.objects.get(pk=ajaxdata['postnumber'])
     
            commentpost = form.save(commit=False)
            commentpost.post_id = specific_post
            commentpost.author = request.user.username
            commentpost.save()
            
            # build response data for Ajax
            response_data = {}

            response_data['result'] = 'Create post successful!'
            response_data['postpk'] = commentpost.pk
            response_data['text'] = commentpost.text_comment
            response_data['created'] = commentpost.created_date.strftime('%B %d, %Y %I:%M %p')
            response_data['author'] = commentpost.author

            # print(response_data)
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")


# funtion to delete/make invisible comment from database
@csrf_exempt
def deleteComment(request):
    if request.method == 'POST':
        id = request.POST.get('commentid')
        print(id)

        commentToDelete = Comments.objects.get(pk=id)
        print(commentToDelete)
        commentToDelete.visible = False
        commentToDelete.save()

        return HttpResponse(json.dumps({"Completed": "Comment Removed"}),content_type="application/json")

