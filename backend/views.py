from django.http import JsonResponse

# Create your views here.
def test(request):

    print("testing")
    data = {
        'name': 'test',
        'prupose': 'backend',
    }

    return JsonResponse(data)