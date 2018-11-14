from django.http import HttpResponse

def test_response(request):
    return HttpResponse('This is a test response.. Awesome')
