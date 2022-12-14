"""tcc URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from .views import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('company/', include('company.urls')),
    path('favicon.ico',
         RedirectView.as_view(
            url=staticfiles_storage.url('images/favicon.ico')
            ),),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# override the standard error handlers
handler403 = 'tcc.views.handler403'
handler404 = 'tcc.views.handler404'
handler405 = 'tcc.views.handler405'
handler500 = 'tcc.views.handler500'
