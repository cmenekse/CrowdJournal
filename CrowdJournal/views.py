from django.shortcuts import render_to_response
from django.template import RequestContext
from django.templatetags.static import static
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from CrowdJournal.models import News,Argument,UserProfile
from CrowdJournal.serializers import NewsSerializer,ArgumentSerializer,UserProfileSerializer


#it looks like it renders the given data to JSON Format
class JSONResponse(HttpResponse):    
    def __init__(self,data, **kwargs):
        content=JSONRenderer().render(data)
        kwargs['content_type'] = "application/json"
        super(JSONResponse,self).__init__(content,**kwargs)

#--------------------Get Calls-------------------------------
#POST Parameters= UserID: The id of the requested User
#RETURN information about a single user
def getUserInformation(request):
    if request.method=='POST':
        postedUserID=request.POST['userID']
        userID=UserProfile.objects.filter(userID=postedUserID)
        serializer=UserProfileSerializer(userID,many=False)
        return JSONResponse(serializer.data)

#POST Parameters= Empty
#RETURN all of the news
@csrf_exempt
def getAllNews(request):
    if request.method=='POST':
        allNews=News.objects.all()
        serializer=NewsSerializer(allNews,many=True)
        return JSONResponse(serializer.data)

#POST Parameters=NewsID:The id of the requested news
#RETURN: The arguments with the desired opinion
@csrf_exempt
def getSingleNewsArgumentsWithType(request):
    if request.method=='POST':
        postedNewsID = request.POST['newsID']
        postedOpinionType = request.POST['opinion']
        #Access to the single news instance than get all of its arguments
        singleNewsInstance= News.objects.get(pk=postedNewsID)
        filteredArgumentsByType = singleNewsInstance.argument_set.filter(opinion=postedOpinionType).order_by("-count")
        #filteredArgumentsByType=argumentsOfSingleNewsInstance.filter(opinion=postedOpinionType)
        serializer=ArgumentSerializer(filteredArgumentsByType,many=True)
        return JSONResponse(serializer.data);

#POST Parameters= NewsID:The id of the requested news
#RETURN: Information about a single news
@csrf_exempt
def getSingleNewsInformation(request):
    if request.method=='POST':
        postedNewsID=request.POST['newsID']
        singleNews=News.objects.filter(pk=postedNewsID)
        #TODO : Make sure what many=True does it is not clear in the documentation of Rest Framework
        serializer=NewsSerializer(singleNews,many=True)
        return JSONResponse(serializer.data)


            