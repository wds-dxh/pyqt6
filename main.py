'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-10 15:10:42
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-10 15:10:59
FilePath: /pyqt6/main.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVideoWidget
from PyQt6.QtMultimedia import QMediaPlayer, QMediaContent

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()

        self.setCentralWidget(self.videoWidget)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        self.create_menu()
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

        self.setWindowTitle("Video Player")
        self.resize(640, 480)

    def create_menu(self):
        # 这里可以添加菜单项，如打开文件、播放、暂停等
        pass

    # 下面是媒体状态改变、位置改变、时长改变的槽函数示例，你可以根据需要实现具体逻辑
    def mediaStateChanged(self, state):
        pass

    def positionChanged(self, position):
        pass

    def durationChanged(self, duration):
        pass

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Movie", "", "Movie Files (*.mp4 *.avi *.mkv)")
        if file_name != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            self.mediaPlayer.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec())