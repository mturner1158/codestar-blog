from django.shortcuts import render
from .models import About
from .forms import CollaborateForm


# Create your views here.

def about_detail(request):
    """
    Display first object of about table.

    **Context**

    ``about``
        Latest about entry`.

    **Template:**

    :template:`about/about.html`
    """

    queryset = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": queryset,
         "collaborate_form": collaborate_form},
    )