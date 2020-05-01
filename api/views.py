from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
import importlib
import os
import json

# Create your views here.


class UploadView(View):

    def get(self, request):
        print(request)
        hwk = importlib.machinery.SourceFileLoader('hwks1', 'hwks/hwks1.py').load_module()
        return HttpResponse(hwk.run())
    
    def post(self, request):
        try:
            req = json.loads(request.body)
            hwk = importlib.machinery.SourceFileLoader('hwk', 'hwks/{}'.format(req['hwkID'])).load_module()
            res = hwk.run(req['hwkContent'])
            print(res)
            return JsonResponse({'response': res})
        except Exception as e:
            print(e)
            return JsonResponse({'response': str(e)})
        

class HwkView(View):
    def get(self, request):
        filenameListIter = os.listdir('hwks')
        filenameList = [filename for filename in filenameListIter if filename != '__init__.py' and filename[-3:] == '.py']
        filenameDict = {'filename': filenameList}
        return JsonResponse(filenameDict)



