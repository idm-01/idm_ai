import cv2
import numpy as np
import time
import gpsd
import fnc

# Рамки выделяемого цвета в схеме HSV
# в пределах которых находится цвет льда
ice_l = np.array([65, 0, 135])
ice_h = np.array([250, 90, 280])
# Список собирающий выходные данные
Output = []

# Цикл, собирающий изображения с камеры на протяжении миссии,
# анализируя их и выдавая результат
while True:
    # Захват изображения
    cap = cv2.VideoCapture(0)
    ret, src = cap.read()
    cv2.waitKey(1)
# Создание маски, отображающей лёд
    img = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img, ice_l, ice_h)
    res = cv2.bitwise_and(src, src, mask=mask)
# Расчёт густоты льда в процентах
    ice = np.sum(mask == 255)
    oth = np.sum(mask == 0)
    ice_per = ((ice / (oth + ice)) * 100 // 1)
    ice_per = int(ice_per)
# Расчёт координат
    lat = (GPS.kakoyto_metod())
    lon = (GPS.kakoyto_metod())
    gps = (lat, lon)
# Сохранение результата
    print(ice_per, gps)
    resulut = (ice_per, gps)
    Output.append(resulut)
    cv2.imwrite((r'C:\Users\turoko\PycharmProjects\IDM CV\output\src.png'), src)
    cv2.imwrite((r'C:\Users\turoko\PycharmProjects\IDM CV\output\res.png'), res)
    # Промежуток между захватами изображений в секундах
    time.sleep(10)


