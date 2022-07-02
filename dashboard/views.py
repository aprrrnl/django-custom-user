from django.shortcuts import render

def dashboard(request):

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'dashboard.html', context=context)