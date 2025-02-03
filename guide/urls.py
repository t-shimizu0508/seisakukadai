from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'seisakukadaiapp'

urlpatterns = [
		path('',views.IndexView.as_view(), name='index'),
		path('guide_detail/<int:pk>',views.GuideDetail.as_view(),name='guide_detail'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)