import requests
import re
from lxml import etree

''' def function():
    func = function(l) {
        function e(e) {
            for (var t, r, n = e[0], o = e[1], u = e[2], i = 0, a = []; i < n.length; i++)
                r = n[i],
                Object.prototype.hasOwnProperty.call(p, r) && p[r] && a.push(p[r][0]),
                p[r] = 0;
            for (t in o)
                Object.prototype.hasOwnProperty.call(o, t) && (l[t] = o[t]);
            for (s && s(e); a.length; )
                a.shift()();
            return c.push.apply(c, u || []),
            f()
        }
        function f() {
            for (var e, t = 0; t < c.length; t++) {
                for (var r = c[t], n = !0, o = 1; o < r.length; o++) {
                    var u = r[o];
                    0 !== p[u] && (n = !1)
                }
                n && (c.splice(t--, 1),
                e = i(i.s = r[0]))
            }
            return e
        }
        var r = {}
            , p = {
            1: 0
        }
            , c = [];
        function i(e) {
            if (r[e])
                return r[e].exports;
            var t = r[e] = {
                i: e,
                l: !1,
                exports: {}
            };
            return l[e].call(t.exports, t, t.exports, i),
            t.l = !0,
            t.exports
        }
        i.m = l,
        i.c = r,
        i.d = function(e, t, r) {
            i.o(e, t) || Object.defineProperty(e, t, {
                enumerable: !0,
                get: r
            })
        }
        ,
        i.r = function(e) {
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                value: "Module"
            }),
            Object.defineProperty(e, "__esModule", {
                value: !0
            })
        }
        ,
        i.t = function(t, e) {
            if (1 & e && (t = i(t)),
            8 & e)
                return t;
            if (4 & e && "object" == typeof t && t && t.__esModule)
                return t;
            var r = Object.create(null);
            if (i.r(r),
            Object.defineProperty(r, "default", {
                enumerable: !0,
                value: t
            }),
            2 & e && "string" != typeof t)
                for (var n in t)
                    i.d(r, n, function(e) {
                        return t[e]
                    }
                    .bind(null, n));
            return r
        }
        ,
        i.n = function(e) {
            var t = e && e.__esModule ? function() {
                return e.default
            }
            : function() {
                return e
            }
            ;
            return i.d(t, "a", t),
            t
        }
        ,
        i.o = function(e, t) {
            return Object.prototype.hasOwnProperty.call(e, t)
        }
        ,
        i.p = "./";
        var t = this.webpackJsonpexamination = this.webpackJsonpexamination || []
            , n = t.push.bind(t);
        t.push = e,
        t = t.slice();
        for (var o = 0; o < t.length; o++)
            e(t[o]);
        var s = n;
        f()
    }([]) '''

def get_web_content():
    try:
        url = 'https://exam.mshengedu.com/examPC/#/exam/examAnalysis?token=8df70b035c1e4b03844258a11f3cb3e0&testUserId=4184942&subjectId=1010000000001132&originOrgType=0'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
        ''' data = {
            'Accept': 'text/css,*/*;q=0.1',
            'Accept-Encoding': 'gzip, deflate, br',
            'id': '4184942',
            'examUserId': "4184942",
            'questionType': 'null',
            'status': 'null',
            'subjectId': "1010000000001132",
            'token':'d264ef12e3dd49dd8f479b726b0b08c8',
            'testUserId':'4184942',
            'subjectId':'1010000000001132',
            'originOrgType': 0,
        } '''
        
        
        res = requests.request(url=url, headers=headers)#.content.decode('utf-8')
        return res
    except TimeoutError as e:
        return None


def parsing():
    info = get_web_content()
    if info is not None:
        html = etree.HTML(info)
        # 先获取一个大的节点，包含了想要获取的所有信息
        pat = html.xpath('/html/body/div[2]/div/div[3]/div[2]/div[1]')
        
        x = 0
        x in range (34)
        for item in pat:
        # 采用循环，依次从大节点中获取小的节点内容
            # ''.join() 将列表中的内容拼接成一个字符串
            ret = {
            	# @href 表示：获取属性为href的内容
                #'href': "https:" + _.xpath('./div/div[1]/a/@href')[0],
                #'title': ''.join(
                #        _.xpath('./div/div[2]/div/ul/li/a/@title')),
                # text()表示获取节点i里面的文本信息
                'question': item.xpath('.//*[@id="content"]/div[1]/div[1]/div/div/text()'),
                'list': item.xpath('.//*[@id="content"]/div'+str[x]+'/div[3]/div[1]/div[1]/div[1]/span/text()'),
                'option': ''.join(item.xpath('.//*[@id="content"]/div[1]/div[3]/div[1]/div[1]/div[1]/div/span/text()')).strip(),
                'answer': item.xpath('.//*[@id="content"]/div'+str[x]+'/div[3]/div[1]/div[2]/span/text()'),
                'explan': item.xpath('.//*[@id="content"]/div[3]/div[2]/div/span/text()')
                

            }

            print(ret)
            with open('./文化管理真题1.html', 'wb') as f:
                f.write(ret)
    else:
        raise Exception("Failed to get page information, please check！")
    
    return None


if __name__ == '__main__':
    parsing()



