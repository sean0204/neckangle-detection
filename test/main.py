import dlib
import cv2

print(cv2.__version__)
# 選擇第一隻攝影機
cap = cv2.VideoCapture(1)
# 調整預設影像大小，預設值很大，很吃效能
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
cap_Width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
cap_Height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("解析度= %d x %d"%(cap_Width,cap_Height))
# 取得預設的臉部偵測器
#detector = dlib.get_frontal_face_detector()
# 根據shape_predictor方法載入68個特徵點模型，此方法為人臉表情識別的偵測器
#predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
# 當攝影機打開時，對每個frame進行偵測
j=1
while (cap.isOpened()):
    # 讀出frame資訊
    ret, frame = cap.read()

    # 偵測人臉
    
    # 輸出到畫面
    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(10) == ord('h'):
        path = "./image %d.jpg"%(j)
        cv2.imwrite(path, frame)
        j+=1
        print("save image {} ".format(j))
    # 如果按下ESC键，退出
    if cv2.waitKey(10) == 27:
        break
# 釋放記憶體
cap.release()
# 關閉所有視窗
cv2.destroyAllWindows()