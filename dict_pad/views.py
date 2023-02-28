from django.shortcuts import render
from django.http import HttpResponse
from .forms import PageForm

# Create your views here.
def index(request):
    form = PageForm(data={'content':""})
    context = {
        'form':form
    }
    return render(request, 'dict_pad/index.html',context=context)

def first_page(request):
    return render(request, 'dict_pad/first.html')

def second_page(request):
    return render(request, 'dict_pad/second.html')


def download(request):
    file_data = ""
    if request.method=='POST':
        form = PageForm(data=request.POST)
        if form.is_valid():
            file_data = request.POST['content']
    response = HttpResponse(file_data, content_type='application/text charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="dictationfile.txt"'
    return response
