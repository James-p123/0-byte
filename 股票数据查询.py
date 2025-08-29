import requests
import pandas as pd
import json
import dash
import time
from dash import html,dcc
from dash import Input,Output
from dash import dash_table
import akshare as ak
from datetime import datetime
import plotly.express as px
import plotly.figure_factory as fg
import plotly.graph_objects as go
#获取全部的板块代码和名称
def get_all_bk_code_and_name():
    '''
    获取全部的板块代码和名称
    '''
    url='https://push2.eastmoney.com/api/qt/clist/get?'
    params={
        'cb':'jQuery1123025425493616713957_1665558535555',
        'pn':'1',
        'pz':'500',
        'po':'1',
        'np':'1',
        'fields':'f12,f13,f14,f174',
        'fid':'f174',
        'fs':'m:90+t:2',
        'ut':'b2884a393a59ad64002292a3e90d46a5',
        '_':'1665558535637'
    }
    res = requests.get(url=url, params=params)
    text = res.text[43:len(res.text) - 2]
    json_text = json.loads(text)
    df=pd.DataFrame(json_text['data']['diff'])
    columns=['板块代码','-','板块名称','板块资金流入']
    df.columns=columns
    return df
#获取全部的板块
def get_all_bk_data(priods='今日'):
    '''
    获取全部的板块概念数据
    实时数据
    数据类型，今日，5日，10日
    '''
    data_dict={'今日':'f62','5日':'f164','10日':'f174'}
    url='https://push2.eastmoney.com/api/qt/clist/get?'
    params={
        'cb':'jQuery1123025425493616713957_1665558535555',
        'fid':data_dict[priods],
        'po':'1',
        'pz':'200',
        'pn':'1',
        'np':'1',
        'fltt':'2',
        'invt':'2',
        'ut':'b2884a393a59ad64002292a3e90d46a5',
        'fs':'m:90 t:2',
        'fields':'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124,f1,f13'
    }
    res = requests.get(url=url, params=params)
    text = res.text[43:len(res.text) - 2]
    json_text = json.loads(text)
    df=pd.DataFrame(json_text['data']['diff'])
    columns=['-','-','今日涨跌幅','板块代码','-','板块名称','今日主力净流入-净额','今日超大单净流入-净额',
    '今日超大单净流入-净占比','今日大单净流入-净额','今日大单净流入-净占比','今日中单净流入-净额','今日中单净流入-净占比',
    '今日小单净流入-净额','今日小单净流入-净占比','-','今日主力净流入-净占比','今日主力净流入最大股','股票代码','-']
    df.columns=columns
    del df['-']
    return df
#获取板块交易数据
def get_bk_trader_data_em(code='BK1029',start_date='20220701'):
    '''
    获取板块交易数据
    数据来自东方财富日线数据
    汽车板块为例http://quote.eastmoney.com/bk/90.BK1029.html#
    code板块代码，start_date开始时间，end_date介绍时间
    '''
    loc=time.localtime()
    year=loc.tm_year
    mo=loc.tm_mon
    daily=loc.tm_mday
    if mo<=9:
        mo='0'+str(mo)
    if daily<=9:
        daily='0'+str(daily)
    end_date='{}{}{}'.format(year,mo,daily)
    url='http://66.push2his.eastmoney.com/api/qt/stock/kline/get?'
    params={
        'cb':'jQuery35105177058251439297_1659341939018',
        'secid':'90.{}'.format(code),
        'ut':'fa5fd1943c7b386f172d6893dbfba10b',
        'fields1':'f1,f2,f3,f4,f5,f6',
        'fields2':'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
        'klt':'101',
        'fqt':'1',
        'beg':start_date,
        'end':end_date,
        'smplmt':'460',
        'lmt':'1000000',
        '_':'1659341939158'
    }
    res=requests.get(url=url,params=params)
    text=res.text[41:len(res.text)-2]
    json_text=json.loads(text)
    df=pd.DataFrame(json_text['data']['klines'])
    df.columns=['数据']
    data=[]
    for i in df['数据']:
        data.append(i.split(','))
    df1=pd.DataFrame(data)
    columes=['date','open','close','high','low','成交额',
    '振幅','涨跌幅','涨跌额','换手率','-']
    df1.columns=columes
    return df1
