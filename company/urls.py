from django.urls import path
from . import views


urlpatterns = [
    path('accessibility_statement/', views.AccessibilityStatement.as_view(),
         name='accessibility_statement',),
    path('copyright_statement/', views.CopyrightStatement.as_view(),
         name='copyright_statement',),
    path('terms_and_conditions/', views.TermsAndConditions.as_view(),
         name='terms_and_conditions',),
    path('sustainability/', views.Sustainability.as_view(),
         name='sustainability',),
    path('faqs/', views.Faqs.as_view(), name='faqs',),
    path('our_story/', views.OurStory.as_view(), name='our_story',),
    path('health_benefits/', views.HealthBenefits.as_view(), name='health_benefits',),
    path('', views.contact, name='contact'),
]
