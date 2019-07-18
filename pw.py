#密碼重設程式

password = 'a123456'
x = 3 
x > 0
while True:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功')
        break
    else:
        print('密碼錯誤!還有', x - 1, '次機會')
        x = x - 1
        if x == 0:
            break

     