#获取板块成分股
def get_bk_stock_data_em(code='BK1029',priods='今日'):
    '''
    获取板块成分股
    数据来自东方财富
    汽车板块为例子
    code板块代码1029汽车
    https://data.eastmoney.com/bkzj/BK1029.html
    '''
    data_dict={'今日':'f3','5日':'f109','10日':'f160'}
    url='https://push2.eastmoney.com/api/qt/clist/get?'
    params={
        'cb':'jQuery112304883635439371805_1659341233428',
        'fid':data_dict[priods],
        'po':'1',
        'pz':'5000',
        'pn':'1',
        'np':'1',
        'fltt':'2',
        'invt':'2',
        'ut':'b2884a393a59ad64002292a3e90d46a5',
        'fs':'b:{}'.format(code),
        'fields':'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124,f1,f13'
    }
    res=requests.get(url=url,params=params)
    text=res.text[42:len(res.text)-2]
    json_text=json.loads(text)
    df=pd.DataFrame(json_text['data']['diff'])
    #选取股票的代码和名称就可以了
    columns=['-','最新价','今日涨跌幅','股票代码','-','股票名称','主力净流入-净额','超大单净流入','超大单净流入-占比',
    '大单净流入','大单净流入-占比','中单净流入','中单净流入-占比','小单净流入','小单净流入-占比',
    '-','主力净流入-净占比','-','-','-']
    df.columns=columns
    del df['-']
    return df
#获取板块实时数据
def get_bk_now_cash_trader_data(code='BK1029'):
    '''
    获取板块实时资金数据
    code板块代码
    '''
    url='https://push2.eastmoney.com/api/qt/stock/fflow/kline/get?'
    params={
        'cb':'jQuery1123002395009316077612_1665562995811',
        'lmt':'0',
        'klt':'1',
        'fields1':'f1,f2,f3,f7',
        'fields2':'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65',
        'ut':'b2884a393a59ad64002292a3e90d46a5',
        'secid':'90.{}'.format(code),
        '_':'1665562995812'
    }
    res=requests.get(url=url,params=params)
    text=res.text[43:len(res.text)-2]
    json_text=json.loads(text)
    df=pd.DataFrame(json_text['data']['klines'])
    df.columns=['数据']
    data_list=[]
    for m in df['数据']:
        data_list.append(m.split(','))
    data=pd.DataFrame(data_list)
    columns=['时间','今日主力净流入','  今日小单净流入','今日中单净流入','今日大单净流入','今日超大单净流入']
    data.columns=columns
    return data
#获取板块历史资金流
def get_bk_hist_cash_data(code='BK1029'):
    '''
    '''
    url='https://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get?'
    params={
        'cb':'jQuery1123045213813657472657_1665564061064',
        'lmt':'0',
        'klt':'101',
        'fields1':'f1,f2,f3,f7',
        'fields2':'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65',
        'ut':'b2884a393a59ad64002292a3e90d46a5',
        'secid':'90.{}'.format(code),
        '_':'1665564061065'
    }
    res=requests.get(url=url,params=params)
    text=res.text[43:len(res.text)-2]
    json_text=json.loads(text)
    df=pd.DataFrame(json_text['data']['klines'])
    df.columns=['数据']
    data_list=[]
    for m in df['数据']:
        data_list.append(m.split(','))
    data=pd.DataFrame(data_list)
    columns=['日期','主力净流入-净额','小单净流入-净额','中单净流入-净额','大单净流入-净额',
    '超大单净流入-净额','主力净流入-净占比','小单净流入-净占比','中单净流入-净占比','大单净流入-净占比',
    '超大单净流入-净占比','-','-','-','-']
    data.columns=columns
    del data['-']
    return data
