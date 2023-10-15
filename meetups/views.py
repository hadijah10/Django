from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetups
# Create your views here.

def index(request):
    meetups = Meetups.objects.all()
    return render(request, 'meetups/index.html',{
        "showmeetups":True,
        "meetups":meetups
    })
def meetup_details(request,meetup_slug):
    try:
        selected_meetup = Meetups.objects.get(slug=meetup_slug)
        return render(request,'meetups/meetup-details.html',{
            'meetup_found':True,
        "meetup_title":selected_meetup.title,
        "meetup_description":selected_meetup.description})
    except Exception as exc:
        return render(request,'meetups/meetup-details.html',{
            'meetup_found':False
        })