# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Games(models.Model):

    #__Games_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    number of players = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)

    #__Games_FIELDS__END

    class Meta:
        verbose_name        = _("Games")
        verbose_name_plural = _("Games")


class Match(models.Model):

    #__Match_FIELDS__
    number of players = models.IntegerField(null=True, blank=True)
    winner = models.TextField(max_length=255, null=True, blank=True)
    date of the match = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Match_FIELDS__END

    class Meta:
        verbose_name        = _("Match")
        verbose_name_plural = _("Match")



#__MODELS__END
