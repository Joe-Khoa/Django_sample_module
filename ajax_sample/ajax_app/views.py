from django.shortcuts import render,HttpResponse
from ajax_app.models import Like,Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'post/index.html',{'posts':posts})
def LikePost(request):
    if request.method == 'GET':
        # post_id = request.GET['post_id']
        # likepost = Post.objects.get(pk=post_id) # get liked_post
        # m = Like(post=likepost) # create like_obj
        # m.save()
        return HttpResponse('success!')
    else:
        return HttpResponse('req is not GET_method')
