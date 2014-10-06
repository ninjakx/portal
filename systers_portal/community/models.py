from django.db import models

from common.models import Post
from users.models import SystersUser


class Community(models.Model):
    """Model to represent Systers community or subcommunity"""
    name = models.CharField(max_length=255, verbose_name="Name")
    slug = models.SlugField(max_length=150, unique=True, verbose_name="Slug")
    order = models.IntegerField(unique=True, verbose_name="Order")
    email = models.EmailField(max_length=255, blank=True, verbose_name="Email")
    mailing_list = models.EmailField(max_length=255, blank=True,
                                     verbose_name="Mailing list")
    members = models.ManyToManyField(SystersUser, blank=True, null=True,
                                     related_name='communities',
                                     verbose_name="Members")
    community_admin = models.ForeignKey(SystersUser, related_name='community',
                                        verbose_name="Community admin")
    parent_community = models.ForeignKey('self', blank=True, null=True,
                                         verbose_name="Parent community")
    website = models.URLField(max_length=255, blank=True,
                              verbose_name="Website")
    facebook = models.URLField(max_length=255, blank=True,
                               verbose_name="Facebook")
    googleplus = models.URLField(max_length=255, blank=True,
                                 verbose_name="Google+")
    twitter = models.URLField(max_length=255, blank=True,
                              verbose_name="Twitter")

    class Meta:
        verbose_name_plural = "Communities"
        permissions = (
            ('add_community_systersuser', 'Add community Systers User'),
            ('change_community_systersuser', 'Change community Systers User'),
            ('delete_community_systersuser', 'Delete community Systers User'),
            ('add_community_news', 'Add community news'),
            ('change_community_news', 'Change community news'),
            ('delete_community_news', 'Delete community news'),
            ('add_community_resource', 'Add community resource'),
            ('change_community_resource', 'Change community resource'),
            ('delete_community_resource', 'Delete community resource'),
            ('add_community_page', 'Add community page'),
            ('change_community_page', 'Change community page'),
            ('delete_community_page', 'Delete community page'),
            ('approve_community_comment', 'Approve community comment'),
            ('delete_community_comment', 'Delete community comment'),
            ('approve_community_joinrequest', 'Approve community join '
                                              'request'),
        )

    def __unicode__(self):
        return self.name


class CommunityPage(Post):
    """Model to represent an arbitrary community page"""
    order = models.IntegerField(unique=True, verbose_name="Order")
    community = models.ForeignKey(Community, verbose_name="Community")


class JoinRequest(models.Model):
    """Model to represent a request to join a community by a user"""
    user = models.ForeignKey(SystersUser, related_name='created_by')
    approved_by = models.ForeignKey(SystersUser, blank=True, null=True,
                                    related_name='approved_by')
    community = models.ForeignKey(Community)
    date_created = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __unicode__(self):
        if self.is_approved:
            return "Join Request by {0} - approved".format(self.user)
        return "Join Request by {0} - not approved".format(self.user)