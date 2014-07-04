from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user=models.ForeignKey(User,unique=True)
    arguments=models.ManyToManyField('Argument',blank=True,null=True)
    positiveCount=models.PositiveIntegerField(default=0)
    negativeCount=models.PositiveIntegerField(default=0)
    neutralCount=models.PositiveIntegerField(default=0)
    #TODO : Fix this issue (It does not display the field in admin,however it displays when you select the creator)
    def __unicode__(self):
        return  str(self.user)


class News(models.Model):
    title=models.CharField(max_length=150)
    url=models.URLField()
    date=models.DateTimeField()
    creator=models.ForeignKey('UserProfile')
    def __unicode__(self):
        return self.title

class Argument(models.Model):
    #Users can enter Arguments with Positive,Negative or Neutral opinions.
    OPINION=(
        ('P','Positive')
        ,('N','Negative')
        ,('NE','Neutral'),)
    opinion=models.CharField(max_length=2,choices=OPINION)
    content=models.TextField();
    news=models.ForeignKey('News')

    date=models.DateTimeField()
    count=models.PositiveIntegerField(default=0)
#It will have a one to one relationship with the User in Django auth






