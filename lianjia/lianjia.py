# -*- coding:utf8 -*-
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json


# 1.首先先获取页面的总长度
firstHtmlUrlOpen = urlopen('http://wh.fang.lianjia.com/loupan/pg1')
firstHtml = BeautifulSoup(firstHtmlUrlOpen.read().decode("utf8", 'ignore') , 'html.parser')
pageDiv = firstHtml.find('div', {'class': 'page-box house-lst-page-box'})
pageData = pageDiv.attrs['page-data']
pageDataDict = json.loads(pageData)
wholePageNum = pageDataDict['totalPage']
print('------------开始,页数为' + str(wholePageNum) + '------------')

# 2.开始循环抓取
for i in range(wholePageNum):
    pageNum = i+1
    print('\n\n\n------------爬取第' + str(pageNum) + '页开始------------')
    fangHtmlUrlOpen = urlopen('http://wh.fang.lianjia.com/loupan/pg' + str(pageNum) + '/')  # 测试抓取第1页   nlc_details
    fangHtmlStr = fangHtmlUrlOpen.read()
    fangHtmlStr = fangHtmlStr.decode("utf8", 'ignore')
    fangHtml = BeautifulSoup(fangHtmlStr, 'html.parser')
    fangDivList = fangHtml.findAll('div', {'class': 'info-panel'})
    for fangDiv in fangDivList:
        # 抓取楼盘名、楼盘位置、楼盘价格

        # 查找名称
        fangTextDiv = fangDiv.find('div', {'class': 'col-1'})
        fangNameNodeA = fangTextDiv.find('a')
        fangName = fangNameNodeA.get_text()

        # 查找地理位置
        fangLocationNode = fangTextDiv.find('span', {'class': 'region'})
        fangLocation = fangLocationNode.get_text()

        # 获取价格
        fangPriceNode = fangDiv.find('span', {'class': 'num'})
        if fangPriceNode is not None:
            fangPrice = fangPriceNode.get_text()
        else:
            fangPrice = '价格未知'

        print('    ' + fangName + '    ' + fangLocation + '    ' + fangPrice + '元/平')

    print('------------爬取第' + str(pageNum) + '页结束------------\n\n\n')
    # 休息2秒,防止被禁用
    time.sleep(2)



