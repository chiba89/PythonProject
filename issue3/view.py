import eel
import desktop
import search

app_name="C:/Users/handb/Desktop/PythonProject/issue3/html"
end_point="C:/Users/handb/Desktop/PythonProject/issue3/html/index.html"
size=(700,600)

@ eel.expose
def kimetsu_search(word):
    search.kimetsu_search(word)
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)