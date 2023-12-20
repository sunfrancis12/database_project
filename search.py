import mysql.connector as mysql

def search(food):

    connection = mysql.connect(host='localhost',port='3306',user='root',password='francis1212') #connect to database
    cursor = connection.cursor()

    cursor.execute("use project;") #使用project資料庫
    cursor.execute(f"SELECT * FROM data where 介紹 like \'%{food}%\';") #搜尋含有該資料之店家
    record = cursor.fetchall()
    
    #return " ".join(record)
    string = ""
    for i in record:
        for j in i:
            string += f"{str(j)} "
        string += "\n"
        
    return string
    