#获取分时数据
def stock_board_industry_hist_min_em(symbol='BK1027', period= '5') :
    """
    获取分时数据
    :param period: choice of {"1", "5", "15", "30", "60"}
    :type period: str
    :return: 分时历史行情
    :rtype: pandas.DataFrame
    """
    url = "http://7.push2his.eastmoney.com/api/qt/stock/kline/get"
    params = {
        "secid": f"90.{symbol}",
        "ut": "fa5fd1943c7b386f172d6893dbfba10b",
        "fields1": "f1,f2,f3,f4,f5,f6",
        "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61",
        "klt": period,
        "fqt": "1",
        "beg": "0",
        "end": "20500101",
        "smplmt": "10000",
        "lmt": "1000000",
        "_": "1626079488673",
    }
    r = requests.get(url, params=params)
    data_json = r.json()
    temp_df = pd.DataFrame(
        [item.split(",") for item in data_json["data"]["klines"]]
    )
    temp_df.columns = ["日期时间","开盘","收盘","最高","最低","成交量","成交额","振幅","涨跌幅","涨跌额","换手率",]
    temp_df = temp_df[
        [ "日期时间","开盘","收盘","最高","最低","涨跌幅","涨跌额","成交量","成交额","振幅", "换手率",]
    ]
    temp_df["开盘"] = pd.to_numeric(temp_df["开盘"], errors="coerce")
    temp_df["收盘"] = pd.to_numeric(temp_df["收盘"], errors="coerce")
    temp_df["最高"] = pd.to_numeric(temp_df["最高"], errors="coerce")
    temp_df["最低"] = pd.to_numeric(temp_df["最低"], errors="coerce")
    temp_df["涨跌幅"] = pd.to_numeric(temp_df["涨跌幅"], errors="coerce")
    temp_df["涨跌额"] = pd.to_numeric(temp_df["涨跌额"], errors="coerce")
    temp_df["成交量"] = pd.to_numeric(temp_df["成交量"], errors="coerce")
    temp_df["成交额"] = pd.to_numeric(temp_df["成交额"], errors="coerce")
    temp_df["振幅"] = pd.to_numeric(temp_df["振幅"], errors="coerce")
    temp_df["换手率"] = pd.to_numeric(temp_df["换手率"], errors="coerce")
    return temp_df
df=get_all_bk_code_and_name()
bk_name=dict(zip(df['板块代码'].tolist(),df['板块名称'].tolist()))
app=dash.Dash(__name__)
app.layout=html.Div([
    html.H2('股票板块题材分析'),
    dcc.RadioItems(options=['下载数据','不下载数据'],value='不下载数据',id='down'),
    dcc.RadioItems(options=['今日', '3日', '5日', '10日'],value='今日',id='bk_down'),
    html.P('选择数据可以选择今日, 3日, 5日, 10日数据'),
    dcc.RadioItems(options=['个股资金流入排行','板块代码和名称','板块概念数据','板块交易数据',
    '板块成分股排行','板块实时资金数据','板块历史资金流数据','1分钟数据','5分钟数据','15分钟数据','30分钟数据','60分钟数据',],value='个股资金流入排行',id='bk_data_type',style={'font-size':18}),
    dcc.Dropdown(options=bk_name,value='BK1029',id='bk_stock'),
    dcc.DatePickerSingle(date='20220901',id='start_date'),
    dcc.DatePickerSingle(date=datetime.now(),id='end_date'),
    dcc.Download(id='down_bk_data'),
    dash_table.DataTable(
        id='show_bk_data',
        page_size=10,
        style_table={'font-size':16}
    ),
    dcc.Graph(id='show_bk_figure')
])
#通用板块数据回调
@app.callback(
        Output(component_id='show_bk_data',component_property='data'),
        Input(component_id='start_date',component_property='date'),
        Input(component_id='end_date',component_property='date'),
        Input(component_id='bk_down',component_property='value'),
        Input(component_id='bk_data_type',component_property='value'),
        Input(component_id='bk_stock',component_property='value')
)
def update_show_bk_data(start_date,end_date,bk_down,bk_data_type,bk_stock):
    if bk_data_type=='个股资金流入排行':
        df=ak.stock_individual_fund_flow_rank(indicator=bk_down)
        return df.to_dict('records')
    elif bk_data_type=='板块代码和名称':
        df=get_all_bk_code_and_name()
        return df.to_dict('records')
    elif bk_data_type=='板块概念数据':
        df=get_all_bk_data(priods=bk_down)
        return df.to_dict('records')
    elif bk_data_type=='板块交易数据':
        df=get_bk_trader_data_em(code=bk_stock,start_date=''.join(str(start_date)[:11].split('-')))
        return df.to_dict('records')
    elif bk_data_type=='板块成分股排行':
        df=get_bk_stock_data_em(code=bk_stock)
        return df.to_dict('records')
    elif bk_data_type=='板块实时资金数据':
        df=get_bk_now_cash_trader_data(code=bk_stock)
        return df.to_dict('records')
    elif bk_data_type=='板块历史资金流数据':
        df=get_bk_hist_cash_data(code=bk_stock)
        return df.to_dict('records')
    elif bk_data_type=='1分钟数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="1")
        return df.to_dict('records')
    elif bk_data_type=='5分钟数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="5")
        return df.to_dict('records')
    elif bk_data_type=='15分钟数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="15")
        return df.to_dict('records')
    elif bk_data_type=='30分钟数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="30")
        return df.to_dict('records')
    elif bk_data_type=='60分钟数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="60")
        return df.to_dict('records')
