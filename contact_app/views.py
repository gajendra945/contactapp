from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
import logging

logger = logging.getLogger(__name__)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            message = form.cleaned_data['message']

            try:
                # Send email
                send_mail(
                    subject=f"New Contact from {name}",
                    message=f"Name: {name}\nEmail: {email}\nMobile: {mobile}\nMessage: {message}",
                    from_email=email,
                    recipient_list=['yuneeshh@gmail.com']
                )
                return render(request, 'contact_app/thank_you.html', {'name': name})
            except Exception as e:
                logger.error(f"Error sending email: {e}")
                return render(request, 'contact_app/contact.html', {'form': form, 'error': str(e)})
    else:
        form = ContactForm()
    return render(request, 'contact_app/contact.html', {'form': form})
