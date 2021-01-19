from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, BookShop

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def book(request):
    bookshop_list = BookShop.objects.all()
    return render(request, "books.html", {"bookshop_list": bookshop_list})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")

def add(request):
    return render(request, "add.html")

def change(request):
    return render(request, "change.html")

def delete(request):
    return render(request, "delete.html")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    title = form["book_title"]
    subtitle = form["book_subtitle"]
    description = form["book_description"]
    price = form["book_price"]
    genre = form["book_genre"]
    author = form["book_author"]
    year = form["book_year"]
    books = BookShop(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    books.save()
    return redirect(book)
    
def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)