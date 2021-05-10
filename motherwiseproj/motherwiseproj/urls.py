from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from motherwise import views
from mothers.views import run_task

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^motherwise/', include('motherwise.urls')),
    url(r'^users/', include('mothers.urls')),
    url(r'^umobile/', include('usermobile.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^users', views.index, name='index'),
    url(r'^manager',views.admin,  name='admin'),
    url(r'^admin',views.admin,  name='admin'),
    url(r'^home',views.adminhome,  name='adminhome'),
    url(r'^torequestpwd',views.torequestpwd,  name='torequestpwd'),
    url(r'^logout',views.adminlogout,  name='adminlogout'),
    url(r'^signuppage',views.adminsignuppage,  name='adminsignuppage'),
    url(r'^loginpage',views.adminloginpage,  name='adminloginpage'),
    url(r'^signup',views.adminSignup,  name='adminSignup'),
    url(r'^login',views.adminLogin,  name='adminLogin'),
    url(r'^export_xlsx_member/$', views.export_xlsx_member, name='export_xlsx_member'),
    url(r'^import_view/member/$', views.import_view_member, name='import_view_member'),
    url(r'^import_member/$', views.import_member_data, name='import_member_data'),
    url(r'^add_member/$', views.add_member, name='add_member'),
    url(r'^delete_member/$', views.delete_member, name='delete_member'),
    url(r'^active_members/$', views.active_members, name='active_members'),
    url(r'^inactive_members/$', views.inactive_members, name='inactive_members'),
    url(r'^message_to_selected_members/$', views.message_to_selected_members, name='message_to_selected_members'),
    url(r'^to_page',views.to_page,  name='to_page'),
    url(r'^to_previous',views.to_previous,  name='to_previous'),
    url(r'^to_next',views.to_next,  name='to_next'),
    url(r'^do_cohort',views.do_cohort,  name='do_cohort'),
    url(r'^search_members',views.search_members,  name='search_members'),
    url(r'^account',views.admin_account,  name='admin_account'),
    url(r'^edit_account',views.edit_admin_account,  name='edit_admin_account'),
    url(r'^send_cohort_message',views.send_cohort_message,  name='send_cohort_message'),
    url(r'^switch_chat',views.admin_switch_chat,  name='admin_switch_chat'),
    url(r'^to_chat',views.admin_to_chat,  name='admin_to_chat'),
    url(r'^switch_to_cohort',views.admin_switch_to_cohort,  name='admin_switch_to_cohort'),
    url(r'^create_group',views.create_group,  name='create_group'),
    url(r'^message_to_group',views.message_to_group,  name='message_to_group'),
    url(r'^switch_group',views.switch_group,  name='switch_group'),
    url(r'^groups',views.get_groups,  name='get_groups'),
    url(r'^open_group_chat',views.open_group_chat,  name='open_group_chat'),
    url(r'^group_cohort_chat',views.group_cohort_chat,  name='group_cohort_chat'),
    url(r'^group_chat_message',views.group_chat_message,  name='group_chat_message'),
    url(r'^group_private_chat',views.group_private_chat,  name='group_private_chat'),
    url(r'^delcontact',views.admin_delete_contact,  name='admin_delete_contact'),
    url(r'^delgroup',views.admin_delete_group,  name='admin_delete_group'),
    url(r'^posts',views.to_posts,  name='to_posts'),
    url(r'^mineppppp',views.my_posts,  name='my_posts'),
    url(r'^create_post',views.create_post,  name='create_post'),
    url(r'^add_post_comment',views.add_post_comment,  name='add_post_comment'),
    url(r'^search_post',views.search_post,  name='search_post'),
    url(r'^filter',views.filter,  name='filter'),
    url(r'^like_post',views.like_post,  name='like_post'),
    url(r'^submit_comment',views.submit_comment,  name='submit_comment'),
    url(r'^delpost',views.delete_post,  name='delete_post'),
    url(r'^delcomment',views.delete_comment,  name='delete_comment'),
    url(r'^postdelpicture',views.delete_post_picture,  name='delete_post_picture'),
    url(r'^edit_post',views.edit_post,  name='edit_post'),
    url(r'^send_mail_forgotpassword',views.send_mail_forgotpassword,  name='send_mail_forgotpassword'),
    url(r'^resetpassword', views.resetpassword, name='resetpassword'),
    url(r'^rstpwd',views.admin_rstpwd,  name='admin_rstpwd'),
    url(r'^notifications',views.notifications,  name='notifications'),
    url(r'^sentnotis',views.sentnotis,  name='sentnotis'),
    url(r'^delnoti',views.delete_noti,  name='delete_noti'),
    url(r'^processnewmessage',views.processnewmessage,  name='processnewmessage'),
    url(r'^noti_search',views.notisearch,  name='notisearch'),
    url(r'^fffff',views.fffff,  name='fffff'),
    url(r'^videotest',views.videotest,  name='videotest'),
    url(r'^open_conference',views.open_conference,  name='open_conference'),
    url(r'^create_conference',views.create_conference,  name='create_conference'),
    url(r'^delconf',views.delete_conference,  name='delete_conference'),
    url(r'^conference_notify',views.conference_notify,  name='conference_notify'),
    url(r'^video_selected_members',views.video_selected_members,  name='video_selected_members'),
    url(r'^new_notis',views.new_notis,  name='new_notis'),
    url(r'^send_reply_message',views.send_reply_message,  name='send_reply_message'),
    url(r'^send_member_message',views.send_member_message,  name='send_member_message'),

    url(r'^to_conferences',views.to_conferences,  name='to_conferences'),
    url(r'^noti_detail',views.noti_detail,  name='noti_detail'),

    url(r'^notify_group_chat',views.notify_group_chat,  name='notify_group_chat'),
    url(r'^analytics',views.analytics,  name='analytics'),

    url(r'pushsend',views.sendfcmpush,  name='sendfcmpush'),

    ############# Landing page ###########################################################################################

    url(r'new',views.landing,  name='landing'),
    url(r'main',views.main,  name='main'),
    url(r'landingnotify',views.landing_notify,  name='landing_notify'),

    #################################

    url(r'^translate',views.open_translate,  name='open_translate'),
    url(r'^process_translate',views.process_translate,  name='process_translate'),

    url(r'^sms_send',views.sms_test,  name='sms_test'),
    url(r'^tttchange',views.change,  name='change'),

]

run_task(repeat=20,repeat_until=None)


urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns=format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









































