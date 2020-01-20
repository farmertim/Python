from flask import Flask
app=Flask(__name__)#__name__代表目前執行的模組
@app.route("/")#函式的裝飾 已函式為基礎 ，提供附加的功能
def home():
    
    return "Hello Flask22" 
@app.route("/text")
def text():
   
    return "this is text"
if __name__=="__main__":#如果以主程式執行
    app.run()#立刻啟動伺服器
