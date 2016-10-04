import os
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

# 此为图片下载的根目录
download_path = '/Users/liuheng/devprojects/python/download/'

# 创建指定路径的文件夹，并返回创建的路径
def create_download_file(download_file_name):
    dir_path = os.path.join(download_path, download_file_name)
    os.mkdir(dir_path)
    return dir_path

# 得到页中的所有img地址
def get_page_img(href, path):
    imgNum = 0
    html = urlopen(href).read()
    bsObj = BeautifulSoup(html, 'html.parser')
    divList = bsObj.findAll("div", {"class": "il_img"})
    for div in divList:
        imgNum = imgNum + 1
        img = div.find('img')
        url = img['src']
        print(url)
        img_path = os.path.join(path, str(imgNum) + '.png')
        urlretrieve(url, img_path)

    print('--------------------------------')


# 首先遍历所有的指向新页面的标签，然后调用get_page_img方法进行下载
main_page_url = 'http://www.ivsky.com'
main_html = urlopen(main_page_url).read()
main_bs = BeautifulSoup(main_html, 'html.parser')
href_div_list = main_bs.findAll('div', {'class': 'syl_pic'}, limit=2)

for div in href_div_list:
    href = div.find('a')
    title = href.attrs['title']
    img_download_path = create_download_file(title)
    href_link = href.attrs['href']
    get_page_img(main_page_url + href_link, img_download_path)
