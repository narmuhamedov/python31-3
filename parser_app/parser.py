import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt

URL = "http://www.manascinema.com"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
}


# start parsing
@csrf_exempt
def get_html(url, params=""):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


# get data
@csrf_exempt
def get_data(html):
    soup = bs(html, "html.parser")
    items = soup.find_all("div", class_="short_movie_info")
    manas_flm = []
    for item in items:
        manas_flm.append(
            {
                "title_name": item.find("div", class_="m_title").get_text(),
                "title_url": URL + item.find("a").get("href"),
                "image": URL
                + item.find("div", class_="m_thumb").find("img").get("src"),
            }
        )
    return manas_flm


# endparsing
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        manas_flm2 = []
        for page in range(0, 1):
            html = get_html(f"http://www.manascinema.com/movies/", params=page)
            manas_flm2.extend(get_data(html.text))
            return manas_flm2
            #print(manas_flm2)

    else:
        raise Exception("Error in parser")


#parser()
