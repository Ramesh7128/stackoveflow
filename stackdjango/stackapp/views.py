from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
import urllib2
import json
import requests
from django.core import serializers



# Create your views here.
def index(request):
    context = {}
    child1 = []
    url = "https://api.stackexchange.com/2.2/users/2545197%3B787980/questions?order=desc&sort=activity&site=stackoverflow"
    response = requests.get(url)
    childict = {}
    data = response.json()
    # print data

    for key, value in data.items():
        if key == "items":
            # child1.append({"owner" : val[0]['owner']})
            for val in value:
                user_quest = val['owner']['display_name']
                for test in value:
                    if test['owner']['display_name'] == user_quest:
                        child1.append(test)
                    else:
                        break
                print child1
                print "------------------------------------------------------------"
                child1 = []


            # for val in value:
            #     # print val
            #     if not any(d.get(val['owner']['display_name'], None) == val['owner'] for d in value1):
            #         value1.append({val['owner']['display_name'] : {val['owner']})
        # except:
        #     pass
        # print "key" , key
        # print "value" , val
    # print value1
    return HttpResponse(json.dumps(data), content_type='application/json')
    # return render(request, 'index.html', context)