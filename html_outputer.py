#!/usr/bin/env python
# -*- conding:utf-8 -*-
import json
class HtmlOutPuter(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return None
        #print('文本解析有数据传来')
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<meta charset=utf-8>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td><br>" % data['url'])
            fout.write("<td>%s</td><br>" % data['title'])
            fout.write("<td>%s</td><br>" % data['summary_node'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()