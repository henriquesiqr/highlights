import cv2
 
caps = []
 
for i in range(3):
    cap = cv2.VideoCapture(i)
 
    if cap.isOpened():
        caps.append((i, cap))
        print(f"Câmera {i} aberta.")
 
while True:
    for i, cap in caps:
        ret, frame = cap.read()
 
        if ret:
            cv2.imshow(f"Camera {i}", frame)
 
    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break
 
for _, cap in caps:
    cap.release()
 
cv2.destroyAllWindows()