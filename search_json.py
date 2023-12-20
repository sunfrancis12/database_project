import mysql.connector as mysql
import json

def search_json(food):

    connection = mysql.connect(host='localhost',port='3306',user='root',password='francis1212') #connect to database
    cursor = connection.cursor()

    cursor.execute("use project;") #使用project資料庫
    cursor.execute(f"SELECT * FROM data where 介紹 like \'%{food}%\';") #搜尋含有該資料之店家
    record = cursor.fetchall()

    food_dict = {} #儲存結果的dict
    count = 1 #第n筆結果
    
    for i in record: #將資料庫查詢存入一個json檔
        shop_id = "shop_" + str(count)
        count +=1
        
        food_dict[shop_id] = {}
        food_dict[shop_id]["名稱"] = str(i[0])
        food_dict[shop_id]["網址"] = str(i[1])
        food_dict[shop_id]["電話"] = str(i[2])
        food_dict[shop_id]["行政區"] = str(i[3])
        food_dict[shop_id]["Areacode"] = str(i[4])
        food_dict[shop_id]["地址"] = str(i[5])
        food_dict[shop_id]["介紹"] = str(i[6])
    
    #print(food_dict)
    
    food_json = json.dumps(food_dict, ensure_ascii=False) #將json轉成字串
    
    return food_json  
    