#通用图片显示数据回调
@app.callback(
        Output(component_id='show_bk_figure',component_property='figure'),
        Input(component_id='start_date',component_property='date'),
        Input(component_id='end_date',component_property='date'),
        Input(component_id='bk_down',component_property='value'),
        Input(component_id='bk_data_type',component_property='value'),
        Input(component_id='bk_stock',component_property='value')
)
def update_bk_figure_data(start_date,end_date,bk_down,bk_data_type,bk_stock):
    if bk_data_type=='个股资金流入排行':
        df=ak.stock_individual_fund_flow_rank(indicator=bk_down)[:10]
        fig=px.bar(data_frame=df,x='名称',y='{}主力净流入-净额'.format(bk_down))
        return fig
    elif bk_data_type=='板块代码和名称':
        df=get_all_bk_code_and_name()
        fig=px.bar(data_frame=df,x='板块名称',y='板块资金流入')
        return fig
    elif bk_data_type=='板块概念数据':
        df=get_all_bk_data(priods=bk_down)[:10]
        fig=px.bar(data_frame=df,x='板块名称',y='今日主力净流入-净额')
        return fig
    elif bk_data_type=='板块交易数据':
        df=get_bk_trader_data_em(code=bk_stock,start_date=''.join(str(start_date)[:11].split('-')))
        fig=go.Figure(data=[go.Candlestick(x=df['date'],open=df['open'],close=df['close'],high=df['high'],low=df['low'])])
        return fig
    elif bk_data_type=='板块成分股排行':
        df=get_bk_stock_data_em(code=bk_stock)
        fig=px.bar(data_frame=df,x='股票名称',y='主力净流入-净额')
        return fig
    elif bk_data_type=='板块实时资金数据':
        df=get_bk_now_cash_trader_data(code=bk_stock)
        y_list =['今日主力净流入','今日中单净流入','今日大单净流入','今日超大单净流入']
        for m in y_list:
            df[m] = pd.to_numeric(df[m])
        fig=px.line(data_frame=df,x='时间',y=['今日主力净流入','今日中单净流入','今日大单净流入','今日超大单净流入'])
        return fig
    elif bk_data_type=='板块历史资金流数据':
        df=get_bk_hist_cash_data(code=bk_stock)
        y_list=['主力净流入-净额','小单净流入-净额','中单净流入-净额','大单净流入-净额','超大单净流入-净额']
        for m in y_list:
            df[m]=pd.to_numeric(df[m])
        fig=px.line(data_frame=df,x='日期',y=['主力净流入-净额','小单净流入-净额','中单净流入-净额','大单净流入-净额','超大单净流入-净额'])
        return fig
    elif bk_data_type=='1分钟数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="1")
        df['日期时间']=pd.to_datetime(df['日期时间'])
        fig=go.Figure(data=[go.Candlestick(open=df['开盘'],close=df['收盘'],low=df['最低'],high=df['最高'])])
        return fig
    elif bk_data_type=='5分钟数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="5")
        df['日期时间'] = pd.to_datetime(df['日期时间'])
        fig=go.Figure(data=[go.Candlestick(open=df['开盘'],close=df['收盘'],low=df['最低'],high=df['最高'])])
        return fig
    elif bk_data_type=='15分钟数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="15")
        df['日期时间'] = pd.to_datetime(df['日期时间'])
        fig=go.Figure(data=[go.Candlestick(open=df['开盘'],close=df['收盘'],low=df['最低'],high=df['最高'])])
        return fig
    elif bk_data_type=='30分钟数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="30")
        df['日期时间'] = pd.to_datetime(df['日期时间'])
        fig=go.Figure(data=[go.Candlestick(open=df['开盘'],close=df['收盘'],low=df['最低'],high=df['最高'])])
        return fig
    elif bk_data_type=='60分钟数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="60")
        df['日期时间'] = pd.to_datetime(df['日期时间'])
        fig=go.Figure(data=[go.Candlestick(open=df['开盘'],close=df['收盘'],low=df['最低'],high=df['最高'])])
        return fig
