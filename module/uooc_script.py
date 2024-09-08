import time

import cv2
import numpy as np

from core import picture, color
from core import image


def UI_from_Schedule_GO_TO_Course(self):
    img_possibles = {
        "uooc_UI-at-Home": (362, 1240),
        "uooc_UI-at-Schedule": (330, 269),
        "uooc_UI-at-My": (362, 1240),
    }
    img_ends = "uooc_UI-at-Course"
    picture.co_detect(self, None, None, img_ends, img_possibles)


def implement(self):
    # UI_from_Schedule_GO_TO_Course(self)
    swiped = False
    while self.flag_run:
        self.latest_img_array = self.get_screenshot_array()
        position = get_video_position(self)
        self.logger.info("Video positions detected : " + str(position))
        for i in range(len(position)):
            p = position[i]
            if this_video_watched(self, p):
                continue
            else:
                self.click(p[0] + 32, p[1] + 19)
                while self.flag_run:
                    time.sleep(1)
                    self.latest_img_array = self.get_screenshot_array()
                    if check_this_video_over(self):
                        self.logger.info("Video at " + str(p) + " is over.")
                        break
                if i != len(position) - 1 and swiped:
                    swiped = False
                    break
        else:
            self.u2_swipe(377, 1195, 377, 530, 1)
            swiped = True
            time.sleep(1)



def get_video_position(self):
    region = (93, 481, 190, 1280)
    video_template = image.getImageByName(self, "uooc_video-template")
    cut_img = image.screenshot_cut(self, region)
    res = cv2.matchTemplate(cut_img, video_template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    res = []
    for pt in zip(*loc[::-1]):
        res.append((pt[0] + region[0], pt[1] + region[1]))
    return res


def check_this_video_over(self):
    return image.compare_image(self, "uooc_video-end-feature")


def this_video_watched(self, position):
    region = (position[0] - 50, position[1], position[0] - 10, position[1] + 35)
    for i in range(region[0], region[2]):
        for j in range(region[1], region[3]):
            if color.judge_rgb_range(self, i, j, 0, 20, 180, 210, 0, 20):
                self.logger.info("Video at " + str(position) + " has been watched.")
                return True
    return False

