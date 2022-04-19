#規定範圍並產生密碼
import random

start = 1
end = 100
answer =  random.randint(start, end)  

#重複猜數字，直到猜對為止
while True:
    guess = input('密碼介於 ' + str(start) + '~' + str(end) + ':\n>>')
    
    #檢查輸入的內容是否為數字
    try:
        guess = int(guess)  #把字串轉換成整數
    except ValueError:  #轉換失敗便要求重新輸入數字
        print('格式錯誤，請輸入數字\n')
        continue
    
    #檢查輸入的數字是否介於規定範圍內
    if guess <= start or guess >= end:
        print('請輸入 ' + str(start) + '~' + str(end) + ' 之間的整數\n')
        continue
    
    #判斷有沒有猜中密碼
    if guess == answer:
        print('答對了！')
        break   #猜對才跳脫迴圈
    elif guess < answer:
        start = guess
        print('太小了！',end="")
    else:
        end = guess
        print('太大了！',end="")