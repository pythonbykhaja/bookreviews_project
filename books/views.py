from django.shortcuts import render
from django.http import HttpResponse
from books.models import Publisher

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
    print(request)
    return HttpResponse('Testing')

