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
    str_query = ""
    if request.method=="POST":
        query = json.loads(request.body)
        for key, value in query.items()
            str_query = str_query + ";" + key
        context = {}
        child1 = []
        url = "https://api.stackexchange.com/2.2/users/" + str_query +  "/questions?order=desc&sort=activity&site=stackoverflow"
        response = requests.get(url)
        childict = {}
        data = response.json()
        # print data
        # print test.json
        li = []
        for key, value in data.items():
            if key == "items":
                for val in value:

                    # user_quest = val['owner']['display_name']
                    # for test in value:
                    if val['owner']['display_name'] not in li:
                        li.append(val['owner']['display_name'])

                    # print "----------------------"

        # print li
        # default_value = []
        # a = dict.fromkeys(li, default_value)
        a = {k: [] for k in li}
        # for k, v in a.items():
        for key, value in data.items():
            if key == "items":
                for val in value:
                    a[val['owner']['display_name']].append(val)
        print a
        d1 = dict(a.items()[len(a)/2:])
        d2 = dict(a.items()[:len(a)/2])
        return HttpResponse(json.dumps(a), content_type='application/json')