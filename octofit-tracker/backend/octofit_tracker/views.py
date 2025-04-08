from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "url": "https://vigilant-spork-w4x5q9566q42gxxp-8000.app.github.dev"
    })