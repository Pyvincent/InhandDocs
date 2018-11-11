"""InhandDocs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import xadmin
from django.views.static import serve
from InhandDocs import settings

urlpatterns = [
    path(r'xadmin/', xadmin.site.urls),
    # media 配置
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # 用户url入口
    path(r'', include('apps.users.urls', namespace='user')),
    # CKeditor上传图片
    # url(r'^uploadimg/', upload_image),
    # 产品文档url入口
    path(r'product_docs', include('apps.product_docs.urls', namespace='product_docs')),
    # 验证码
    url(r'^captcha/', include('captcha.urls')),
]
