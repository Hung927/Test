# num = input('number：')
# time = int(input('times：'))
# temp = ''
# ans = 0
# for i in range(time):
#     temp += num
#     ans += int(temp)
    
# print(ans)

# for i in range(1, 11):s

# even_pow = {i: i**2 for i in range(1, 11) if not (i % 2)}
# print(even_pow)


# import pandas as pd

# # 建立 Series 物件，傳入 list 當作參數
# series_1 = pd.Series([2, 1, 7, 3])

# print(series_1)


def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)




