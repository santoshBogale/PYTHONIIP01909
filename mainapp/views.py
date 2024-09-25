from django.shortcuts import render
from .forms import UserForm
from .models import UserSubmission  # Import the model
import datetime
import random

def index(request):
    # Dynamic content
    current_datetime = datetime.datetime.now()
    quotes = [
        "The best way to predict the future is to invent it.",
        "Life is what happens when you’re busy making other plans.",
        "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
        "Success usually comes to those who are too busy to be looking for it."
    ]
    random_quote = random.choice(quotes)

    # Handle form submission
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            # Save form data to the database
            UserSubmission.objects.create(name=name, email=email)
            
            return render(request, 'index.html', {
                'current_datetime': current_datetime,
                'random_quote': random_quote,
                'name': name,  # Pass user data back to the template
                'email': email
            })
    else:
        form = UserForm()
    
    return render(request, 'index.html', {
        'current_datetime': current_datetime,
        'random_quote': random_quote,
        'form': form
    })
def submissions_list(request):
    # Retrieve all stored submissions from the database
    submissions = UserSubmission.objects.all().order_by('-submitted_at')
    
    return render(request, 'submissions_list.html', {
        'submissions': submissions
    })


