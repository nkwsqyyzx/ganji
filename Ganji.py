# -*- coding: UTF8 -*-
from HtmlCache import HtmlCache
from bs4 import BeautifulSoup
import time

cache = HtmlCache(basepath='bin/')

from bs4 import BeautifulSoup
def GetMatchesLink(link='/fang3/tuiguang-10093771.htm'):
    # 从每个联赛中获取下一轮比赛对阵链接
    url = 'http://bj.ganji.com{0}'.format(link)
    html, cached = cache.getContentWithAgent(url=url, encoding='utf8', timeout=7 * 24 * 60 * 60)
    soup = BeautifulSoup(html)

    print('======================================================================')
    # 发布时间
    lis = soup.find('ul', {'class':'title-info-l clearfix'}).findAll('li')
    print(lis[0].get_text().replace('\n', '').replace('  ', ' '))

    # 基本信息
    lis = soup.find('ul', {'class':'basic-info-ul'}).findAll('li')
    if len(lis) < 5:
        return
    print('详细信息:', url)
    print(lis[0].get_text().replace('\n', '').replace(' ', ''))
    print(lis[1].get_text().replace('\n', '').replace(' ', ''))
    print(lis[2].get_text().replace('\n', '').replace(' ', ''))
    print(lis[3].get_text().replace('\n', '').replace(' ', ''))
    print('小区:', lis[4].find('div').findAll('a')[0].get_text().replace('\n', '').replace(' ', ''))

    lis = soup.findAll('div', {'class':'person-name'})
    print('联系人:', lis[0].get_text().replace('\n', '').replace(' ', ''))

    lis = soup.findAll('p', {'class':'company-name'})
    if len(lis) < 1:
        print('公司: 未知,可能为房东,也可能是转租')
    else:
        print('公司:', lis[0].get_text().replace('\n', '').replace(' ', ''))

    lis = soup.find('div', {'class':'basic-info-contact'}).findAll('em')
    print('电话:', lis[0].get_text().replace('\n', '').replace(' ', ''))

def Get小区房子():
    urlList = []
    # 科育小区
    urlList.append('http://bj.ganji.com/xiaoqu/keyushequ/hezufang/')
    urlList.append('http://bj.ganji.com/xiaoqu/keyushequ/hezufang/f20/')
    urlList.append('http://bj.ganji.com/xiaoqu/keyushequ/hezufang/f40/')
    urlList.append('http://bj.ganji.com/xiaoqu/keyushequ/hezufang/f60/')
    # 科源社区
    urlList.append('http://bj.ganji.com/xiaoqu/keyuanshequ/hezufang/')

    # 手动转码
    # 海淀路小区
    urlList.append('http://bj.ganji.com/fang3/_%E6%B5%B7%E6%B7%80%E8%B7%AF%E5%B0%8F%E5%8C%BA/')
    # 海淀路社区
    urlList.append('http://bj.ganji.com/fang3/_%E6%B5%B7%E6%B7%80%E8%B7%AF%E7%A4%BE%E5%8C%BA/')
    # 大河庄苑
    urlList.append('http://bj.ganji.com/fang3/_%E5%A4%A7%E6%B2%B3%E5%BA%84%E8%8B%91/')
    # 稻香园
    urlList.append('http://bj.ganji.com/fang3/_%E7%A8%BB%E9%A6%99%E5%9B%AD/')
    urlList.append('http://bj.ganji.com/fang3/o2/_%E7%A8%BB%E9%A6%99%E5%9B%AD/')
    urlList.append('http://bj.ganji.com/fang3/o3/_%E7%A8%BB%E9%A6%99%E5%9B%AD/')
    urlList.append('http://bj.ganji.com/fang3/o4/_%E7%A8%BB%E9%A6%99%E5%9B%AD/')
    urlList.append('http://bj.ganji.com/fang3/o5/_%E7%A8%BB%E9%A6%99%E5%9B%AD/')
    # 万泉庄
    urlList.append('http://bj.ganji.com/fang3/_%E4%B8%87%E6%B3%89%E5%BA%84/')
    urlList.append('http://bj.ganji.com/fang3/o2/_%E4%B8%87%E6%B3%89%E5%BA%84/')
    urlList.append('http://bj.ganji.com/fang3/o3/_%E4%B8%87%E6%B3%89%E5%BA%84/')
    urlList.append('http://bj.ganji.com/fang3/o4/_%E4%B8%87%E6%B3%89%E5%BA%84/')

    for url in urlList:
        try:
            html, cached = cache.getContentWithAgent(url=url, encoding='utf8', timeout=4 * 60 * 60)
            soup = BeautifulSoup(html)
            lis = soup.findAll('div', {'class':'info-title'})
            for li in lis:
                link = li.find('a')['href']
                if link:
                    GetMatchesLink(link)
                    if not cached:
                        time.sleep(2)
        except Exception as e:
            print(e)
            continue

if __name__ == "__main__":
    Get小区房子()

