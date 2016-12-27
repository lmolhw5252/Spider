
from baike_spider import url_manager,html_downloader,html_outputer,html_parser


class SpiderMain(object):
    def __init__(self):
        #url管理器
        self.urls = url_manager.UrlManager()
        #下载器
        self.downloader = html_downloader.HtmlDownloader()
        #解析器
        self.parser = html_parser.HtmlParser()
        #输出器
        self.outputer = html_outputer.HtmlOutputer()
        #设置最大数量
        self.maxcount = 10


    def craw(self,root_url):
        count = 0
        self.urls.add_new_url(root_url)
        '''当url中有在爬取的url时'''
        while self.urls.has_new_url():
            '''在爬取的时候要加入异常处理'''
            try:
                '''获取在爬取的url'''
                new_url = self.urls.get_new_url()
                # print("craw %d : %s" %(count,new_url))

                '''启动下载器下载这个页面，结果存在html_cont中'''
                html_cont = self.downloader.download(new_url)

                '''下载好的页面，我们调用解析器来解析这个页面的数据，得到新的url列表和新的数据'''
                new_urls , new_data = self.parser.parse(new_url , html_cont)
                '''新的url列表'''
                self.urls.add_new_urls(new_urls)

                '''收集数据'''
                self.outputer.collect_data(new_data)
                if count == self.maxcount:
                    break

            except Exception as e:
                print(e)
                # print("craw failed")
                continue
            else:
                count +=1
                print(new_url)

        self.outputer.output_html() #内容输出至文件

if __name__ == "__main__":
    #设置入口url
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    #启动爬虫
    obj_spider.craw(root_url)