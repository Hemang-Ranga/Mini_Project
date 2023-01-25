from django.shortcuts import render
from .forms import PageForm

# Create your views here.
def index(request):
    form = PageForm(request.POST)
    context = {
        'form':form
    }
    return render(request, 'dict_pad/index.html',context=context)
