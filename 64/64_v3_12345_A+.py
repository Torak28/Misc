import random
import time

import keyboard
import mss
import mss.tools
import pyautogui
from PIL import Image


def grab_screen(name):
    whole_game_screen = {"top": 231, "left": 640, "width": 639, "height": 639}
    img_name = f"full_scr-{str(name)}.png"

    sct_img = sct.grab(whole_game_screen)
    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

    return img, img_name


def grab_bg_color(img):
    colors = []

    rgb_im = img.convert("RGB")
    border = 35
    offset = 80
    width, height = rgb_im.size

    vars = [
        (0 + border + offset, 0 + border),
        (width - border, 0 + border + offset),
        (width - border - offset, height - border),
        (0 + border, height - border - offset),
    ]

    for elem in vars:
        r, g, b = rgb_im.getpixel(elem)

        if (r, g, b) not in colors and (r, g, b) != (0, 0, 0):
            colors.append((r, g, b))

    return colors


def check_blinking(img):
    ans = [sorted(Image.Image.getcolors(img), reverse=True)[0][1]][0]

    if ans == (0, 0, 0):
        return True
    return False


def check_black_amount(lst):
    for elem in lst:
        if elem[1] == (0, 0, 0):
            return elem[0]

    return 0


def check_not_black_amount(lst):
    for elem in lst:
        if elem[1] != (0, 0, 0):
            return elem[0]

    return 0


def check_cols(lst, bg_cols):
    bullets = (216, 207, 100)
    black = (0, 0, 0)

    allowed_colors = [sorted(lst, reverse=True)[0][1]]
    allowed_colors.append(bullets)
    if black not in allowed_colors:
        allowed_colors.append(black)
    for bg_col in bg_cols:
        if bg_col not in allowed_colors:
            allowed_colors.append(bg_col)

    lst = [_[1] for _ in lst]

    return all(x in allowed_colors for x in lst)


def check_orientation(img):
    up_norm = (280, 0, 370, 25)
    down_norm = (280, 614, 370, 639)

    up_cross = (580, 0, 639, 25)
    down_cross = (0, 580, 25, 639)

    img_up_norm = img.crop(up_norm)
    img_down_norm = img.crop(down_norm)
    img_up_cross = img.crop(up_cross)
    img_down_cross = img.crop(down_cross)

    up_region_norm = Image.Image.getcolors(img_up_norm)
    down_region_norm = Image.Image.getcolors(img_down_norm)
    up_region_cross = Image.Image.getcolors(img_up_cross)
    down_region_cross = Image.Image.getcolors(img_down_cross)

    chk_lst_norm = [_[0][1] for _ in [up_region_norm, down_region_norm]]
    chk_lst_cross = [_[0][1] for _ in [up_region_cross, down_region_cross]]
    if (0, 0, 0) not in chk_lst_norm:
        return "Normal"
    elif (0, 0, 0) not in chk_lst_cross:
        return "Crossed"
    return "Transition"


def check_end_screen(img, player_col):
    up = (0, 0, 639, 25)
    down = (0, 614, 639, 639)
    right = (614, 0, 639, 639)
    left = (0, 0, 25, 639)

    img_up = img.crop(up)
    img_down = img.crop(down)
    img_right = img.crop(right)
    img_left = img.crop(left)

    up_region = Image.Image.getcolors(img_up)
    down_region = Image.Image.getcolors(img_down)
    right_region = Image.Image.getcolors(img_right)
    left_region = Image.Image.getcolors(img_left)

    try_again_region = (140, 120, 510, 170)
    try_again_crop = img.crop(try_again_region)
    try_again_cols = [
        x[1] for x in sorted(Image.Image.getcolors(try_again_crop), reverse=True)
    ]

    cols = Image.Image.getcolors(img)

    # success
    if (
        len(up_region) == 1
        and len(down_region) == 1
        and len(right_region) == 1
        and len(left_region) == 1
        and len(cols) == 2
        and player_col in cols
    ):
        return True
    # Try again
    elif try_again_cols == [(0, 0, 0), (255, 255, 255)]:
        return True

    return False


