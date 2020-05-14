import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from .models import Search


BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/bbb?query={}'     #source url for searching
BASE_IMG_URL = 'https://images.craigslist.org/{}_300x300.jpg'                     #source url for image

def codedadies_home(request):
    return render(request, 'my_app/base.html', {})            #create home view


def new_search(request):
    search = request.POST.get('search')
    Search.objects.create(search=search)                               # create data
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus((search)))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')                 # definition of the Soup Data
    post_listings = soup.find_all('li', {'class': 'result-row'})       # creating list of data soup


    final_posting  = []

    #a=1

    for post in post_listings:
        post_title = post.find(class_ = 'result-title').text                        # title of searching in forloop
        post_url = post.find('a').get('href')                                       # url of searching in forloop



        if post.find(class_='result-price'):                             # if You find price then create veriable
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'No Price'                                      # else veriable as string ""


        if post.find(class_='result-image gallery'):                  # if Searching have foto create veriable with url
            IMG_ID = post.find(class_='result-image').get('data-ids').split(',')[0][2:]
            BASE_LAST_URL = BASE_IMG_URL.format(IMG_ID)
        else:
            BASE_LAST_URL = 'https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/13001524/American-Staffordshire-Terrier-MP.jpg'

        #SECOND WAY

        # a=a+1
        # response_2 = requests.get(post_url)
        # data_2 = response_2.text
        # soup_2 = BeautifulSoup(data_2, features='html.parser')
        #
        # if soup_2.find_all('div', {'class': 'swipe-wrap'}):
        #     post_pic = soup_2.find('img').get('src')
        # else:
        #     post_pic = 'https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/13001524/American-Staffordshire-Terrier-MP.jpg'
        #
        # if a==15:
        #     break

        final_posting.append((post_title, post_url,post_price, BASE_LAST_URL))#, post_pic))



    stuff_for_frontend = {
        'search': search,
        'final_posting': final_posting,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend )