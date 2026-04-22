from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # 这行告诉 Django：首页的规则去 blog/urls.py 里找
]