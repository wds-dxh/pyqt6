# pyqt6的安装

1. 注意换源
2. 安装qt6-tools，然后找到designer
3. 使用vscode编辑的时候，配置任务文件

```json
{  
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",  
    "tasks": [  
        {  
            "label": "PyQt6 UI to Python",  
            "type": "shell",  
            "command": "python",  
            "args": [  
                "-m",  
                "PyQt6.uic.pyuic",  
                "${file}",  
                "-o",  
                "${fileDirname}/${fileBasenameNoExtension}.py"  
            ],  
            "problemMatcher": [],  
            "group": {  
                "kind": "build",  
                "isDefault": true  
            }  
        }  

        {  
            "label": "Run PyQt6 Designer",  
            "type": "shell",  
            "command": "designer.exe",  
            "windows": {  
                "command": "designer.exe" // 如果在 PATH 中，直接使用名称  
            },  
            "linux": {  
                "command": "designer" // 在 Linux 上，可能没有 .exe 扩展名  
            },  
            "mac": {  
                "command": "/path/to/designer" // 在 macOS 上，你可能需要指定完整路径  
            },  
            "problemMatcher": [],  
            "group": {  
                "kind": "other",  
                "isDefault": false  
            }  
        }  
    ]  
    
}
```

# QDate，QTime，QDateTime

## 1. current_date_time

```python
"""
1. QDate、QTime、QDateTime类提供了日期、时间和日期时间的功能。
2.都有currentDate()、currentTime()、currentDateTime()静态方法，返回当前日期、时间和日期时间。
3.可以使用toString()方法将日期、时间和日期时间转换为字符串。（可以使用Qt.DateFormat枚举值指定格式）
--Qt.DateFormat枚举值：ISODate：国际标准日期格式；RFC2822Date：RFC2822日期格----中国是ISODate
"""
```

## 2.daylight_saving- 夏令时

```python
"""
总结--DST是夏令时的缩写，是一种节约能源的方式，通过在夏季调整时钟来节约能源。
这个例子展示了如何使用PyQt6获取夏令时信息。
1.我们使用QDateTime.currentDateTime()方法获取当前日期和时间。
2.我们使用QDateTime.isDaylightTime()方法检查当前日期是否在夏令时。
3.timeZoneAbbreviation()方法返回当前时区的缩写。

"""
```

## 3. UTC时间

```python
"""
1. QDateTime类的toUTC()方法将本地时间转换为UTC时间。
2. QDateTime类的offsetFromUtc()方法返回本地时间与UTC时间之间的偏移量（以秒为单位）。
"""
```



# 常用基本控件

## 程序基本结构

```python
from PyQt6.QtWidgets import QApplication
from PyQt6 import uic
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    w = QWidget() # 创建一个窗口
    
    sys.exit(app.exec())    
```



## Qlabel 标签控件

1. 对齐方式
2. 是否设置超链接
3. 获取标签文本
4. 设置换行显示
5. 为标签设置图片





