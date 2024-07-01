
import requests
import execjs  # pip install pyexecjs2

# 重点了解一下
# execjs.compile加载js代码
# open('./CodeJsdemo1.js', 'r'(读), encoding='utf-8').read()文件读取 指定编码
v = execjs.compile(open('./CodeJsdemo1.js', 'r', encoding='utf-8').read()).call('main123')

# cookie  用户信息
# 时效性cookie  在一定的时间之内 有效的  过期
cookies = {
    'cid': '280caffbf85fa59d54e0b41727f633bc1716290012',
    'other_uid': 'Ths_iwencai_Xuangu_ufqxlxrd5o5vh6l567x10964gfcz2tg4',
    'ta_random_userid': 'zkzoioa244',
    'v': v,  # 每次都是新的
}

# 请求头  模拟浏览器的请求
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'cid=280caffbf85fa59d54e0b41727f633bc1716290012; other_uid=Ths_iwencai_Xuangu_ufqxlxrd5o5vh6l567x10964gfcz2tg4; ta_random_userid=zkzoioa244; v=A3cTNHt73X7PcFmzwZkd5VTiBmDFPEgZJRHPLsklkHOsg5ke0Qzb7jXgX3Ta',
    'Origin': 'https://www.iwencai.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.iwencai.com/unifiedwap/result?w=5g&querytype=stock&addSign=1718712525669',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'hexin-v': 'A3cTNHt73X7PcFmzwZkd5VTiBmDFPEgZJRHPLsklkHOsg5ke0Qzb7jXgX3Ta',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# post请求  搜索接口 提交一个信息给服务器 请求体
json_data = {
    'source': 'Ths_iwencai_Xuangu',
    'version': '2.0',
    'query_area': '',
    'block_list': '',
    'add_info': '{"urp":{"scene":1,"company":1,"business":1},"contentType":"json","searchInfo":true}',
    'question': '5g',
    'perpage': '100',
    'page': 1,
    'secondary_intent': 'stock',
    'log_info': '{"input_type":"typewrite"}',
    'rsh': 'Ths_iwencai_Xuangu_ufqxlxrd5o5vh6l567x10964gfcz2tg4',
}

# 发送了一个post请求
#  地址: 动态接口
response = requests.post(
    'https://www.iwencai.com/customized/chart/get-robot-data',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
print(response)
