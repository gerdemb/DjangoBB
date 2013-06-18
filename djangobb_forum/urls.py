from django.conf.urls import *

from djangobb_forum import settings as forum_settings
from djangobb_forum import views as forum_views
from djangobb_forum.feeds import LastPosts, LastTopics, LastPostsOnForum, \
     LastPostsOnCategory, LastPostsOnTopic
from djangobb_forum.forms import EssentialsProfileForm, \
    PersonalProfileForm, MessagingProfileForm, PersonalityProfileForm, \
    DisplayProfileForm, PrivacyProfileForm, UploadAvatarForm


urlpatterns = patterns('',

    # Forum
    url('^$', forum_views.index, name='djangobb-index'),
    url('^(?P<forum_id>\d+)/$', forum_views.show_forum, name='djangobb-forum'),
    url('^moderate/(?P<forum_id>\d+)/$', forum_views.moderate, name='djangobb-moderate'),
    url('^search/$', forum_views.search, name='djangobb-search'),
    url('^misc/$', forum_views.misc, name='djangobb-misc'),

    # User
    url('^user/(?P<username>.*)/upload_avatar/$', forum_views.upload_avatar, {
        'form_class': UploadAvatarForm,
        'template': 'djangobb_forum/upload_avatar.html'
        }, name='djangobb-forum_profile_upload_avatar'),
    url('^user/(?P<username>.*)/privacy/$', forum_views.user, {
        'section': 'privacy',
        'form_class': PrivacyProfileForm,
        'template': 'djangobb_forum/profile/profile_privacy.html'
        }, name='djangobb-forum_profile_privacy'),
    url('^user/(?P<username>.*)/display/$', forum_views.user, {
        'section': 'display',
        'form_class': DisplayProfileForm,
        'template': 'djangobb_forum/profile/profile_display.html'
        }, name='djangobb-forum_profile_display'),
    url('^user/(?P<username>.*)/personality/$', forum_views.user, {
        'section': 'personality',
        'form_class': PersonalityProfileForm,
        'template': 'djangobb_forum/profile/profile_personality.html'
        }, name='djangobb-forum_profile_personality'),
    url('^user/(?P<username>.*)/messaging/$', forum_views.user, {
        'section': 'messaging',
        'form_class': MessagingProfileForm,
        'template': 'djangobb_forum/profile/profile_messaging.html'
        }, name='djangobb-forum_profile_messaging'),
    url('^user/(?P<username>.*)/personal/$', forum_views.user, {
        'section': 'personal',
        'form_class': PersonalProfileForm,
        'template': 'djangobb_forum/profile/profile_personal.html'
        }, name='djangobb-forum_profile_personal'),
    url('^user/(?P<username>.*)/essentials/$', forum_views.user, name='djangobb-forum_profile_essentials'),
    url('^user/(?P<username>.*)/$', forum_views.user, name='djangobb-forum_profile'),
    url('^users/$', forum_views.users, name='djangobb-forum_users'),

    # Topic
    url('^topic/(?P<topic_id>\d+)/$', forum_views.show_topic, name='djangobb-topic'),
    url('^(?P<forum_id>\d+)/topic/add/$', forum_views.add_topic, name='djangobb-add_topic'),
    url('^topic/(?P<topic_id>\d+)/delete_posts/$', forum_views.delete_posts, name='djangobb-delete_posts'),
    url('^topic/move/$', forum_views.move_topic, name='djangobb-move_topic'),
    url('^topic/(?P<topic_id>\d+)/stick_unstick/(?P<action>[s|u])/$', forum_views.stick_unstick_topic, name='djangobb-stick_unstick_topic'),
    url('^topic/(?P<topic_id>\d+)/open_close/(?P<action>[c|o])/$', forum_views.open_close_topic, name='djangobb-open_close_topic'),

    # Post
    url('^post/(?P<post_id>\d+)/$', forum_views.show_post, name='djangobb-post'),
    url('^post/(?P<post_id>\d+)/edit/$', forum_views.edit_post, name='djangobb-edit_post'),
    url('^post/(?P<post_id>\d+)/delete/$', forum_views.delete_post, name='djangobb-delete_post'),
    # Post preview
    url(r'^preview/$', forum_views.post_preview, name='djangobb-post_preview'),

    # Subscription
    url('^subscription/topic/(?P<topic_id>\d+)/delete/$', forum_views.delete_subscription, name='djangobb-forum_delete_subscription'),
    url('^subscription/topic/(?P<topic_id>\d+)/add/$', forum_views.add_subscription, name='djangobb-forum_add_subscription'),

    # Feeds
    url(r'^feeds/posts/$', LastPosts(), name='djangobb-forum_posts_feed'),
    url(r'^feeds/topics/$', LastTopics(), name='djangobb-forum_topics_feed'),
    url(r'^feeds/topic/(?P<topic_id>\d+)/$', LastPostsOnTopic(), name='djangobb-forum_topic_feed'),
    url(r'^feeds/forum/(?P<forum_id>\d+)/$', LastPostsOnForum(), name='djangobb-forum_forum_feed'),
    url(r'^feeds/category/(?P<category_id>\d+)/$', LastPostsOnCategory(), name='djangobb-forum_category_feed'),
)

### EXTENSIONS ###

# LOFI Extension
if (forum_settings.LOFI_SUPPORT):
    urlpatterns += patterns('',
        url('^lofi/$', forum_views.index, {'full':False}, name='djangobb-lofi_index'),
        url('^(?P<forum_id>\d+)/lofi/$', forum_views.show_forum, {'full':False}, name='djangobb-lofi_forum'),
        url('^topic/(?P<topic_id>\d+)/lofi/$', forum_views.show_topic, {'full':False}, name='djangobb-lofi_topic'),
    )

# REPUTATION Extension
if (forum_settings.REPUTATION_SUPPORT):
    urlpatterns += patterns('',
        url('^reputation/(?P<username>.*)/$', forum_views.reputation, name='djangobb-reputation'),
    )

# ATTACHMENT Extension
if (forum_settings.ATTACHMENT_SUPPORT):
    urlpatterns += patterns('',
        url('^attachment/(?P<hash>\w+)/$', forum_views.show_attachment, name='djangobb-forum_attachment'),
    )
