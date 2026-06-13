import cv2 as cv

img = cv.imread('materials\Resources\Photos\cat.jpg')
cv.imshow('cat', img)


def rescaleFrame(frame, scale=0.2):
    width =int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimentions = (width,height)

    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)


def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)


capture = cv.VideoCapture('materials/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()