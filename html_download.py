
import requests
from requests.exceptions import RequestException
import time

class HtmlDownloader(object):

    def download(self, url):
        cookies = 'BAIDUID=3FCB907BBE0A09BEEED596A6AA3586B4:FG=1; \
        BIDUPSID=3FCB907BBE0A09BEEED596A6AA3586B4; PSTM=1538881463;\
        BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; pgv_pvi=5319319552; \
        baikedeclare=showed; ZD_ENTRY=google; delPer=0; H_PS_PSSID=1463_21108_18559_22159; \
        Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1539833271,1539910307; \
        Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1539910307; \
        pgv_si=s1565589504'
        jar = requests.cookies.RequestsCookieJar()
        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) \
                  AppleWebKit / 537.36(KHTML, likeGecko) \
                  Chrome / 69.0.3497.100Safari / 537.36'

        if url is None:
            return None
        try:
            response = s.get(url, cookies=jar)
            if response.status_code != 200:
                return None
            #print('url解析出了文本')
            response.encoding = 'utf-8'
            #print('解析出的文本的编码', response.encoding)
            return response.text
        except RequestException as e:
            #print('获取网页错误:%s', e.args)
            return None