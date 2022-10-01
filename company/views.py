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