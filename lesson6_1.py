def sayHello():#沒有參數的function
    print("Hello!")

def sayHello_withName(name): #有一個參數的function
    print(f"Hello {name}")

def square_area(side): #有一個參數,同時有傳出值
    area = side ** 2 #function內的變數
    return area

def rectangle(width,height):#有2個參數,同時有傳出值
    area = width * height
    return area

if __name__ == "__main__":
    side = eval(input("請輸入正方形的邊:"))
    area = square_area(side) #文件變數
    print(f"正方形,一邊為{side},面積為{area}")

    area = rectangle(15.5, 20.9)
    print(f"矩形的寬是15.5,高是20.9,面積為{area}")