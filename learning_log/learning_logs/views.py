from django.shortcuts import render

# Create your views here.
def index(request):
    """learning_logs App的主页"""
    return render(request, 'learning_logs/index.html')
