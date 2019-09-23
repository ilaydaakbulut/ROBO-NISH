from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from robonish.views import index_view

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('robonish/', include('robonish.urls', namespace="robonish")),
    path('', view=index_view, name='index_view'),
    #path('', TemplateView.as_view(template_name='index.html'), name='home'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)