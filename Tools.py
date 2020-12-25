# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 上午9:16
# @Author  : gui
# @File    : Tools.py
# @Software: PyCharm

import os
import datetime


def set_cam_mode(exposure_auto=True):
    """
    设置两个相机为自动曝光或手动曝光
    :param exposure_auto:
    :return:
    """
    if exposure_auto:
        # 自动曝光
        os.system("v4l2-ctl -d /dev/video0 -c exposure_auto=3")
        os.system("v4l2-ctl -d /dev/video1 -c exposure_auto=3")
    else:
        # 手动曝光
        os.system("v4l2-ctl -d /dev/video0 -c exposure_auto=1")
        os.system("v4l2-ctl -d /dev/video1 -c exposure_auto=1")


def take_photo_by_fswebcam(root, file_prefix=""):
    """
    使用fswebcam拍摄照片
    :param root: 照片存放的路径
    :param file_prefix: 照片名前缀
    :type root str
    :type file_prefix str
    :return:
    """
    # root = "./tmp/"
    if root[-1] != "/":
        root += "/"
    # 获取时间戳，生成要保存文件名称
    time_str = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    dir_str = root + datetime.datetime.now().strftime("%Y-%m-%d")
    if not os.path.isdir(dir_str):
        try:
            os.mkdir(dir_str)
            print("new" + dir_str)
        except Exception as e:
            print(e)
    file_name = dir_str + "/" + file_prefix + time_str
    print(file_name)
    # "fswebcam -d /dev/video0 -r 3264x2448 --no-banner " + root + time_str + "-CAP0.jpg"
    tmp = "fswebcam -r 3264x2448 --no-banner -s 5 --png 0 "
    try:
        os.system(tmp + " -d /dev/video0 " + file_name + "-CAP0.png")
        os.system(tmp + " -d /dev/video1 " + file_name + "-CAP1.png")
    except Exception as e:
        print(e)
        return False
    return True


if __name__ == "__main__":
    take_photo_by_fswebcam("./tmp")
