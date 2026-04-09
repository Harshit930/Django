from django.shortcuts import redirect

class MyMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        print("Before View (Request)")

        response = self.get_response(request)

        print("After View (Response)")

        return response
    


class LoginCheckMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        if not request.user.is_authenticated:

            if request.path != '/login/':

                return redirect('/login/')

        response = self.get_response(request)

        return response