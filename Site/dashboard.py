"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'Sample_shop.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name
from filebrowser.sites import site

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Список таблиц базы данных'),
            collapsible=True,
            css_classes=('collapse closed',),
            column=1,
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('Администрирование'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=('django.contrib.*',),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent actions'),
            limit=10,
            collapsible=False,
            column=2,
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Управление медиа файлами'),
            column=2,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': 'filebrowser/browse/',
                    'external': False,
                },
            ]
        ))
        
        self.children.append(modules.ModelList(
            title='Настройки сайта',
            column=3,
            models=('Shop.models.Categories',)
        ))
