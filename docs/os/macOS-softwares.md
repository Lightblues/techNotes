
!!! note
    整理在用/尝试过的软件

## Homebrew+shell

- <https://brew.sh/>
- <https://formulae.brew.sh/>
- [程序员 Homebrew 使用指北](https://sspai.com/post/56009) 一篇非常全面的介绍 Homebrew 的文章，包括了如何将 Homebrew 安装的软件全部迁移到新设备等

### zsh+conda+软件安装

```bash
# 安装 brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# vim 复制已有的配置文件
cp code/00-config/configs/shell/.vimrc ~/

# 配置 zsh
brew install --cask iterm2      # iterm2
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
chsh -s $(which zsh) # 似乎  Monterey 默认就是 zsh?
# ! 因为备份了配置, 直接复制过来
cp code/00-config/configs/shell/.zshrc ~/
source ~/.zshrc
# 安装插件: zsh-syntax-highlighting, zsh-autosuggestions autojump
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
brew install autojump # j
source ~/.zshrc

# 基本软件
brew install htop   # htop
brew install tree   # tree
brew install trash  # 用 trash 替换 rm
brew install carlocab/personal/unrar # x=extract 解压 rar 文件调用
brew install bat    # 增强 cat

# 
brew isstall wget

# VS Code; Sublime
brew install --cask visual-studio-code # 官方下载安装包好慢来着
brew install --cask sublime-text

# conda
brew install --cask miniconda
conda init zsh

# go
brew install go # VS Code 可以自动识别安装相关调试工具

# Applications
brew install --cask neteasemusic # 网易云音乐
brew install --cask iina # IINA
brew install --cask wechat qq # WeChat QQ
brew install --cask keka # 压缩软件

# Tools
brew install --cask utools # uTools
brew install --cask eudic # 欧路词典
brew install --cask karabiner-elements # 改键
```

记录一下目前安装列表

```bash
(base) ➜  code brew list
==> Formulae
autojump gdbm  mpdecimal python@3.10 sqlite  tree
ca-certificates go  openssl@1.1 readline trash  xz

==> Casks
eudic   miniconda  qq   visual-studio-code
iina   neteasemusic  sublime-text  wechat
iterm2   popclip
```

### 常用 brew 命令

常用的有 `search, install, info, services` 等

```sh
brew –version或者brew -v 显示brew版本信息
brew install <formula> 安装指定软件
brew unistall <formula> 卸载指定软件
brew list 显示所有的已安装的软件
brew search text 搜索本地远程仓库的软件，已安装会显示绿色的勾
brew search /text/ 使用正则表达式搜软件
brew update 自动升级homebrew（从github下载最新版本）
brew outdated 检测已经过时的软件
brew upgrade 升级所有已过时的软件，即列出的以过时软件
brew upgrade <formula>升级指定的软件
brew pin <formula> 禁止指定软件升级
brew unpin <formula> 解锁禁止升级
brew upgrade –all 升级所有的软件包，包括未清理干净的旧版本的包
brew services –help 查看brew如何管理服务
```

### 系统 services 管理

```bash
brew services list： 查看所有服务
brew services run [服务名]: 单次运行某个服务
brew services start [服务名]: 运行某个服务，并设置开机自动运行。
brew services stop [服务名]：停止某个服务
brew services restart：重启某个服务。
```

### brew 安装的软件迁移到新电脑

```sh
# 旧电脑: 安装 bundle 并 dump, 会生成文件 Brewfile
brew bundle dump
cat Brewfile

# 复制 Brewfile 到新电脑; 安装
brew bundle
```

## 命令行

### 命令行快捷键

可参考 [iTerm2 快捷键大全](https://cnbin.github.io/blog/2015/06/20/iterm2-kuai-jie-jian-da-quan/)，但其实常用的也不是很多，主要是 Ctrl 的组合键：

- `Ctrl+A`, `Ctrl+E` 移动光标在行首/行尾；
- `Ctrl+W`, `Ctrl+K` 删除光标前/后的内容；
- `Ctrl+U` 清除一行（不过 `Ctrl+C` 好像可以替代？）；
- `Ctrl+L` 清空屏幕

## 软件列表 (简)

列表

### 效率/工具类

- 滴答清单
- Speedtest
- [Logitech Options](https://www.logitech.com.cn/zh-cn/product/options)
- PopClip: 选中弹出快捷工具
- Moom: 窗口管理
- CheatSheet: 查看快捷键
- ShortcutDetective: 快捷键冲突

Menu

- iStat Menus: Menu 系统监控
- Bartender 4: 解决Menu不够放的问题
- ClashX

稍后读/存档

- DEVONthink: ⭐️

系统工具

- App Cleaner & Uninstaller: 系统清理/管理; ⭐️
- [Tencent Lemon](https://lemon.qq.com/): 腾讯少有的良心软件
- DaisyDisk: 磁盘空间管理 ⭐️

折腾

- balenaEtcher

通讯

- [Telegram](https://macos.telegram.org/): 宇宙第一通讯软件 ⭐️

### code/开发

- VS Code: 主力软件 ⭐️⭐️
- iTerm2 可以导入配置文件 ⭐️
- Sublime Text
- PyCharm 学生账号的话可以试试
- Transmit: SFTP工具, 同步配置
- Postman

用过的一些后端 (brew 安装)

- nginx
- mongodb-community
- elasticsearch-full
- kibana-full
- redis

### 文本: 笔记/文档管理软件

- [Typora](https://typora.io/) 长期公测后终于收费了
- Notion: 速度太慢, 弃了
- Lark 飞书: 替代 Notion的数据库功能
- MWeb: 个人开发的超赞 Markdown 笔记软件
- Bear: UI挺好看

写作工具

- DeepL

文档管理

- Zotero

阅读

- PDF Expert ⭐️
- Clearview: 有点丑

### 图片: 截图/OCR

- Xnip
- iText
- Mathpix: 公式+文字识别 👍
- Artpaper: 一款免费的壁纸工具

### 网络/浏览器/存储

- [Chrome](https://www.google.com/intl/zh-CN/chrome/)
    - [Chrome 快捷键](https://support.google.com/chrome/answer/157179?hl=zh-Hans)
- Aria2
- ClashX
- 阿里云盘 aDriver: 文件下载
- EasyConnect: 学校 VPN, [download](https://stuvpn.fudan.edu.cn/portal/#!/down_client)

存储

- Synology Drive Client: [Synology 相关软件下载](https://www.synology.com/zh-hk/support/download/DS918+#utilities)
- BaiduNetdisk 百度，无奈之举

## 工具类软件

### uTools

见 [[uTools.md]]

- 猿料社区: <https://yuanliao.info/>
- Doc <https://u.tools/docs/guide/about-uTools.html> 入门及其简要，但有插件开发指南
- 相关插件
    - 网页快开; 聚合翻译; 颜色助手; 剪切板

### Automator

- 官方教程 [Automator User Guide](https://support.apple.com/guide/automator/welcome/mac)
- Mac [利用 Automator 自动化你的工作（pod、git等终端操作）](https://juejin.cn/post/6844904154863763469)

#### 案例: PDF 压缩

参见 [如何用 Automator 在 Mac 上批量压缩 PDF](https://zhuanlan.zhihu.com/p/30979115) ，其中第二个 workflow 可实现原地压缩 PDF 文件。

主要的思路是：1. 先接受传输的文件 filePath；2. 运行 shell 脚本 `dirname "$1"` 获得当前的目录 floderName；3. 获取 filePath 的值传入进行压缩；4. 移动输出的文件到 folderName。

## 其他软件

### Word 使用

- 生成目录（确保文章的标题层级）[Word写论文如何生成目录？](https://www.zhihu.com/question/20540465)
- 公式编号（手动设置格式）[word公式编号与引用详细教程--制表符、题注、交叉引用](https://www.bilibili.com/video/av285889573/)
    - 注意打开标尺可能尺度有问题，我们需要的是显示字符的数量，在「设置-常规-显示度量单位」里选择「派卡」？
- 公式转换
    - 和Latex语法并不一致，对于支持的语法，可以点击「设计、转换、当前专业」或者直接点击公式右边的三角形按钮选「专业」
    - 或者用 Mathpix Snip 或者 Pages 转换？

## 图片管理方案 (构建中)

- 参见 [如何高效地整理照片及管理照片？](https://www.zhihu.com/question/20966524)

尝试的软件

- Billfish
- Lightroom
- Photos
- Inboard
- Picsee 图片分类和管理，原生似乎更好用
- Mylio 和原生的 Photos 很类似；比如按照日历形式展现的特性很好；但使用层面上从流畅性、系统集成度、编辑的直观 都要落后于原生

大爱原生的 photos

- Docs <https://support.apple.com/zh-cn/guide/photos/welcome/mac>
    - Title Caption 等 <https://support.apple.com/zh-cn/guide/photos/phta4e5a733f/mac>
- 插件
    - Mimeo Photos 不是很好用的相册制作插件

## Archive

> 有同类型替换的、不再使用的、停止维护的

### Alfred

最重要的，还是查看官方文档 [Getting Started with Alfred 4 for Mac](https://www.alfredapp.com/help/getting-started/)。

自己简单看了少数派上的 [从零开始学习 Alfred：基础功能及设置](https://sspai.com/post/32979)，就是很简单地罗列了 Feature 中不同选项的意思；

比如我目前用到的

- 应用、文件搜索
    - `/` `~` 可定位到根目录或用户文件夹；
- Bookmark 搜索，可惜好像不能搜索网页名字而是直接检索网页地址；
- 自定义网页搜索 Web Search；
- `Opt+Cmd+C` 剪切板历史
