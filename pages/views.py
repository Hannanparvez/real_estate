from django.shortcuts import render,redirect
from property_listing.models import Property_listing,Testimonial,Agent
from agents.models import Agent
from django.contrib import messages
from blog.models import Blog
from pages.models import Feedback
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
# Create your views here.
def index(request):
    sliders=Property_listing.objects.order_by('-list_date').filter(slider=True)
    latest=Property_listing.objects.order_by('-list_date')[:4]
    baoms=Agent.objects.all().filter(is_mvp=True)
    blogs=Blog.objects.order_by('-blog_date')[:4]
    testimonials=Testimonial.objects.all()
    context={
        'sliders':sliders,
        'latests':latest,
        'baoms':baoms,
        'blogs':blogs,
        'testimonials':testimonials,


    }
    
    return render(request,'pages/index.html',context)

def agents(request):
    agents=Agent.objects.all().order_by('hire_date')
    paginator=Paginator(agents,6)
    page=request.GET.get('page')
    paged_agents=paginator.get_page(page)
       
    context={
        'agents':paged_agents,
    }

    return render(request,'pages/agents.html',context)

def about(request):
    team=Agent.objects.all().filter(is_team=True)
    context={
        "team":team,
    }
    return render(request,'pages/about.html',context)


def contact(request):
    
    if request.method=="POST":
       
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        if name=="" or email=="" or subject=="" or message=="":
            messages.error(request,'The contact form cannot be empty')
            return render(request,'pages/contact.html')
        feedback=Feedback(name=name,email=email,message=message,subject=subject)
        feedback.save()
        messages.success(request,'Thank you so much for your feedback..wil get back')
        return redirect('contact')
    else:
        return render(request,'pages/contact.html')


    

    


def search(request):
    listings=Property_listing.objects.all().order_by('-list_date')

    #keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            listings=listings.filter(description__icontains=keywords)
    # city
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            listings=listings.filter(city__iexact=city)      
    # state
    if 'type' in request.GET:
        sale_type=request.GET['type']
        if sale_type:
            listings=listings.filter(sale_type__iexact=sale_type)     
    # price
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            listings=listings.filter(price__gte=price)     
    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            listings=listings.filter(bedrooms__lte=bedrooms)
    if 'bathrooms' in request.GET:
        bathrooms=request.GET['bathrooms']
        if bathrooms:
            listings=listings.filter(bathrooms__lte=bathrooms)
    context={
        "listings":listings
    }
    return render(request,'pages/search.html',context)