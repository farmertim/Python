import urllib.request as request
#抓取PPT的網頁原始碼
url="https://www.ptt.cc/bbs/Stock/index.html"
#建立一個Request物件，附加Request Header的資訊 user-agent
data=request.Request(url,headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"})

with request.urlopen(data) as response:
    final=response.read().decode("utf-8")
#print(final)

#解析原始碼，取的文章的標題 要下載 BeautifulSOup
import bs4
#parser 解析器
root=bs4.BeautifulSoup(final,"html.parser")#讓BeautifulSoup 協助我們找尋HTML格式文件
#titles=root.find("div",class_="title")#尋找一個class="title" 的div標籤
titles=root.find_all("div",class_="title")#尋找所有class="title" 的div標籤
#print(titles.a.string)#找到div 標籤 裡 a標籤裡的string字串
for title in titles:
    if title.a!=None:#如果 title 包含a 標籤 就印出來 不包含就代表以被刪除
        print(title.a.string)
