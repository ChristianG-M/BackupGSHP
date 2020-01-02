import urllib.request
import random


def downloader(image_url):
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name) + '.png'
    urllib.request.urlretrieve(image_url,full_file_name)


downloader(url)