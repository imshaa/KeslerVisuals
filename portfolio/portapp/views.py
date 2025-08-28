from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactMessage

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # 1️⃣ Save to database
        contact = ContactMessage(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()

        with open("messages.txt", "a", encoding="utf-8") as f:
            f.write(f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}\n---\n")

        return redirect("index")  # Refresh after submit
    
    return render(request, "index.html")

def graphic(request):
    return render(request, "graphicfiles.html") 


def figma(request):
    return render(request, "figmafiles.html")

def video(request):
    return render(request, "videofiles.html")