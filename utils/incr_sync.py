""" @220325
增量同步

1. 构建 {文件夹: 路径} 的字典
2. 增量同步
3. 对应同步图片文件下, 对于没有的文件夹, 创建文件夹
 """
import os
import glob
import filecmp # 比较文件是否相同
import subprocess

# 定义了文件名映射, 例如 "Python-note": ["510-Python", "Python"],
from filename_map import filemap

document_dir = "/Users/frankshi/Library/Mobile Documents/iCloud~com~coderforart~iOS~MWeb/Documents"
technote_dir = "/Users/frankshi/Projects/03-blog/techNotes/docs"

def get_dir2path(path, dir2path={}):
    """ 构建 {文件夹名: 文件夹路径} 的map """
    # for root, dirs, files in os.walk(path):
        # for dir in dirs:
        #     if dir.startswith(".") or dir in ["meida"]:
        #         continue
        #     dir2path[dir] = os.path.join(root, dir)
    for name in os.listdir(path):
        # 遍历所有的目录 1. 非隐藏; 2. 非 media文件夹; 
        p = f"{path}/{name}"
        if os.path.isfile(p):
            continue
        if name.startswith(".") or name in ["meida"]:
            continue
        # md文件夹的条件: 其中有 md文件
        items = os.listdir(p)
        if len(items)==0 or any(i.endswith(".md") for i in items):
            # 要求文件夹不同名!
            assert name not in dir2path
            dir2path[name] = p
        else:
            # 递归
            dir2path = get_dir2path(p, dir2path)
    return dir2path

# def get_md_paths(dir):
#     """ 利用 glob 得到所有 md 文件的路径 """
#     paths = glob.glob(f"{dir}/**/*.md", recursive=True)
#     return paths
# get_md_paths(technote_dir)


def incr_sync(name, src_dir, dest_dir):
    # 增量同步
    # 1. 文件
    src = f"{doc_dir2path[src_dir]}/{name}.md"
    dest = f"{tech_dir2path[dest_dir]}/{name}.md"
    if os.path.exists(dest) and filecmp.cmp(src, dest):
        return
    print(f"[sync] {name}")
    subprocess.run(["rsync", "-av", src, dest])
    
    # 2. 图片文件夹
    src, dest = f"{doc_dir2path[src_dir]}/media/{name}", f"{tech_dir2path[dest_dir]}/media/"
    if not os.path.exists(dest):
        os.makedirs(dest)
    if not os.path.exists(src):
        return
    subprocess.run(["rsync", "-av", src, dest])

# main
doc_dir2path = get_dir2path(document_dir, {})
tech_dir2path = get_dir2path(technote_dir, {})
for name, (src_dir, dest_dir) in filemap.items():
    # 同步文件
    incr_sync(name, src_dir, dest_dir)