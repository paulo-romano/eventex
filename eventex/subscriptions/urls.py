from django.conf.urls import url
from eventex.subscriptions.views import subscribe, detail

urlpatterns = [
    url(r'^inscricao/$', subscribe, name='new'),
    url(r'^inscricao/(\d+)/$', detail, name='detail'),
]
