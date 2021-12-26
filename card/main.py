# Do all data extracting here 
from mypackage.utility import getData

""" async.art """
"https://async-2.appspot.com/arts?page=1&count=12&artType=visual&sortBy=creationDate&sortDirection=-1"

getData(
    url = "https://async-2.appspot.com/arts?page={}&count=12&artType=visual&sortBy=creationDate&sortDirection=-1",
    header = """ 
    accept: */*
    accept-encoding: gzip, deflate, br
    accept-language: en-US,en;q=0.9
    if-none-match: W/"28-pj4ERw7enojeSLPdAUvHFFSLGr0"
    origin: https://async.art
    referer: https://async.art/
    sec-fetch-dest: empty
    sec-fetch-mode: cors
    sec-fetch-site: cross-site
    sec-gpc: 1
    user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36
                """,
    page_starting=1, 
    page_ending=3,
    page_data_total=5, 
    pera_api='market', 
    title='title',
    prefix='https://res.cloudinary.com/asynchronous-art-inc/image/upload/w_800,h_800,c_thumb,q_70,f_auto/',
    img='imagePath'
)