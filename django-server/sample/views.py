from django.shortcuts import render

# Create your views here.
def index(request):
    content = {
        'title' : 'sample page',
        'msg' : 'coding coding'
    }
    return render(request,'sample/index.html',content)