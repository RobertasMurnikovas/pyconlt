from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from presenters.views.presenter import PresenterView, PresentersView

urlpatterns = [

    url(r'^speakers/(?P<pk>[0-9]+)/', PresenterView.as_view()),
    url(r'^speakers/$', PresentersView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
