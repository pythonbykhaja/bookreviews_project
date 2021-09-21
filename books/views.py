from django.shortcuts import render, redirect
from django.http import HttpResponse
from books.models import Publisher,Book


# Create your views here.

def publisher(request):
    """
    Publisher view
    """
    return render(request, 'books/publisher.html')


def create_publisher(request):
    """
    This view will create the publisher in the database
    """
    try:
        name = request.GET.get('name')
        email = request.GET.get('email')
        website = request.GET.get('website')
        Publisher.objects.create(name=name, email=email, website=website)
    except Exception as e:
        return HttpResponse(f"Couldnot insert record {e}")
    return render(request, 'books/publisher_record_created.html',
                  context={'message': 'successfully inserted publisher record'})


def get_all_publishers(request):
    """
    This view will return all the publishers
    """
    publishers = Publisher.objects.all()
    context = {
        'publishers': publishers
    }
    return render(request, 'books/publishers.html', context=context)


def get_all_books(request):
    """
    This view is to return all the books
    """
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/books.html', context=context)


def add_book(request):
    publishers = [publisher.name for publisher in Publisher.objects.all()]
    context = {
        'publishers': publishers
    }
    return render(request, 'books/add_book.html', context=context)

def create_book(request):
    """
    This method will submit the books to database
    """
    publisher_name = request.POST.get('publisher')
    publisher = Publisher.objects.get(name=publisher_name)
    title = request.POST.get('title')
    publication_date = request.POST.get('publication_date')
    Book.objects.create(title=title, publication_date=publication_date, publisher=publisher)

    return HttpResponse('Created')
