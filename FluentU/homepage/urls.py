from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('leveltest',views.test1,name='test1'),
    path('beginner',views.beg,name='beg'),
    path('begtest',views.begtest,name='begtest'),
    path('inter',views.inter,name='inter'),
    path('intertest',views.intertest,name='intertest'),
    path('adv',views.adv,name='adv'),
    path('advtest',views.advtest,name='advtest'),
    path('blog',views.blog_view,name='blog'),
    path('writeblog/', views.write_blog_view, name='write_blog'),
    path('choice/',views.choice,name='choice'),
    path('choice/softskills',views.softskills,name='softskills'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

