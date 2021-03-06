# Django Oscar Portation

This is an application for django oscar products import/export. Import/export is processed into xlsx files.


# Getting Started

1. Install oscar-portation with `pip install oscar-portation`

2. Add `portation` to `INSTALLED_APPS`

3. Next, you should to fork oscar core `dashboard` app to your folder with apps:

	`./manage.py oscar_fork_app dashboard shop`

4. Then add `shop.dashboard` to installed apps, like:
```
	INSTALLED_APPS = [
		...
	    'portation',
	] + get_core_apps(
	    ['shop.dashboard']
	)
```
5. Create `app.py` file inside the `shop.dashboard` folder.

6. Paste code for processing urls:

```
	from django.conf.urls import url
	from oscar.apps.dashboard.app import (
	    DashboardApplication as CoreDashboardApplication)

	from portation.app import application


	class DashboardApplication(CoreDashboardApplication):
	    portation_app = application

	    def get_urls(self):
	        processed_urls = super(DashboardApplication, self).get_urls()
	        urls = [
	            url(r'^portation/', self.portation_app.urls),
	        ]
	        return processed_urls + self.post_process_urls(urls)


	application = DashboardApplication()

```

7. Hooray! Now you can visit `/dashboard/portation/import/` and `/dashboard/portation/export/` to try it.

8. Optiaonally, you can add menu items:

```
	OSCAR_DASHBOARD_NAVIGATION += [
	    {
	        'label': _('Import/export'),
	        'icon': 'icon-refresh',
	        'children': [
	            {
	                'label': _('Import'),
	                'url_name': 'dashboard:portation-import',
	                'access_fn':
	                    lambda user, url_name, url_args, url_kwargs: user.is_staff,
	            },
	            {
	                'label': _('Export'),
	                'url_name': 'dashboard:portation-export',
	                'access_fn':
	                    lambda user, url_name, url_args, url_kwargs: user.is_staff,
	            },
	        ],
	    },
	]
```

# Current Version 
Beta

# Contributing

Please feel free to send your issues and pull requests.

# Lisense
BSD License
