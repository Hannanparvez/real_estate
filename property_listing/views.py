from django.shortcuts import render,redirect, get_object_or_404
from .models import Property_listing,Inquire
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator

def listings(request):
    if request.method=="POST":
        opt=request.POST['view']
        if opt=="1":
            listings=Property_listing.objects.order_by('-list_date').filter(status=True)
            hold=opt
        elif opt=="2":
            listings=Property_listing.objects.all().filter(sale_type__iexact="rent")
            hold=opt

        elif opt=="3":
            listings=Property_listing.objects.all().filter(sale_type__iexact="sale")
            hold=opt
        else:
            listings=Property_listing.objects.order_by('list_date').filter(status=True)
            hold="0"
        paginator=Paginator(listings,6)
        page=request.GET.get('page')
        paged_listings=paginator.get_page(page)
        context ={
            'listings':paged_listings,
            'hold':hold

        }
        return render(request,'property/listings.html',context)
    else:
        listings =Property_listing.objects.all().filter(status=True)

        paginator=Paginator(listings,6)
        page=request.GET.get('page')
        paged_listings=paginator.get_page(page)
        context ={
            'listings':paged_listings,
            'hold':"0",
        }
        return render(request,'property/listings.html',context)
def listing(request,listing_id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        agent=request.POST['agent_name']
        property_name=request.POST['property_name']
        agent_email=request.POST['agent_email']
        inquiry=Inquire(name=name,email=email,message=message,agent=agent,property_name=property_name)
        inquiry.save()
        messages.success(request,'Your inquiry has been made')

        return redirect('/listings/'+str(listing_id))

    listing=get_object_or_404(Property_listing,pk=listing_id)
    context ={
        'listing':listing

    }
    return render(request,'property/listing.html',context)
    