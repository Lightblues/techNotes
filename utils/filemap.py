""" 定义 rsyn 文件同步位置
1. 要求两个目录下的文件 **同名**
2. 注意不要有空格等特殊符号
 """

document_dir = ""
technote_dir = ""

# 定义文件同步位置
# 主要要保证文件不同名
filemap = {
    # code
    # Python
    "Python-note": ["510-Python", "Python"],
    # JavaScript
    "js-note": ["550-languages", "JavaScript"],
    "js-mindmap": ["550-languages", "JavaScript"],
    "node-js-note": ["550-languages", "JavaScript"],
    "jQuery": ["550-languages", "JavaScript"],


    # Linux
    "实验环境相关": ["800-Linux", "Linux"],
    "Linux": ["800-Linux", "Linux"],
    "Linux-maintain": ["800-Linux", "Linux"],

    # os
    "Arch": ["810-OS", "os"],
    "CentOS": ["810-OS", "os"],
    "Ubuntu": ["810-OS", "os"],
    "macOS": ["810-OS", "os"],
    "Windows": ["810-OS", "os"],
    "Hackintosh": ["810-OS", "os"],
    "EFI": ["810-OS", "os"],
    
    # stat
    "ASL-mindmap": ["stat", "110-stat"],
    "ASL-notes": ["stat", "110-stat"],
    "ASL-notes2": ["stat", "110-stat"],
    "ASL-notes3": ["stat", "110-stat"],
    "ASL-notes4": ["stat", "110-stat"],
}

""" 
1. 构建 {文件夹: 路径} 的字典
2. 增量同步
3. 对应同步图片文件下, 对于没有的文件夹, 创建文件夹
 """