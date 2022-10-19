from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm


class AccessibilityStatement(CreateView):
    """
    Displays Accessibility Statement page.
    gets : requested template by name
    returns : rendered view of the html template
    """
    template_name = 'accessibility_statement.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class CopyrightStatement(CreateView):
    """
    Displays Copyright Statement page.
    gets : requested template by name
    returns : rendered view of the html template
    """
    template_name = 'copyright_statement.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class TermsAndConditions(CreateView):
    """
    Displays Terms and Conditions page.
    gets : requested template by name
    returns : rendered view of the html template
    """
    template_name = 'terms_and_conditions.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class Sustainability(CreateView):
    """
    Displays Sustainability page.
    gets : requested template by name
    returns : rendered view of the html template
    """
    template_name = 'sustainability.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class Faqs(CreateView):
    """
    Displays Sustainability page.
    gets : requested template by name
    returns : rendered view of the html template
    """
    template_name = 'faqs.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class OurStory(CreateView):
    """
    Displays Sustainability page.
    gets : requested template by name
    returns : rendered view of the html template
    """
    template_name = 'our_story.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


def contact(request, *args, **kwargs):
    """
    Displays Contact Us page form.
    Uses Post method to send contact form.
    Validation checks performed on input before saving.
    Email sent externally to TCC Gmail.
    Retains user on same page after commenting.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            subject = form.cleaned_data['subject'],
            message = form.cleaned_data['message'],
            form.save()
           
            # send mail combining field forms
            send_mail({subject}, f'{name}, {email}, {message}',
                      settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],
                      fail_silently=False)
            messages.success(
                request, 'Thank you for contacting us \
                - we will reply within 24 hours!')
           
            # redirect to home page
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Something went wrong with your submission.\
                Please try again.'
            )
    # blank form created if any other method is used
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})