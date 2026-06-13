import numpy as np
import cv2 as cv

img = cv.imread('materials\Resources\Photos\lady.jpg')

is_gray = False
is_blured = False
is_canny = False
is_rotated = False
is_flipped = False


while True:
    key = cv.waitKey(50) & 0xff
    result = img.copy()
    mode_text = []

    if key == ord('g'):
        is_gray = not is_gray
    elif key == ord('b'):
        is_blured = not is_blured
    elif key == ord('e'):
        is_canny = not is_canny
    elif key == ord('r'):
        is_rotated = not is_rotated
    elif key == ord('f'):
        is_flipped = not is_flipped
    elif key == ord('d'):
        break

    if is_gray:
        result = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
        mode_text.append('gray')
    if is_blured:
        result = cv.GaussianBlur(result,(15,15),cv.BORDER_DEFAULT)
        mode_text.append('blurred')
    if is_canny:
        result = cv.Canny(result,125,175)
        mode_text.append('edges')
    if is_rotated:
        result = cv.rotate(result,cv.ROTATE_90_CLOCKWISE)
        mode_text.append('rotated')
    if is_flipped:
        result = cv.flip(result,0)
        mode_text.append('flipped')
    
    if len(result.shape) == 2:
        result = cv.cvtColor(result, cv.COLOR_GRAY2BGR)
    mode_str = "Mode: " + " + ".join(mode_text) if mode_text else "Mode: normal"
    cv.putText(result, f'{mode_str}',(10,30),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=2)
    cv.imshow('Photo editor', result)

cv.destroyAllWindows()