from django.shortcuts import render, redirect

# Create your views here.

def HomePage(request):
    return render(request, 'home.html')

def DiscoveryPage(request):
    return render(request, 'discovery.html')

def SocialNetworking(request):
    return render(request,'social.html' )


def BusinessPage(request):
    return render(request, 'business.html')

def VirtualClosetPage(request):
    return render(request, 'virtual_closet.html')
