from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Card

from .utility import getData, getDataGpk

# Create your views here.

# def getData(url, header, page_starting, page_ending, page_data_total, pera_api, title, prefix, img):

class index(ListView):
    model = Card
    paginate_by = 4
    context_object_name = 'card'
    template_name = 'home/index.html'



def latest(request):

    getData(
    url = "https://async-2.appspot.com/arts?page={}&count=12&artType=visual&sortBy=creationDate&sortDirection=-1",
    header = {
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    },
    page_starting=1,
    page_ending=3,
    page_data_total=5,
    pera_api='market',
    title='title',
    prefix='https://res.cloudinary.com/asynchronous-art-inc/image/upload/w_800,h_800,c_thumb,q_70,f_auto/',
    img='imagePath'
    )

    return HttpResponse("Task Has Been Completed..")


""" portion.io"""
def latest2(request):
    getData(
        url = 'https://api.portion.io/api/v1/drops/search?artists=&chains=Ethereum&sortBy=newest&limit=36',
        header= 
        {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'  
        },
        page_starting=1, 
        page_ending=2,
        page_data_total= 30, 
        pera_api='Items',
        title='artName',
        prefix='https://s3.amazonaws.com/ipfs.cache.v3/',
        img='IPFShash' 
    )
    return HttpResponse("Task Has Been Completed..")


""" myth.market"""
# ||
## ==> https://gpk.market/market/
### ==> https://gpk.myth.market/api/listings?page=1&author=gpk.topps

def latest3(request):

    getDataGpk(
    url = 'https://gpk.myth.market/api/listings?page={}&author=gpk.topps',
    header= 
    { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'  
    },
    page_starting=1, 
    page_ending=3,
    page_data_total= 10, 
    pera_api='results',
    pera_api_1='mdata',
    title='name',
    prefix='https://ipfs.io/ipfs/',
    img='img' 
    )
    return HttpResponse("Task Has been completed ")
