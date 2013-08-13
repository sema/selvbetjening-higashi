from django.conf.urls import *
from django.conf import settings

from selvbetjening.portal.profile.views import profile_redirect
from selvbetjening.sadmin.base import sadmin

from selvbetjening.sadmin.members.models import MembersRootAdmin
from selvbetjening.sadmin.events.models import EventsRootAdmin
from selvbetjening.sadmin.mailcenter.models import MailcenterRootAdmin

sadmin.site.register('members', MembersRootAdmin)
sadmin.site.register('events', EventsRootAdmin)
sadmin.site.register('mailcenter', MailcenterRootAdmin)

from django.contrib.auth import views as auth_views

from selvbetjening.core.members.forms import ProfileFormWithoutSpecials

from selvbetjening.portal.quickregistration.views import register

from selvbetjening.portal.profile.forms import CrispySetPasswordForm, CrispyPasswordResetForm, LoginForm
from selvbetjening.portal.profile.views import profile_edit, password_change

from selvbetjening.portal.eventregistration.forms import EmptyForm
from selvbetjening.portal.eventregistration.views import list_events, information, signup, signoff, \
    change_options, view_invoice

urlpatterns = patterns('',
    url(r'^$', list_events, name='home'),

    url(r'^bliv-medlem/$', register,
        kwargs={
            'success_page': 'home'
        },
        name='quickregistration_register'),

    url(r'^events/(?P<event_id>[0-9]+)/$',
        information,
        name='eventregistration_information'),

    url(r'^events/(?P<event_id>[0-9]+)/tilmeld/$',
        signup,
        kwargs={
            'form_class': EmptyForm
        },
        name='eventregistration_signup'),

    url(r'^events/(?P<event_id>[0-9]+)/afmeld/$',
        signoff,
        name='eventregistration_signoff'),

    url(r'^events/(?P<event_id>[0-9]+)/tilvalg/$',
        change_options,
        name='eventregistration_change_options'),

    url(r'^events/(?P<event_id>[0-9]+)/status/$',
        view_invoice,
        name='eventregistration_status'),


    url(r'^profil/opdater/$', profile_edit,
        kwargs={
            'form_class': ProfileFormWithoutSpecials,
            'success_page': 'home'
        },
        name='members_editprofile'),

    url(r'^profil/logud/$', auth_views.logout,
        {'template_name': 'profile/logout.html',},
        name='members_logout'),

    url(r'^profil/skift-kodeord/$', password_change,
        kwargs={
            'post_change_redirect': 'home'
        },
        name='members_password_change'),

    url(r'^login/$', auth_views.login,
        {'template_name': 'profile/login.html', 'authentication_form': LoginForm},
        name='members_login'),

    url(r'^nulstil-kodeord/$', auth_views.password_reset,
        {'template_name':'profile/password_reset/password_reset.html',
         'password_reset_form': CrispyPasswordResetForm,
         'email_template_name': 'simpleregistration/password_reset_email.html',
         'subject_template_name': 'simpleregistration/password_reset_email_subject.txt'},
        name='auth_password_reset'),
    url(r'^nulstil-kodeord/email-sendt/$', auth_views.password_reset_done,
        {'template_name':'profile/password_reset/password_reset_done.html'},
        name='members_password_reset_done'),
    url(r'^nulstil-kodeord/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/', auth_views.password_reset_confirm,
        {'template_name':'profile/password_reset/password_reset_confirm.html',
         'set_password_form': CrispySetPasswordForm},
        name='auth_password_reset_confirm'),
    url(r'^nulstil-kodeord/reset/done/$', auth_views.password_reset_complete,
        {'template_name':'simpleregistration/password_reset_done.html'}),

    url(r'^nulstil-kodeord/$', auth_views.password_reset,
        {'template_name': 'profile/password_reset/password_reset.html',
         'password_reset_form': CrispyPasswordResetForm,
         'email_template_name': 'profile/password_reset/password_reset_email.html'},
        name='auth_password_reset'),
    url(r'^nulstil-kodeord/email-sendt/$', auth_views.password_reset_done,
        {'template_name': 'profile/password_reset/password_reset_done.html'},
        name='members_password_reset_done'),
    url(r'^nulstil-kodeord/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/', auth_views.password_reset_confirm,
        {'template_name': 'profile/password_reset/password_reset_confirm.html',
         'set_password_form': CrispySetPasswordForm},
        name='auth_password_reset_confirm'),
    url(r'^nulstil-kodeord/reset/done/$', auth_views.password_reset_complete,
        {'template_name': 'profile/password_reset/password_reset_complete.html'}),

    (r'^sadmin/', include(sadmin.site.urls))
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
