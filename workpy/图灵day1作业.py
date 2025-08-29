# -*- coding : utf-8 -*-

import requests

url = 'https://www.oklink.com/zh-cn/btc/tx-list'

headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN',
    'Cookie': 'aliyungf_tc=1e9d6af2e1b7dfdb5d84d4627cfe5875c8506c94c9ffd57d2cf13c7f0af45e24; locale=zh_CN; _okcoin_legal_currency=CNY; Hm_lvt_5244adb4ce18f1d626ffc94627dd9fd7=1650982869; Hm_lpvt_5244adb4ce18f1d626ffc94627dd9fd7=1650982869',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
x = 'LWIzMWUtNDU0Ny05Mjk5LWI2ZDA3Yjc2MzFhYmEyYzkwM2NjfDI3NjIxNDQ4MjY1MTkyMjY='

function Bn(t, n, r) {
    if (void 0 === n && (n = {}),
    "function" != typeof t)
        return t;
    try {
        if (t.__sentry__)
            return t;
        if (t.__sentry_wrapped__)
            return t.__sentry_wrapped__
    } catch (n) {
        return t
    }
    var sentryWrapped = function() {
        var i = Array.prototype.slice.call(arguments);
        try {
            r && "function" == typeof r && r.apply(this, arguments);
            var e = i.map(function(t) {
                return Bn(t, n)
            });
            return t.handleEvent ? t.handleEvent.apply(this, e) : t.apply(this, e)
        } catch (t) {
            throw Jn += 1,
            setTimeout(function() {
                Jn -= 1
            }),
            Wt(function(r) {
                r.addEventProcessor(function(t) {
                    var r = f({}, t);
                    return n.mechanism && (gt(r, void 0, void 0),
                    Et(r, n.mechanism)),
                    r.extra = f(f({}, r.extra), {
                        arguments: i
                    }),
                    r
                }),
                captureException(t)
            }),
            t
        }
    };
    try {
        for (var i in t)
            Object.prototype.hasOwnProperty.call(t, i) && (sentryWrapped[i] = t[i])
    } catch (t) {}
    t.prototype = t.prototype || {},
    sentryWrapped.prototype = t.prototype,
    Object.defineProperty(t, "__sentry_wrapped__", {
        enumerable: !1,
        value: sentryWrapped
    }),
    Object.defineProperties(sentryWrapped, {
        __sentry__: {
            enumerable: !1,
            value: !0
        },
        __sentry_original__: {
            enumerable: !1,
            value: t
        }
    });
    try {
        Object.getOwnPropertyDescriptor(sentryWrapped, "name").configurable && Object.defineProperty(sentryWrapped, "name", {
            get: function() {
                return t.name
            }
        })
    } catch (t) {}
    return sentryWrapped
}

r = requests.get(url, headers = headers)