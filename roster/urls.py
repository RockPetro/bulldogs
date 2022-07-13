from django.urls import path
from . import views

# temporary, not production, but okay for testing
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('', views.playerRoster, name='index'),
    path('profile/<str:jersey>', views.playerProfile, name='profile')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
