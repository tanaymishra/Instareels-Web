from django.shortcuts import render
from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
def home(request):
    return render(request,'index.html')
@csrf_exempt
def link(requests):
    try:
        url=requests.POST.get('url')
        # print(url)
        link=download(url,'some.mp4')
        return HttpResponse(link)
    except :
        return HttpResponse("Internel Server Error")
def download(url,params):
    import re
    from requests_html import HTMLSession
    try:
        params=str(params)
        verify=re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",url)
    except:
        return ValueError("Invalid params!")
    if __name__ == '__main__':
        # print(verify)
        pass
    if verify[0][0]==url:
        pass
    else:
        raise ValueError("Wrong url Supplied")
    try:
        try:

            session = HTMLSession()
            response = session.get(url).text
            print("try")
            final= re.findall(r'content="https://scontent-bom1-2.cdninstagram.com/v/(.*?)[\"\']',response)[-1]
            return 'https://scontent-bom1-2.cdninstagram.com/v/'+final
        except :
            session = HTMLSession()
            response = session.get(url).text
            print("except")
            final= re.findall(r'content="https://scontent-bom1-1.cdninstagram.com/v/(.*?)[\"\']',response)[-1]
            return 'https://scontent-bom1-2.cdninstagram.com/v/'+final
    except Exception as e:
        print(e)