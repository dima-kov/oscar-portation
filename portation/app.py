from django.conf.urls import url
from oscar.core.application import Application

from portation.views import ImportView, ExportView


class PortationDashboardApplication(Application):
    name = None
    default_permissions = ['is_staff', ]

    import_view = ImportView
    export_view = ExportView

    def get_urls(self):
        urls = [
            url(r'^import/$', self.import_view.as_view(),
                name='portation-import'),
            url(r'^export/$', self.export_view.as_view(),
                name='portation-export'),
        ]
        return self.post_process_urls(urls)


application = PortationDashboardApplication()
