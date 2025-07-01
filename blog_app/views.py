from django.shortcuts import render
from .models import Post  # Import your Post model
# Create your views here.
def post_list(request):
    posts = Post.objects.all()  # Assuming you have a Post model
    return render(request, 'post_list.html', {'posts': posts})  # context , dictionary to pass data to the template