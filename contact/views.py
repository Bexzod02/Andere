from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Contactform
# Create your views here.
def contact_view(request):
    form = Contactform(request.POST or None)
    if form.is_valid():
        form.save() 
        messages.success(request, 'successfully send your message')
        return redirect('#contact/')
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)
