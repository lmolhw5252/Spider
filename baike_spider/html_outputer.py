

'''输出器'''
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html_1(self):
        fout = open('output.md', 'w', encoding='utf8')

        # 使用MarkDown语法输出
        fout.write('#百度百科\n')
        for data in self.datas:
            fout.write("##[%s](%s)##\n" % (data['title'], data['url']))
            fout.write("> %s" % (data['summary']))
            fout.write('\n\n---------\n\n')  # 分隔线

        fout.close()

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf8')

        fout.write("<html>")
        fout.write("<body>")
        fout.write('<a href="http://yhx.wiki/" target="_blank"><h3>http://yhx.wiki<h3></a>')
        fout.write('<table border="1px" cellspacing="0px" cellpadding="5">')
        fout.write('<tr>')
        fout.write('<td>标题</td>')
        fout.write('<td>摘要</td>')
        fout.write('<td>链接</td>')
        fout.write('</tr>')

        # ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("<td>%s</td>" % data['url'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()