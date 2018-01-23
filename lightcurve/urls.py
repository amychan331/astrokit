from django.conf.urls import patterns, url

urlpatterns = patterns('lightcurve.views',
    url(r'^(?P<lightcurve_id>[0-9]+)/edit$', 'edit_lightcurve', name='edit_lightcurve'),
    url(r'^(?P<lightcurve_id>[0-9]+)/status$', 'get_status', name='get_status'),
)