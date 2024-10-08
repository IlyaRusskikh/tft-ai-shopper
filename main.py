from ultralytics import YOLO
import json
import crop
from window_capture import window_capture
import controller
import torch
import time


if not torch.cuda.is_available():
    print('CUDA is not available ;(')
    time.sleep(2)
    for t in range(3):
        print(f'process will close in {3-t}...')
        time.sleep(1)
    exit(0)

with open('source/settings.txt', encoding='utf-8', mode='r') as f_in:
    settings_vars = json.load(f_in)

with open(f'source/wish_lists/{settings_vars["wish_list"]}', encoding = 'utf-8', mode='r') as f_in:
    necessary = json.load(f_in)

model = YOLO(f"source/models/{settings_vars['model']}", task='classify')
win_cap = window_capture()
previous_shop = current_shop = [None, None, None, None, None]
block_actions = False
buy_list = dict()
necessary_refresh = 0

print(f'Model {settings_vars['model']} successfully loaded!\nReady to buy units from {settings_vars["wish_list"]}\nGood luck!')

while True:
    if necessary_refresh > settings_vars["wish_list_refresh_value"]:
        with open(f'source/wish_lists/{settings_vars["wish_list"]}', encoding='utf-8', mode='r') as f_in:
            necessary = json.load(f_in)
        necessary_refresh = 0
    else:
        necessary_refresh += 1

    screenshot = win_cap.get_screenshot()
    crops = crop.shop_cells(screenshot)
    res = model.predict(crops, verbose=False, stream=True)
    cur_index = 0

    for r in res:
        if r.probs.top1conf.item() > settings_vars["conf"]:
            current_shop[cur_index] = r.names[r.probs.top1]
        else:
            current_shop[cur_index] = None
        cur_index += 1

    if not previous_shop == current_shop:
        del buy_list
        buy_list = dict()

    for buy_list_index in list(buy_list):
        if crop.is_cell_empty(crops[buy_list_index]):
            del buy_list[buy_list_index]
    if len(buy_list) > 0:
        block_actions = True
    else:
        block_actions = False

    if current_shop == [None, None, None, None, None] and block_actions:
        block_actions = False

    if not block_actions:
        for current_shop_item in current_shop:
            if current_shop_item in necessary:
                controller.buy_unit(current_shop.index(current_shop_item), settings_vars["beforeclick_delay"], settings_vars["afterclick_delay"])
                buy_list[current_shop.index(current_shop_item)] = current_shop_item

    previous_shop = current_shop