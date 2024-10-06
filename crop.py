import cv2

def by_cords(image, x1, y1, x2, y2):
    return image[y1:y2, x1:x2]

def shop_cells(image):
    slot_width = 189
    gutter_width = 12
    gutter_fix = 0

    crops = []
    for i in range(5):
        if i == 3:
            gutter_fix = 1
        crops.append(by_cords(image, 481+(slot_width * i + gutter_width * i + gutter_fix), 952, 481+(slot_width * (i + 1) + gutter_width * i + gutter_fix), 1070))
    return crops


def shop_window(image):
    return by_cords(image, 481, 952, 1476, 1070)


def cells_of_shop_window(shop_window_image):
    slot_width = 189
    gutter_width = 12
    gutter_fix = 0

    crops = []
    for i in range(5):
        if i==3 :
            gutter_fix = 1
        crops.append(by_cords(shop_window_image, slot_width * i + gutter_width * i + gutter_fix, 0, slot_width * (i + 1) + gutter_width * i + gutter_fix,118))
    return crops


def crop_of_cell(cell_image):
    return by_cords(cell_image, 0, 85, 155, 118)


def is_cell_empty(crop):
    pixels = 10
    thresh_val = 50
    maxval = 255

    summ = 0

    grayscale_crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    grayscale_crop_resize = cv2.resize(grayscale_crop, (pixels, pixels), cv2.INTER_NEAREST)
    blurred_grayscale_crop_resize = cv2.GaussianBlur(grayscale_crop_resize, (7, 7), 0)
    (T, thresh_blurred_grayscale_crop_resize) = cv2.threshold(blurred_grayscale_crop_resize, thresh_val, maxval,
                                                              cv2.THRESH_BINARY)

    for x in range(pixels):
        for y in range(pixels):
            if thresh_blurred_grayscale_crop_resize[x][y] == maxval:
                summ += 1

    return summ / (pixels * pixels) == 0