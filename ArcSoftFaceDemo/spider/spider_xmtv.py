# -*- coding: utf-8 -*-
__author__ = 'Ginseng'
from urllib import request
import re


class Spider():
    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'  # 注意匹配的内容要与原始匹配数据一致,注意问号的作用(非贪婪模式)
    name_pattern = '</i>([\s\S]*?)</span>'
    number_patter = '<span class="video-number">([\s\S]*?)</span>'
    # name2_pattern = "[\S]*?"
    number2_pattern = 'i>([\d\w\s\S]*)'
    number3_pattern = '[\d\s\S]*万$'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()  # bytes
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __get_real_number(self, value):
        """
        方式一:直接用正则转换万
        :param value:
        :return:
        """
        v = value.group()
        # re.sub('万', '', v)  # 17.7   17 7000
        v = v.replace('万', '')
        v = float(v) * 10000
        return str(v)

    def __analysis(self, htmls):
        # 1.尽量寻找离目标值最近的唯一标识性的
        # 2.尽量寻找可闭合的标签
        # root_html2 = re.findall(self.root_pattern, htmls) # 似乎结果与下面的一样
        anchors = []
        root_html = re.findall(Spider.root_pattern, htmls)
        for html in root_html:
            # name = re.findall(Spider.name_pattern, html)[0]
            # name = re.sub(' ', '', name)
            # name = re.sub('\n', '', name)
            # number = re.findall(Spider.number_patter, html)[0]
            # number = re.findall(Spider.number2_pattern, number)[0]
            # number = re.sub(Spider.number3_pattern, self.__get_real_number, number)  # 不要用类调用方法如Spider,__get_real_number
            # -------------------------------------以上方法是原始方法
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_patter, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)

        return anchors

    def __refine(self, anchors):
        """
        批量处理
        :param anchors:
        :return:
        """
        lam = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': str(re.findall(Spider.number2_pattern, anchor['number'][0])).replace("['", '').replace("']", '')
        }
        return map(lam, anchors)

    def __sort(self, anchors):
        # 第三个参数 reverse默认False,是升序排列
        anchors = sorted(anchors, key=self.__sort_seed,
                         reverse=True)  # key传入一个函数,用于对比字典内的某种元素大小,如果不指定key则默认会比较字典内的所有元素,但必须得支持大小比较
        return anchors

    def __sort_seed(self, anchor):
        """
        方式二:通过正则和if转换万
        :param anchor:
        :return:
        """
        snum = str(anchor['number'])
        r = re.findall('\d*', snum)
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            # print(anchor["name"] + "----" + anchor["number"])  # 不能用+号连接  因为+是连接符，需要2边都是str才行
            # print(anchor["name"], "----", anchor["number"])
            print("rank", str(rank + 1), ":", anchors[rank]['name'],
                  "-----", anchors[rank]['number']
                  )

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()
