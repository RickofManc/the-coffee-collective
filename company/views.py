from django.shortcuts import render
from django.views.generic import CreateView


class AccessibilityStatement(CreateView):
    """
    Displays Accessibility Statement page.
    gets : requested template by name
    returns : rendered view of the html template
    """
    template_name = "accessibility_statement.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class CopyrightStatement(CreateView):
    """
    Displays Copyright Statement page.
    gets : requested template by name
    returns : rendered view of the html template
    """
    template_name = "copyright_statement.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class TermsAndConditions(CreateView):
    """
    Displays Terms and Conditions page.
    gets : requested template by name
    returns : rendered view of the html template
    """
    template_name = "terms_and_conditions.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
