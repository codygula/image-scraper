import re
import requests


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

get_image_URLs("https://login.yahoo.com/?.src=ym&lang=en-US&done=https%3A%2F%2Fmail.yahoo.com%2Fd%2Ffolders%2F1%3F.src%3Dfp")
