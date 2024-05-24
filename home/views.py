from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    #return HttpResponse("this is a homepage")
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")

from .models import Contact  # Ensure you import the Contact model

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        # Create an instance of the Contact model
        contact = Contact(name=name, phone=phone, address=address)
        
        # Save the instance to the database
        contact.save()
        
        # Show success message
        messages.success(request, 'Your message has been sent') 
        
        # Redirect to prevent form resubmission
        return redirect('contact')  
    
    return render(request, "contact.html")


