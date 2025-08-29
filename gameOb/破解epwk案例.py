import requests

cookies = {
    'Hm_lvt_e6c705a49657dec3d6b1ad798c50243e': '1699446609',
    'hy_data_2020_id': '18baee954fed9e-03884d321d3268-26031051-921600-18baee954fff8c',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2218baee954fed9e-03884d321d3268-26031051-921600-18baee954fff8c%22%2C%22site_id%22%3A1314%2C%22user_company%22%3A1280%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22pc-bd%22%2C%22%24latest_utm_medium%22%3A%22cpc%22%2C%22%24latest_utm_campaign%22%3A%2296877516%22%2C%22%24latest_utm_content%22%3A%223655936905%22%2C%22%24latest_utm_term%22%3A%22%E4%B8%80%E5%93%81%E5%A8%81%E5%AE%A2%E5%A8%81%E5%AE%A2%E7%BD%91%22%7D%2C%22device_id%22%3A%2218baee954fed9e-03884d321d3268-26031051-921600-18baee954fff8c%22%7D',
    'access_origin': 'https%3A//www.baidu.com/baidu.php%3Furl%3D0f00000uEDLSpLgiC_JAANUvnoRnDa4g1QyZN7fcmyq-hHjiAnSsTQZQ2yYD_QSdv1LF1gtAFYN3bXeMmHLTKhQ3cS5Pro1AqP5cgt0wtZe81B4lamDpuQcIZg4cWsI7RtNn1uTFISMfHxultjA6nuAYytlvemnHRHmwVamvrzTJdELneLsign6n37KIahurxa5IVnOc2VbHz0ZDuFA_chLxaRB1.7D_NR2Ar5Od663pZbMZsIJcrjVzyfIY3L_NqMuk3dS5gKfYt_U_DY2ynTrXSeo6CpXgih4SjikjW9l32AM-9uY3vglChPOH_txZIgYqT7jHzs8BCFBCnTXMI8LtXMxu8l32AM-CFhY_mx5_sS81j__sSXejE33I-XZ1LmxU_se2t5M8sSL1sSLF9tqvZvenrzEj4e_5Vtt5Vzmx5ksSEzselS_IYPZVknXLqXE-oLp3OUPtMSLI-kSL-yFBEIuu3q-xuz4QryeR_nYQ7xH8otN0.U1Yk0ZDqYoEAVtLSEtLPS0KspynqnfKY5I2ekoxPOoOP1xlO1TL30A-V5HczPfKM5yq-TZns0ZNG5yF9pywdUAY0TA-b5Hf0mv-b5H6Y0AdY5HDsnWPxnH0krNtknjDLg1csPH7xn1DzP7tknjfYg1nvnjD0pvbqn0KzIjYknWD0mhbqnHR3g1csP7tdnjn0UynqnH0zndtknjD4g1DsnHIxnW0dnNtknj7xnH0kg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYvPjf3rHbsPjf0UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdMXh93XfKGuAnqiD4a0ZKCIZbq0Zw9ThI-IjYvndtsg1Ddn0KYIgnqnHD3nWfLnHDdn16znjcsnHRYnHT0ThNkIjYkPWb4PjfvPHmdPjnL0ZPGujd-m1NbmW-9PW0snhw9PyDL0AP1UHdjwDDLrHcdwWDsP19anjuD0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYz0AdWgvuzUvYqn7tsg1Kxn7tsg1DsPjuxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg16Ln1DknH7xrjT1nHDknNts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0A7buhk9u1Yk0Akhm1Ys0AwWmvfqnDcznRw7nHmkPRf4wRmkP16dfbfkfHfsP16df101fH01PjfknRD3rRPAfb7Aibd5HbNP0Zwzmyw-5H6knjDsnsKBuA-b5H9AnjckfWczfRmYnW7KwWu7rDPanDfLfYwAn1b1wWuA0AqW5HD0mMfqn0KEmgwL5H00ULfqn0KETMKY5H0WnanWnansc10Wna3snj0snj0WnaPDw-fWnanVc108nj0snj0sc1D8nj0snj0sc10WnansQW0snj0snansc10Wnans0AF9UhV9mvnqnansc10Wn0K3TLwd5Hc4PjcdrH040Z7xIWYsQW6sg108njKxna3sn7tsQW6sg108PjFxn7tsQWfzg100mMPxTZFEuA-b5H00ThqGuhk9u1Ys0APv5fKGTdqWTADqn0KWTjYs0AN1IjYs0APzm1Y1PW0zPs%26us%3Dnewvui%26xst%3DTjYvPjf3rHbsPjfKm1YsfWckwDRkPWDdwj-7wWDLrjNawj7KPj0LrjNjnjPKnjnYPjDkfH64fYuafRu2HRqrwRYKmWY3wW0znRcznb7APjckfRmvwH9jfWKDPYPDwWn4nYmvw6715HDLnjnkrHT1Pj63Pj01P16dnHcLg1czPNts0gTqYoEAVtLSEtLPOoOP1x6KTHLi8tpL1xlO1TL30gRqnWbYnWR4njbKIjYkPWb4PjfvPHmd0ydk5H0an0cV0yPC5yuWgLKW0ykd5H0Kmv3qnHRsnjTYnHwxnWKxuATKTMfqn0D1rHR4nWT1P1nk%26word%3D%26ck%3D6676.7.219.325.189.310.189.781%26shh%3Dwww.baidu.com%26sht%3D15007414_20_dg%26wd%3D%26bc%3D110101',
    'epweike_zturl': 'https%3A//zt.epwk.com/wk20/%3Fepi%3D1443317%26utm_source%3Dpc-bd%26utm_medium%3Dcpc%26utm_campaign%3D96877516%26utm_content%3D3655936905%26utm_term%3D%25E4%25B8%2580%25E5%2593%2581%25E5%25A8%2581%25E5%25AE%25A2%25E5%25A8%2581%25E5%25AE%25A2%25E7%25BD%2591%26sdclkid%3DALf_15fsArDiA5jpA_%26bd_vid%3D8137457304830406984',
    'epweike_zturl_back': 'https%3A//zt.epwk.com/wk20/%3Fepi%3D1443317%26utm_source%3Dpc-bd%26utm_medium%3Dcpc%26utm_campaign%3D96877516%26utm_content%3D3655936905%26utm_term%3D%25E4%25B8%2580%25E5%2593%2581%25E5%25A8%2581%25E5%25AE%25A2%25E5%25A8%2581%25E5%25AE%25A2%25E7%25BD%2591%26sdclkid%3DALf_15fsArDiA5jpA_%26bd_vid%3D8137457304830406984',
    'epweike_construction_epi': 'construction_epi',
    'user_prom_event': '1443317',
    'access_origin_utm': 'do%253Dajax%2526view%253Dtool_click%2526statistic%253D1%2526sp_url%253Dhttps%253A%252F%252Fzt.epwk.com%252Fwk20%252F%253Fepi%253D1443317%2526utm_source%253Dpc-bd%2526utm_medium%253Dcpc%2526utm_campaign%253D96877516%2526utm_content%253D3655936905%2526utm_term%253D%2525E4%2525B8%252580%2525E5%252593%252581%2525E5%2525A8%252581%2525E5%2525AE%2525A2%2525E5%2525A8%252581%2525E5%2525AE%2525A2%2525E7%2525BD%252591%2526sdclkid%253DALf_15fsArDiA5jpA_%2526bd_vid%253D8137457304830406984%2526callback%253DjQuery111209252315579601542_1699446609403%2526_%253D1699446609404',
    'Hm_lvt_387b8f4fdb89d4ea233922bdc6466394': '1699446609,1699520660',
    'PHPSESSID': 'fb1b10115723cc088fa4c84f76bb4b05c74fc15a',
    'time_diff': '0',
    'XDEBUG_SESSION': 'XDEBUG_ECLIPSE',
    'adbanner_city': '%E5%B9%BF%E5%B7%9E%E5%B8%82',
    'login_referer': 'https%3A%2F%2Ftask.epwk.com%2F%3Fk%3Dpython',
    'Hm_lpvt_387b8f4fdb89d4ea233922bdc6466394': '1699520916',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Access-Token': '',
    'App-Id': '4ac490420ac63db4',
    'App-Ver': '',
    'CHOST': 'www.epwk.com',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'Hm_lvt_e6c705a49657dec3d6b1ad798c50243e=1699446609; hy_data_2020_id=18baee954fed9e-03884d321d3268-26031051-921600-18baee954fff8c; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%2218baee954fed9e-03884d321d3268-26031051-921600-18baee954fff8c%22%2C%22site_id%22%3A1314%2C%22user_company%22%3A1280%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22pc-bd%22%2C%22%24latest_utm_medium%22%3A%22cpc%22%2C%22%24latest_utm_campaign%22%3A%2296877516%22%2C%22%24latest_utm_content%22%3A%223655936905%22%2C%22%24latest_utm_term%22%3A%22%E4%B8%80%E5%93%81%E5%A8%81%E5%AE%A2%E5%A8%81%E5%AE%A2%E7%BD%91%22%7D%2C%22device_id%22%3A%2218baee954fed9e-03884d321d3268-26031051-921600-18baee954fff8c%22%7D; access_origin=https%3A//www.baidu.com/baidu.php%3Furl%3D0f00000uEDLSpLgiC_JAANUvnoRnDa4g1QyZN7fcmyq-hHjiAnSsTQZQ2yYD_QSdv1LF1gtAFYN3bXeMmHLTKhQ3cS5Pro1AqP5cgt0wtZe81B4lamDpuQcIZg4cWsI7RtNn1uTFISMfHxultjA6nuAYytlvemnHRHmwVamvrzTJdELneLsign6n37KIahurxa5IVnOc2VbHz0ZDuFA_chLxaRB1.7D_NR2Ar5Od663pZbMZsIJcrjVzyfIY3L_NqMuk3dS5gKfYt_U_DY2ynTrXSeo6CpXgih4SjikjW9l32AM-9uY3vglChPOH_txZIgYqT7jHzs8BCFBCnTXMI8LtXMxu8l32AM-CFhY_mx5_sS81j__sSXejE33I-XZ1LmxU_se2t5M8sSL1sSLF9tqvZvenrzEj4e_5Vtt5Vzmx5ksSEzselS_IYPZVknXLqXE-oLp3OUPtMSLI-kSL-yFBEIuu3q-xuz4QryeR_nYQ7xH8otN0.U1Yk0ZDqYoEAVtLSEtLPS0KspynqnfKY5I2ekoxPOoOP1xlO1TL30A-V5HczPfKM5yq-TZns0ZNG5yF9pywdUAY0TA-b5Hf0mv-b5H6Y0AdY5HDsnWPxnH0krNtknjDLg1csPH7xn1DzP7tknjfYg1nvnjD0pvbqn0KzIjYknWD0mhbqnHR3g1csP7tdnjn0UynqnH0zndtknjD4g1DsnHIxnW0dnNtknj7xnH0kg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYvPjf3rHbsPjf0UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdMXh93XfKGuAnqiD4a0ZKCIZbq0Zw9ThI-IjYvndtsg1Ddn0KYIgnqnHD3nWfLnHDdn16znjcsnHRYnHT0ThNkIjYkPWb4PjfvPHmdPjnL0ZPGujd-m1NbmW-9PW0snhw9PyDL0AP1UHdjwDDLrHcdwWDsP19anjuD0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYz0AdWgvuzUvYqn7tsg1Kxn7tsg1DsPjuxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg16Ln1DknH7xrjT1nHDknNts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0A7buhk9u1Yk0Akhm1Ys0AwWmvfqnDcznRw7nHmkPRf4wRmkP16dfbfkfHfsP16df101fH01PjfknRD3rRPAfb7Aibd5HbNP0Zwzmyw-5H6knjDsnsKBuA-b5H9AnjckfWczfRmYnW7KwWu7rDPanDfLfYwAn1b1wWuA0AqW5HD0mMfqn0KEmgwL5H00ULfqn0KETMKY5H0WnanWnansc10Wna3snj0snj0WnaPDw-fWnanVc108nj0snj0sc1D8nj0snj0sc10WnansQW0snj0snansc10Wnans0AF9UhV9mvnqnansc10Wn0K3TLwd5Hc4PjcdrH040Z7xIWYsQW6sg108njKxna3sn7tsQW6sg108PjFxn7tsQWfzg100mMPxTZFEuA-b5H00ThqGuhk9u1Ys0APv5fKGTdqWTADqn0KWTjYs0AN1IjYs0APzm1Y1PW0zPs%26us%3Dnewvui%26xst%3DTjYvPjf3rHbsPjfKm1YsfWckwDRkPWDdwj-7wWDLrjNawj7KPj0LrjNjnjPKnjnYPjDkfH64fYuafRu2HRqrwRYKmWY3wW0znRcznb7APjckfRmvwH9jfWKDPYPDwWn4nYmvw6715HDLnjnkrHT1Pj63Pj01P16dnHcLg1czPNts0gTqYoEAVtLSEtLPOoOP1x6KTHLi8tpL1xlO1TL30gRqnWbYnWR4njbKIjYkPWb4PjfvPHmd0ydk5H0an0cV0yPC5yuWgLKW0ykd5H0Kmv3qnHRsnjTYnHwxnWKxuATKTMfqn0D1rHR4nWT1P1nk%26word%3D%26ck%3D6676.7.219.325.189.310.189.781%26shh%3Dwww.baidu.com%26sht%3D15007414_20_dg%26wd%3D%26bc%3D110101; epweike_zturl=https%3A//zt.epwk.com/wk20/%3Fepi%3D1443317%26utm_source%3Dpc-bd%26utm_medium%3Dcpc%26utm_campaign%3D96877516%26utm_content%3D3655936905%26utm_term%3D%25E4%25B8%2580%25E5%2593%2581%25E5%25A8%2581%25E5%25AE%25A2%25E5%25A8%2581%25E5%25AE%25A2%25E7%25BD%2591%26sdclkid%3DALf_15fsArDiA5jpA_%26bd_vid%3D8137457304830406984; epweike_zturl_back=https%3A//zt.epwk.com/wk20/%3Fepi%3D1443317%26utm_source%3Dpc-bd%26utm_medium%3Dcpc%26utm_campaign%3D96877516%26utm_content%3D3655936905%26utm_term%3D%25E4%25B8%2580%25E5%2593%2581%25E5%25A8%2581%25E5%25AE%25A2%25E5%25A8%2581%25E5%25AE%25A2%25E7%25BD%2591%26sdclkid%3DALf_15fsArDiA5jpA_%26bd_vid%3D8137457304830406984; epweike_construction_epi=construction_epi; user_prom_event=1443317; access_origin_utm=do%253Dajax%2526view%253Dtool_click%2526statistic%253D1%2526sp_url%253Dhttps%253A%252F%252Fzt.epwk.com%252Fwk20%252F%253Fepi%253D1443317%2526utm_source%253Dpc-bd%2526utm_medium%253Dcpc%2526utm_campaign%253D96877516%2526utm_content%253D3655936905%2526utm_term%253D%2525E4%2525B8%252580%2525E5%252593%252581%2525E5%2525A8%252581%2525E5%2525AE%2525A2%2525E5%2525A8%252581%2525E5%2525AE%2525A2%2525E7%2525BD%252591%2526sdclkid%253DALf_15fsArDiA5jpA_%2526bd_vid%253D8137457304830406984%2526callback%253DjQuery111209252315579601542_1699446609403%2526_%253D1699446609404; Hm_lvt_387b8f4fdb89d4ea233922bdc6466394=1699446609,1699520660; PHPSESSID=fb1b10115723cc088fa4c84f76bb4b05c74fc15a; time_diff=0; XDEBUG_SESSION=XDEBUG_ECLIPSE; adbanner_city=%E5%B9%BF%E5%B7%9E%E5%B8%82; login_referer=https%3A%2F%2Ftask.epwk.com%2F%3Fk%3Dpython; Hm_lpvt_387b8f4fdb89d4ea233922bdc6466394=1699520916',
    'Device-Os': 'web',
    'Device-Ver': '',
    'Imei': '',
    'NonceStr': '16995211335jze7',
    'Origin': 'https://www.epwk.com',
    'Os-Ver': '',
    'Referer': 'https://www.epwk.com/login.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Signature': 'uZlNLjOqVGhpb7PYOLLqEgIuoI0ssduSEk7vQwhSJDb27k2uO8jpnX8ds35PsVAu',
    'Timestemp': '1699521133',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'mobile': '13121758688',
    'vcode': '68h4',
    'from': 'akeymobile',
    'hdn_refer': 'https://task.epwk.com/?k=python',
    'graphics_code': '123sadfsfssdf',
}

response = requests.post('https://www.epwk.com/api/epwk/v1/user/vcodeLogin', cookies=cookies, headers=headers, data=data)
