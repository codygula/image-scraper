import re
import requests
import urllib.request
import uuid

def get_image_URLs(URL):
    
    links = []
    url_protocol = URL.split('/')[0]
    url_html = requests.get(URL).text

    Image_urls = re.findall(r'((http\:|https\:)?\/\/[^"\' ]*?\.(png|jpg))', url_html, flags=re.IGNORECASE | re.MULTILINE | re.UNICODE)

    for image in Image_urls:
        image_url = image[0]
        if not image_url.startswith(url_protocol):
            image_url = url_protocol+image_url
            links.append(image_url)
        else:
            links.append(image_url)

    print(links)

    return links

urlInput = input('ENTER URL: ')

url_list = get_image_URLs(urlInput)

for i in url_list:
    try:
        urllib.request.urlretrieve(i, f"DownloadImage{uuid.uuid4()}.png")
        print("downloading ", i)
    except:
        print("Error downloading ", i)