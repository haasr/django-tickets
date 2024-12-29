# -*- coding: utf-8 -*-

from django.urls import path, re_path, include
from django.contrib import admin

import main.views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# to include media files at the end
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Login and settings pages
    re_path(r'^$', LoginView.as_view(), name='login'),

    re_path(r'^logout/$', main.views.log_out, name='logout'),

    re_path(r'^settings/$',
        login_required(main.views.usersettings_update_view),
        name='user-settings'),

    # Django admin
    re_path(r'^admin/', admin.site.urls),  # No include() needed

    # create new ticket
    re_path(r'^ticket/new/$',
        login_required(main.views.ticket_create_view),
        name='ticket_new'),

    # edit ticket
    re_path(r'^ticket/edit/(?P<pk>\d+)/$',
        login_required(main.views.ticket_edit_view),
        name='ticket_edit'),

    # view ticket
    re_path(r'^ticket/(?P<pk>\d+)/$',
        login_required(main.views.ticket_detail_view),
        name='ticket_detail'),

    # create new followup
    re_path(r'^followup/new/$',
        login_required(main.views.followup_create_view),
        name='followup_new'),

    # edit followup
    re_path(r'^followup/edit/(?P<pk>\d+)/$',
        login_required(main.views.followup_edit_view),
        name='followup_edit'),

    # create new attachment
    re_path(r'^attachment/new/$',
        login_required(main.views.attachment_create_view),
        name='attachment_new'),

    # ticket overviews
    re_path(r'^inbox/$',
        login_required(main.views.inbox_view),
        name='inbox'),

    re_path(r'^my-tickets/$',
        login_required(main.views.my_tickets_view),
        name='my-tickets'),

    re_path(r'^all-tickets/$',
        login_required(main.views.all_tickets_view),
        name='all-tickets'),

    re_path(r'^archive/$',
        login_required(main.views.archive_view),
        name='archive'),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
