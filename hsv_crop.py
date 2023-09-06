import cv2
import numpy as np
import os

# 입력 이미지 폴더 경로
input_folder = '/home/jua/바탕화면/test/B2'  # 폴더 경로를 적절히 변경하세요

# 결과를 저장할 폴더 경로
output_folder = '/home/jua/바탕화면/B2'  # 폴더 경로를 적절히 변경하세요
os.makedirs(output_folder, exist_ok=True)

# 입력 폴더에서 모든 파일 가져오기
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.png')):  # JPG 또는 PNG 파일인 경우만 처리
        # 이미지 파일 경로 생성
        image_path = os.path.join(input_folder, filename)

        # 이미지 불러오기
        image = cv2.imread(image_path)

        # 이미지를 HSV 색 공간으로 변환
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # 파란색 범위 설정 (HSV)
        lower_blue = np.array([80, 50, 50])  # 하한값을 낮게 설정
        upper_blue = np.array([130, 255, 255])  # 상한값을 높게 설정

        # 파란색 범위에 해당하는 부분을 마스크로 생성
        blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

        # 마스크를 사용하여 이미지에서 파란색 부분 찾기
        contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 각 파란색 영역을 개별적인 파일로 저장
        for i, contour in enumerate(contours):
            x, y, w, h = cv2.boundingRect(contour)
            blue_cropped = image[y:y+h, x:x+w]
            output_filename = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}_blue_{i}.jpg')
            cv2.imwrite(output_filename, blue_cropped)

print("처리가 완료되었습니다.")
