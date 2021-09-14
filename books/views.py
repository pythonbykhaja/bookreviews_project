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
    try:
        name = request.GET.get('name')
        email = request.GET.get('email')
        website = request.GET.get('website')
        Publisher.objects.create(name=name, email=email, website=website)
    except Exception as e:
        return HttpResponse(f"Couldnot insert record {e}")
    return HttpResponse("Record Inserted successfully")

