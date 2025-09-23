from sklearn.datasets import fetch_california_housing
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#ví dụ 1
# Giả sử người dùng tìm kiếm "best smart phone 2025" ==> https://www.techadvisor.com/article/724318/best-phone.html
#Data set mô phổng ( 2 features mô tả mỗi doc + relevance lable)
#Fearures : [Độ phổ biến, độ liên quan tới keyword]
X = np.array([
        [0.7,0.92], #Google Pixel 10 Pro XL
        [0.9, 0.85], #Samsung Galaxy S25 Ultra
        [0.6, 0.68], #OnePlus 13
        [0.8, 0.74], #Xiaomi 15 Ultra
        [0.5, 0.72], #Oppo Find X8 Pro
        [0.9, 0.65], #Iphone 16 plus
        [0.4, 0.57], #Google Pixel 9a
        [0.3, 0.45], #Nothing Phone (3a)
        [0.2, 0.36], #CMF Phone 2 Pro
        [0.7, 0.51], #Google Pixel 10
        [0.1, 0.15], #Nokia 3310
        [0.7, 0.67],  # Samsung Z Flip
        [0.4, 0.52],  # Oppo Reno
                ])
# Nhãn thực (relevance: 3 = rất liên quan, 0 = không liên quan)
y = np.array([
    3,  # Google Pixel 10 Pro XL (rất liên quan)
    3,  # Samsung Galaxy S25 Ultra
    2,  # OnePlus 13
    2,  # Xiaomi 15 Ultra
    2,  # Oppo Find X8 Pro
    2,  # iPhone 16 Plus
    1,  # Google Pixel 9a
    1,  # Nothing Phone (3a)
    1,  # CMF Phone 2 Pro
    2,  # Google Pixel 10
    0,  # Nokia 3310 (không liên quan)
    2,  # Samsung Z Flip
    1   # Oppo Reno
])

# Huấn luyện hồi quy
model = LinearRegression()
model.fit(X, y)

#Dự đoán
y_pred = model.predict(X)

#tính MSE loss
mse = mean_squared_error(y, y_pred)

print("Dự đoán điểm (Predicted scores:", y_pred.round(2))
print("MSE loss:", mse)

#sau khi chạy mô hình ta có kết quả: SS galaxy là có mức độ liên quan cao nhất ~ 2.76/3

#ví dụ 2
#Giả sử người mua muốn tìm "Nhà có giá vừa phài, diện tích rộng và phải gần trung tâm".
#Sử dụng bộ data từ thư viên sklearn- thông tin về nhà ở ở bang California Mỹ (~20000 mẫu)

data = fetch_california_housing(as_frame=True)
df = data.frame

#Ta lấy 5 đặc trưng:  MedInc- Thu nhập tb (nghìn usd), HouseAge- Tuổi trung bình của căn nhà, AveRooms- số phòng trung bình, Latitude - Vĩ độ (32-42*), Longitude - Kinh độ (-124* - -114*)
X = df[["MedInc", "HouseAge", "AveRooms", "Latitude", "Longitude"]].values
# Tạo nhãn relevance (0–3) mô phỏng người dùng quan tâm:
# - Người dùng thích thu nhập trung bình cao, nhà mới, phòng rộng, gần trung tâm (lat ~ 34-37, lon ~ -118 đến -121)
relevance = (
    (df["MedInc"] > 5).astype(int) +
    (df["HouseAge"] < 20).astype(int) +
    (df["AveRooms"] > 5).astype(int) +
    ((df["Latitude"].between(34, 37)) & (df["Longitude"].between(-121, -118))).astype(int)
)

y = relevance.clip(0, 3)  # đảm bảo trong khoảng 0–3

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Huấn luyện Linear Regression (Pointwise)
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán relevance score
y_pred = model.predict(X_test)

# Đánh giá
mse = mean_squared_error(y_test, y_pred)

print("Sample predicted scores:", y_pred[:10])
print("True labels:", y_test[:10].tolist())
print("MSE Loss:", mse)
#Bài toán chưa thực su tối ưu do có nhiều kqua dự đoán bị lệch