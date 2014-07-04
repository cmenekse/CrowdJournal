from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CrowdJournalProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/singleNewsInformation$','CrowdJournal.views.getSingleNewsInformation'),
    url(r'^api/allNews$','CrowdJournal.views.getAllNews'),
    url(r'^api/userInfo$','CrowdJournal.views.getUserInformation'),
    url(r'^api/singleNewsArgumentWithType$','CrowdJournal.views.getSingleNewsArgumentsWithType'),
    url(r'^base$',TemplateView.as_view(template_name='base.html')),
    url(r'^index$',TemplateView.as_view(template_name='index.html'))
)
