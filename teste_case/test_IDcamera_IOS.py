from airtest.core.api import *
import unittest
from GlobalVariable import globalvar
import warnings
import logging

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class testidCamera(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        connect_device("iOS:///127.0.0.1:8100")

    def setUp(self):
        start_app('com.vstudio.idcamerason')
        sleep(3.0)
        print("启动最美证件照")

    def test_demo(self):
        """启动测试"""
        touch(globalvar.首页相册icon)
        # 点击首页相册的icon
        sleep(2.0)
        if exists(globalvar.相册页面title):
            # 判断是否点击了相册的icon
            print("进入相册页成功")
        else:
            print("进入相册页失败")
        touch(globalvar.相册页_系统相册)
        # 点击相册页的系统相册icon
        sleep(3)
        if exists(globalvar.app相册权限弹窗):
            print("未同意相册权限")
            if exists(globalvar.app相册权限弹窗):
                # 判断是否出现了证件照的允许访问相册的权限弹窗
                print("出现了证件照的允许访问相册的权限弹窗")
            else:
                print("test出现了证件照的允许访问相册的权限弹窗失败")
            if exists(globalvar.app相册权限弹窗):
                # 点击app相册弹窗同意
                print("点击app相册弹窗的同意")
            else:
                print("test点击app相册弹窗的同意失败")
            touch(globalvar.app相册弹窗同意按钮)
            # 点击app相册弹窗同意按钮
            sleep(3)
            if exists(globalvar.系统相册权限弹窗):
                print("出现系统相册权限弹窗")
            else:
                print("test出现系统相册权限弹窗失败")
            touch(globalvar.系统相册权限弹窗同意按钮)
        else:
            print("已经同意相册权限")
        if exists(globalvar.app水印提示弹窗):
            print("出现水印提示按钮")
        else:
            print("test出现水印提示按钮失败")
        touch(globalvar.app水印提示弹窗同意按钮)
    #     点击水印同意按钮
        if exists(globalvar.进入相册):
            print("进入相册了")
        else:
            print("Test进入相册了失败")
        touch(globalvar.点击香浦)
        print("点击香蒲")
        if exists(globalvar.点击Test相册):
            print("出现Test相册")
        else:
            print("没有出现Test相册")
        touch(globalvar.点击Test相册)
        print("点击Test相册")
        touch(globalvar.点击测试图片)
        print("点击测试图片")
        if exists(globalvar.进入编辑页):
            print("进入编辑")
        else:
            print("Test进入编辑失败")

    def tearDown(self):
        home()
    @classmethod
    def tearDownClass(cls):
        stop_app("com.vstudio.idcamerason")
