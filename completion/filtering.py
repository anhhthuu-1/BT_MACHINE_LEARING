from numpy import nan as NA
import pandas as pd
 #filtering la luoc di theo dieu kien, loại dữ liệu khỏi  dataset theo dieu kien bai toan
data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)
print("-"*10)
cleaned = data.dropna() #xóa các dòng có NA
print(cleaned)
print("-"*10)
cleaned2=data.dropna(how='all') #chỉ xóa các dòng mà tất cả đều NA
print(cleaned2)


