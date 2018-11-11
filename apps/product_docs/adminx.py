import xadmin

from apps.product_docs.models import *


class InstallDocTagAdmin(object):
    list_display = ['name', 'add_time']


xadmin.site.register(InstallDocTag, InstallDocTagAdmin)


class InstallDocAdmin(object):
    list_display = ['doc_title', 'doc_tag', 'add_time']


xadmin.site.register(InstallDoc, InstallDocAdmin)
