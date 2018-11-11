from django.conf.urls import url, include
from django.views.static import serve
from InhandDocs import settings
from apps.product_docs.views import *

app_name = 'product_docs'
urlpatterns = [

    # 文档列表
    url(r'^install/doc/list/$', InstallDocListView.as_view(), name='install_doc_list'),

    # 文档详情
    url(r'^install/doc/detail/(?P<doc_id>\d+)/$', InstallDocDetailView.as_view(), name='install_doc_detail'),

    # 添加文档
    url(r'^install/doc/add/$', AddInstallDocView.as_view(), name='add_install_doc'),

    # 管理文档
    url(r'^install/doc/delete/$', ManaInstallDocView.as_view(), name='mana_install_doc'),

    # 修改文档
    url(r'^install/doc/change/(?P<doc_id>\d+)/$', ChangeInstallDocView.as_view(), name='change_install_doc'),
]
