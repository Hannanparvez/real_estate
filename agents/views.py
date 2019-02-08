from django.shortcuts import render,get_object_or_404
from .models import Agent
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from property_listing.models import Property_listing

# Create your views here.
def agent(request,agent_id):
    agent=get_object_or_404(Agent,pk=agent_id)
    listings=Property_listing.objects.all().filter(agent=agent)
    if request.method=="POST":
        
        opt=request.POST['view']
        if opt=="1":
            listings=listings.filter(status=True)
            hold=opt
        elif opt=="2":
            listings=listings.filter(sale_type__iexact="rent")
            hold=opt

        elif opt=="3":
            listings=listings.filter(sale_type__iexact="sale")
            hold=opt
        else:
            listings=listings.filter(status=True)
            hold="0"
        
        
        # listings=listings.filter(agent=agent)
        total_listings=listings.count()
        context={
            'agent':agent,
            'listings':listings,
            'hold':"0",
            'total_listings':total_listings

        }
        return render(request,'agents/agent.html',context)
    else:
        # agent=get_object_or_404(Agent,pk=agent_id)
        listings =listings.filter(status=True)
        total_listings=listings.count()
        context={
            'agent':agent,
            'listings':listings,
            'hold':"0",
            'total_listings':total_listings

        }
       
        return render(request,'agents/agent.html',context)
    

    # return render(request,'agents/agent.html',context)