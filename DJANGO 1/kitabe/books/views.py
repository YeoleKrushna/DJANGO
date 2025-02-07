from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Books
from .forms import BooksForm
# Create your views here.
def home(request):
    books = Books.objects.all()
    if request.method == "POST":
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            print("Form is invalid:", form.errors)
        data = Books.objects.all()
    else:
        form = BooksForm()
        books = Books.objects.all()

    return render(request, 'books/home.html',{'books':books,'form':form})

def update_data(request, id):
    if request.method == "POST":
        pi = Books.objects.get(pk=id)
        fm = BooksForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
        data = Books.objects.all()
    else:
        pi = Books.objects.get(pk=id)
        fm = BooksForm(instance=pi)
    return render(request,'books/home.html',{'form':fm} )

def deletedata(request,id):
    if request.method == "POST":
        pi = Books.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")