#通用板块数据下载
@app.callback(
        Output(component_id='down_bk_data',component_property='data'),
        Input(component_id='start_date',component_property='date'),
        Input(component_id='end_date',component_property='date'),
        Input(component_id='bk_down',component_property='value'),
        Input(component_id='bk_data_type',component_property='value'),
        Input(component_id='bk_stock',component_property='value'),
        Input(component_id='down',component_property='value')
)
def update_show_bk_data(start_date,end_date,bk_down,bk_data_type,bk_stock,down):
    if bk_data_type=='个股资金流入排行' and down=='下载数据':
        df=ak.stock_individual_fund_flow_rank(indicator=bk_down)
        return dcc.send_data_frame(df.to_excel,filename='{}{}.xlsx'.format(bk_data_type,bk_down))
    elif bk_data_type=='板块代码和名称' and down=='下载数据':
        df=get_all_bk_code_and_name()
        return dcc.send_data_frame(df.to_excel,filename='{}.xlsx'.format(bk_data_type))
    elif bk_data_type=='板块概念数据' and down=='下载数据':
        df=get_all_bk_data(priods=bk_down)
        return dcc.send_data_frame(df.to_excel,filename='{}{}.xlsx'.format(bk_data_type,bk_down))
    elif bk_data_type=='板块交易数据' and down=='下载数据':
        df=get_bk_trader_data_em(code=bk_stock,start_date=''.join(str(start_date)[:11].split('-')))
        return dcc.send_data_frame(df.to_excel,filename='{}{}.xlsx'.format(bk_stock,bk_data_type))
    elif bk_data_type=='板块成分股排行' and down=='下载数据':
        df=get_bk_stock_data_em(code=bk_stock)
        return dcc.send_data_frame(df.to_excel,filename='{}{}.xlsx'.format(bk_stock,bk_data_type))
    elif bk_data_type=='板块实时资金数据' and down=='下载数据':
        df=get_bk_now_cash_trader_data(code=bk_stock)
        return dcc.send_data_frame(df.to_excel,filename='{}{}.xlsx'.format(bk_stock,bk_data_type))
    elif bk_data_type=='板块历史资金流数据' and down=='下载数据':
        df=get_bk_hist_cash_data(code=bk_stock)
        return dcc.send_data_frame(df.to_excel,filename='{}{}.xlsx'.format(bk_stock,bk_data_type))
    elif bk_data_type=='1分钟数据' and down=='下载数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="1")
        return dcc.send_data_frame(df.to_excel,filename='{}{}.xlsx'.format(bk_stock,bk_data_type))
    elif bk_data_type=='5分钟数据' and down=='下载数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="5")
        return dcc.send_data_frame(df.to_excel,filename='{}{}.xlsx'.format(bk_stock,bk_data_type))
    elif bk_data_type=='15分钟数据' and down=='下载数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="15")
        return dcc.send_data_frame(df.to_excel,filename='{}{}.xlsx'.format(bk_stock,bk_data_type))
    elif bk_data_type=='30分钟数据' and down=='下载数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="30")
        return dcc.send_data_frame(df.to_excel,filename='{}{}.xlsx'.format(bk_stock,bk_data_type))
    elif bk_data_type=='60分钟数据' and down=='下载数据':
        df=stock_board_industry_hist_min_em(symbol=bk_stock, period="60")
        return dcc.send_data_frame(df.to_excel,filename='{}{}.xlsx'.format(bk_stock,bk_data_type))
if __name__=='__main__':
    app.run_server(debug=True)