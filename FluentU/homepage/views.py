from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'homepage.html')

def test1(request):
    return render(request,'leveltest.html')

def beg(request):
    return render(request,'beg.html')

def begtest(request):
    return render(request,'begtest.html')

def inter(request):
    return render(request,'inter.html')

def intertest(request):
    return render(request,'intertest.html')

def adv(request):
    return render(request,'adv.html')

def advtest(request):
    return render(request,'advtest.html')

from .models import Blog
def blog_view(request):
    # Fetch all blog objects from the database
    blogs = Blog.objects.all()
    # Pass the blogs variable to the template
    return render(request, 'blogs.html', {'blogs': blogs})



def write_blog_view(request):
    if request.method == 'POST':
        title = request.POST.get('blog-title')
        content = request.POST.get('blog-content')
        # Create a new Blog instance and save it to the database
        blog = Blog.objects.create(title=title, content=content)
        return redirect('blog')  # Redirect to the blog page after successful submission
    return render(request, 'writeblog.html')

def choice(request):
    return render(request,'choice.html')

def softskills(request):
    return render(request,'softcourse.html')

