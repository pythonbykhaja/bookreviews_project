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
    name =string(request.Get['name'])
    website=string(request.Get['email'])
    email = string(request.Get['email'])
    response_text=f"<p>name:{name}<br/> website:{website}<br/> email={email}<p>"
    return HttpResponse('response_text')

