from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog,Comment,Reply
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator

# Create your views here.
def blogs(request):
    blogs=Blog.objects.order_by('-blog_date').all()
    paginator=Paginator(blogs,6)
    page=request.GET.get('page')
    paged_blogs=paginator.get_page(page)
    context={
        'blogs':paged_blogs,
    }
    return render(request,'blog/blogs.html',context)

def blog(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    if request.method=="POST":
        comment_author=request.POST['name']
        comment_author_email=request.POST['email']
        comment_content=request.POST['message']
        comment_on=blog
        comment=Comment(comment_author=comment_author,comment_author_email=comment_author_email
        ,comment_content=comment_content,comment_on=comment_on)
        comment.save()
        messages.success(request,'Your comment has been posted')
        return redirect('/blogs/'+str(blog_id))
    
    
    comments=Comment.objects.order_by('-comment_date').filter(comment_on=blog)
    total_comments=comments.count()
    # reply=Reply.objects.order_by('-reply_date').filter(reply_on=blog)
    
    reply=Reply.objects.order_by('-reply_date').filter(reply_on=blog)
    total_comments=comments.count()+ reply.count()
        
        
        

    
    
    context ={
        'blog':blog,
        'comments':comments,
        'reply':reply,
        'total_comments':total_comments,


    }
    return render(request,'blog/blog.html',context)