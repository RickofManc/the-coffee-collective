from django.urls import path
from . import views


urlpatterns = [
    path("accessibility_statement/", views.AccessibilityStatement.as_view(), name="accessibility_statement",),
    path("copyright_statement/", views.CopyrightStatement.as_view(), name="copyright_statement",),
]