def check_can_move(img, move, bg_cols):
    if move == "idle":
        return True
    black = (0, 0, 0)
    white = (255, 255, 255)

    allowed_colors = [black, white]

    for elem in bg_cols:
        allowed_colors.append(elem)

    if move == "up":
        region = (287, 155, 362, 261)
    elif move == "up + right":
        region = (362, 155, 489, 281)
    elif move == "down":
        region = (287, 369, 363, 484)
    elif move == "down + left":
        region = (150, 349, 287, 484)
    elif move == "right":
        region = (376, 281, 489, 349)
    elif move == "right + down":
        region = (362, 349, 489, 484)
    elif move == "left":
        region = (150, 281, 267, 349)
    elif move == "left + up":
        region = (150, 155, 287, 267)

    img_crp = img.crop(region)
    img_move_cols = Image.Image.getcolors(img_crp)

    black_dots = sorted(img_move_cols)[0]

    if black_dots[1] == (0, 0, 0) and 43 <= black_dots[0] <= 90:
        return False
    lst = [x[1] for x in img_move_cols]

    return all(x in allowed_colors for x in lst)


def add_move_to_heap(move, heap, itx, skip, old_itx, old_move):
    if move[0][1] != "idle":
        if len(heap) == 0:
            if len(move) == 1:
                if move[0][1] != old_move or move[0][0] - old_itx > skip:
                    heap.append(move[0])
            else:
                if move[0][1] != old_move or move[0][0] - old_itx > skip:
                    for elem in move:
                        heap.append(elem)
                        heap.append((itx, "idle"))
        else:
            heap_last_lst = list(filter(lambda x: x[1] != "idle", heap))
            if len(heap_last_lst) == 0:
                heap_last_lst = [(itx, "idle")]
            for elem in move:
                if old_move != elem[1] and heap_last_lst[-1][1] != elem[1]:
                    if heap_last_lst[-1][0] - elem[0] > skip:
                        heap.append(elem)
                        heap.append((itx, "idle"))
                    else:
                        heap.append((itx, "idle"))
                        heap.append(elem)

    return heap


