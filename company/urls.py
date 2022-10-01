from django.urls import path
from . import views


urlpatterns = [
    path("accessibility_statement/", views.AccessibilityStatement.as_view(), name="accessibility_statement",),
]