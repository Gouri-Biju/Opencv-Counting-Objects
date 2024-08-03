import cv2
def candy_count(image):
    cv2.imshow('input', image)
    cv2.waitKey(-1)

    # greyscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('output', gray)
    cv2.waitKey(-1)

    # Blured
    blured = cv2.GaussianBlur(gray, (3, 3), None)
    image = cv2.imshow('blurred', blured)
    cv2.waitKey(-1)

    # converting to binary using given values
    # image = cv2.imread('./image/many_m_n_m.jpg', cv2.IMREAD_GRAYSCALE)
    # height, width = image.shape
    # for row in range(height):
    #     for col in range(width):
    #         if image[row, col] > 220:
    #             image[row, col] = 0
    #         else:
    #             image[row,col] = 255
    # cv2.imshow('output', image)
    # cv2.waitKey(-1)

    # binary(threshhold func)
    retval, binary = cv2.threshold(blured, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('binary', binary)
    cv2.waitKey(-1)

    # adaptive threshholding
    binary_threshAdap = cv2.adaptiveThreshold(blured, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    cv2.imshow('binary_threshAdap', binary_threshAdap)
    cv2.waitKey(-1)

    contours, hierarchy = cv2.findContours(binary_threshAdap, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    big_contours = 0
    image = cv2.imread('./image/many_m_n_m.jpg')
    for index, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        print(index, area)
        if area > 1000:
            big_contours = big_contours + 1
            print("taking counter at index : ", index)
            cv2.drawContours(image, [cnt], -1, (0, 255, 0), 3)
            cv2.imshow('image', image)
            cv2.waitKey(400)
        else:
            print("ignoring counter at index : ", index)

    count = big_contours
    cv2.putText(image, f"Number of Counters : {count}", (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('image', image)
    cv2.waitKey(400)
    cv2.waitKey(-1)

if __name__ =='__main__':
    print('ran directly')
    image = cv2.imread('./image/many_m_n_m.jpg')
    candy_count(image)