def check_for_enemy(img, i, orientation, blink, bg_cols, ort):
    if ort == "Transition":
        move = [(i, "idle")]
    else:
        potential_enemy = 1400
        potential_enemy_blk = 800

        if orientation == "Normal":
            up = (280, 0, 370, 75)
            down = (280, 564, 370, 639)
            right = (564, 270, 639, 360)
            left = (0, 270, 75, 360)
        elif orientation == "Crossed":
            up = (489, 35, 604, 150)  # U + R
            down = (35, 489, 150, 604)  # D + L
            right = (489, 489, 604, 604)  # R + D
            left = (35, 35, 150, 150)  # L + U

        img_up = img.crop(up)
        img_down = img.crop(down)
        img_right = img.crop(right)
        img_left = img.crop(left)

        up_region = Image.Image.getcolors(img_up)
        down_region = Image.Image.getcolors(img_down)
        right_region = Image.Image.getcolors(img_right)
        left_region = Image.Image.getcolors(img_left)

        print("U: ", up_region)
        print("D: ", down_region)
        print("R: ", right_region)
        print("L: ", left_region)

        move = []

        if blink is False:
            if potential_enemy <= check_black_amount(
                up_region
            ) <= 2 * potential_enemy and check_cols(
                up_region, [sorted(Image.Image.getcolors(img_up), reverse=True)[0][1]]
            ):
                if orientation == "Normal":
                    move.append((i, "up"))
                elif orientation == "Crossed":
                    move.append((i, "up + right"))
            if potential_enemy <= check_black_amount(
                down_region
            ) <= 2 * potential_enemy and check_cols(
                down_region,
                [sorted(Image.Image.getcolors(img_down), reverse=True)[0][1]],
            ):
                if orientation == "Normal":
                    move.append((i, "down"))
                elif orientation == "Crossed":
                    move.append((i, "down + left"))
            if potential_enemy <= check_black_amount(
                right_region
            ) <= 2 * potential_enemy and check_cols(
                right_region,
                [sorted(Image.Image.getcolors(img_right), reverse=True)[0][1]],
            ):
                if orientation == "Normal":
                    move.append((i, "right"))
                elif orientation == "Crossed":
                    move.append((i, "right + down"))
            if potential_enemy <= check_black_amount(
                left_region
            ) <= 2 * potential_enemy and check_cols(
                left_region,
                [sorted(Image.Image.getcolors(img_left), reverse=True)[0][1]],
            ):
                if orientation == "Normal":
                    move.append((i, "left"))
                elif orientation == "Crossed":
                    move.append((i, "left + up"))
        elif blink:
            if potential_enemy_blk <= check_not_black_amount(
                up_region
            ) <= 2 * potential_enemy_blk and check_cols(up_region, bg_cols):
                if orientation == "Normal":
                    move.append((i, "up"))
                elif orientation == "Crossed":
                    move.append((i, "up + right"))
            if potential_enemy_blk <= check_not_black_amount(
                down_region
            ) <= 2 * potential_enemy_blk and check_cols(down_region, bg_cols):
                if orientation == "Normal":
                    move.append((i, "down"))
                elif orientation == "Crossed":
                    move.append((i, "down + left"))
            if potential_enemy_blk <= check_not_black_amount(
                right_region
            ) <= 2 * potential_enemy_blk and check_cols(right_region, bg_cols):
                if orientation == "Normal":
                    move.append((i, "right"))
                elif orientation == "Crossed":
                    move.append((i, "right + down"))
            if potential_enemy_blk <= check_not_black_amount(
                left_region
            ) <= 2 * potential_enemy_blk and check_cols(left_region, bg_cols):
                if orientation == "Normal":
                    move.append((i, "left"))
                elif orientation == "Crossed":
                    move.append((i, "left + up"))

    return move if len(move) != 0 else [(i, "idle")]


if __name__ == "__main__":
    sct = mss.mss()
    itx = 0
    old_itx = 0
    old_move = "idle"
    flag = True
    pause = 0.9
    debug = True
    mode = "Far"
    prev_orientation = "Normal"
    bg_cols = [(255, 255, 255)]
    player_col = (131, 131, 131)
    skip_move = 2 if debug else 15
    moves_heap = []
    move_tick = 0

    pyautogui.click(x=900, y=400)
    move = (itx, "up")
    keyboard.send(move[1], do_press=True, do_release=True)
    time.sleep(pause)

    while flag:
        scr, scr_name = grab_screen(itx)
        scr_bg_cols = grab_bg_color(scr)
        scr_ort = check_orientation(scr)
        scr_blk = check_blinking(scr)

        if scr_blk:
            scr_ort = prev_orientation
        else:
            prev_orientation = scr_ort

        if scr_bg_cols == []:
            scr_bg_cols = bg_cols
        else:
            bg_cols = scr_bg_cols

        print(f"i: {itx}")
        print(f"ort: {scr_ort}")
        print(f"bg: {scr_bg_cols}")
        print(f"blk: {scr_blk}")
        new_move = check_for_enemy(scr, itx, scr_ort, scr_blk, scr_bg_cols, scr_ort)

        moves_heap = add_move_to_heap(
            new_move, moves_heap, itx, skip_move, old_itx, old_move
        )

        print(f"moves_heap: {moves_heap}")
        if len(moves_heap) != 0:
            if check_can_move(scr, moves_heap[0][1], scr_bg_cols):
                acc_move = moves_heap.pop(0)
                if acc_move[1] != "idle":
                    old_itx = itx
                    old_move = acc_move[1]
                    keyboard.send(acc_move[1], do_press=True, do_release=True)
                print(f"Move: {acc_move}")

        itx += 1

        if debug:
            scr.save(scr_name)
        else:
            time.sleep(0.01)
        print("---")
        # teoretycznie mógłbym sprawdzić ekran kończący lepiej xd
        flag = not check_end_screen(scr, player_col)

    scr.save(scr_name)
