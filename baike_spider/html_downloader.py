import urllib


class HtmlDownloader(object):

    def download(self , url):

        if url is None:
            return

        response = urllib.urllib.urlopen(url)

        if response.getcode() !=200:
            return
        return  response.read().encode('utf-8')