'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-10 14:25:28
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-10 14:27:02
FilePath: /pyqt6/Layout_management/review.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
#!/usr/bin/python
# file: review.py



import sys
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
        QTextEdit, QGridLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()    # 创建一个网格布局
        grid.setSpacing(10)     # 设置控件之间的间距

        grid.addWidget(title, 1, 0)# 将标题放到第1行第0列
        grid.addWidget(titleEdit, 1, 1)# 将标题编辑框放到第1行第1列

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)    # 将评论放到第3行第0列
        grid.addWidget(reviewEdit, 3, 1, 5, 1)# 将评论编辑框放到第3行第1列，占据5行. (5,1)是一个单元格

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()