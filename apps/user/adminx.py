import xadmin
from xadmin import views

__author__ = 'maxing'
__date__ = '2018/11/20 10:44'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "博客后台管理"
    site_footer = "个人博客"
    menu_style = "accordion"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)