import xadmin
from xadmin import views

########################################################################################################################
## 自建模块导入
########################################################################################################################
from apps.users.models import *


########################################################################################################################
## 注册部门到后台
########################################################################################################################
class UserDepartmentAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'add_time']


xadmin.site.register(UserDepartment, UserDepartmentAdmin)


########################################################################################################################
## 注册职位到后台
########################################################################################################################
class UserPositionAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'add_time']


xadmin.site.register(UserPosition, UserPositionAdmin)


class UserLoginRecordAdmin(object):
    list_display = ['user', 'agent', 'city', 'ip', 'add_time']
    search_fields = ['user', 'agent', 'city', 'ip']
    list_filter = ['user', 'add_time']


class BaseSetting(object):
    # 添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 全局配置，后台管理标题和页脚
    site_title = "Inhand文档管理系统"
    site_footer = "联系我：Vincent Loving you"
    # 菜单收缩
    menu_style = "accordion"
    # menu_style = "default"
    apps_icons = {"appname": "icon"}


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(UserLoginRecord, UserLoginRecordAdmin)
