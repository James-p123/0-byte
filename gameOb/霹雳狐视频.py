import requests

url = "https://v26-web.douyinvod.com/a37ad8f1af8ad109ca5ef427a0b068e2/654b467f/video/tos/cn/tos-cn-ve-15c001-alinc2/o82TbAnPi68Aye9Llie8lQCAgIP8B2IEERNODb/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1306&bt=1306&cs=2&ds=6&ft=bvTKJbQQqUYqfJEZPo0OW_EklpPiX.0mJFVJEY4wNgbPD-I&mime_type=video_mp4&qs=11&rc=aTc1OzVnaDs5NWY5NDRoM0BpM3hwcDk6ZnlobjMzNGkzM0AuYjEwYTZhNTAxLzI1YjUuYSNlb2xscjQwZnJgLS1kLS9zcw%3D%3D&btag=e00010000&dy_q=1699428437&feature_id=d65f473b4463b6315c21eb3d7c571218&l=20231108152716F9323A0679A18800289D"
headers = {
    "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "referer":"https://www.douyin.com/"
}
res = requests.get(url, headers = headers)

with open ("霹雳狐视频/"+"01".mp4,"wb") as f:
    f.write(res.content)

