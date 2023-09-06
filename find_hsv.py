import cv2
import numpy as np

def get_hsv_value(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_pixel = hsv_image[y, x]
        print(f'Hue (색상): {hsv_pixel[0]}')
        print(f'Saturation (채도): {hsv_pixel[1]}')
        print(f'Value (명도): {hsv_pixel[2]}')

# 이미지를 불러오기
image = cv2.imread('/home/jua/바탕화면/B2/B2_8_9_blue_66_resized.jpg')

# BGR 이미지를 HSV로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', get_hsv_value)

while True:
    cv2.imshow('Image', image)
    if cv2.waitKey(10) & 0xFF == 27:  # ESC 키를 누르면 종료
        break

cv2.destroyAllWindows()
