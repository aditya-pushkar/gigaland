import requests
import json

from django.http import HttpResponse

from .models import Card


def get_headers(s, sep=': ', strip_cookie=True, strip_cl=True, strip_headers: list = []) -> dict():
    d = dict()
    for kv in s.split('\n'):
        kv = kv.strip()
        if kv and sep in kv:
            v=''
            k = kv.split(sep)[0]
            if len(kv.split(sep)) == 1:
                v = ''
            else:
                v = kv.split(sep)[1]
            if v == '\'\'':
                v =''
            # v = kv.split(sep)[1]
            if strip_cookie and k.lower() == 'cookie': continue
            if strip_cl and k.lower() == 'content-length': continue
            if k in strip_headers: continue
            d[k] = v
    return d


# # Give url with f string and formating braces {} in equal to with page eg: page={pageNo}
# # page_starting = page no. where we want to get started from 0  or 1
# # page_ending  =page no. where we want to stop 
# # page_data_total = How much data we want from single page
# # pera_api/perameter api = It is firt json obj from Api where we get img and title affter loop through it 

def getData(url, header, page_starting, page_ending, page_data_total, pera_api, title, prefix, img):
    
    # headers = get_headers(header)
    # print(f"The Header is {headers}")
    try:

        for pageNo in range(page_starting, page_ending+1):

            
            url_new = url.format(pageNo)
            response = requests.get(url_new, headers=header)

            # Getting data from singlePage / eachPage

            for num in range(page_data_total):
                
                json_response = response.json()[pera_api][num]
                title_new = json_response[title]
                img_new = prefix + json_response[img]
                print(title_new)
                print(img_new)

                cc = Card(img=img_new, title=title_new)
                cc.save()
        
        return HttpResponse(" fetching all data in completed....")


    except Exception as e:

        print(f" Faild:: {e}")
        

""" for ==> https://gpk.market/market/ """
def getDataGpk(url, header, page_starting, page_ending, page_data_total, pera_api, pera_api_1, title, prefix, img):
    
    # headers = get_headers(header)
    # print(f"The Header is {headers}")

    for pageNo in range(page_starting, page_ending+1):

        url_new = url.format(pageNo)
        response = requests.get(url_new, headers=header)

        # Getting data from singlePage / eachPage

        for num in range(page_data_total):

            try:
                json_response = response.json()[pera_api][num][pera_api_1]
                title_new = json_response[title]
                img_new = prefix + json_response[img]
                print(title_new)
                print(img_new)

                cc = Card(img=img_new, title=title_new)
                cc.save()
            except Exception as e:
	            print(f" Failed {e} ")
           



if __name__ == '__main__':
    get_headers()
    getData()
    getDataGpk()