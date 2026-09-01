from django.shortcuts import render
from django.contrib import messages
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

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavor to respond within 2 working days.")

    queryset = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": queryset,
         "collaborate_form": collaborate_form},
    )