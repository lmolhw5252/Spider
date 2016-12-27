import urllib


from urllib import request


class HtmlDownloader(object):
    # 获取页面HTML代码
    def download(self, url):
        if url is None:
            return None
        response = request.urlopen(url)
        if response.getcode() != 200:
            return None
        else:
            return response.read().decode('utf8')