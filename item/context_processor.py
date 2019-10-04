from .models import AboutUs

def footer(request, *args, **kwargs):
    about = AboutUs.objects.last()
    context = {'about': about}
    return context