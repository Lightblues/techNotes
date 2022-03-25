""" 
定义 rsync 文件同步位置
1. 要求两个目录下的文件 **同名**
2. 注意不要有空格等特殊符号
 """

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
    "jQuery-note": ["550-languages", "JavaScript"],
    # CS
    "git-note": ["400-CS", "CS"],

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
    "ASL-mindmap": ["110-stat", "stat"],
    "ASL-note": ["110-stat", "stat"],
    "ASL-note2": ["110-stat", "stat"],
    "ASL-note3": ["110-stat", "stat"],
    "ASL-note4": ["110-stat", "stat"],
}
