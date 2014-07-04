from django.forms import widgets
from rest_framework import serializers
from CrowdJournal.models import News,Argument,UserProfile



class ArgumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Argument
        fields=('id','news','content')

#User ProfileSerializer should not be a class based view,
#users should probably not do the CRUD operations
class UserProfileSerializer(serializers.ModelSerializer):
    arguments=ArgumentSerializer(serializers.ModelSerializer)
    class Meta:
        model=UserProfile
        fields=('id',)

class NewsSerializer(serializers.ModelSerializer):
    creator	=UserProfileSerializer(serializers.ModelSerializer)
    class Meta:
        model=News
        fields=('id','creator')




