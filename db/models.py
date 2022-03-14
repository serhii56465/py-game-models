from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race,
                             on_delete=models.SET_NULL,
                             null=True)


class Guild(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    bio = models.CharField(max_length=255, blank=True)
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild,
                              on_delete=models.SET_NULL,
                              null=True)
    create_at = models.DateTimeField(auto_now=True)
