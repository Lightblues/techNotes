# 写给Windows用户的macOS入门指南 | 作为边缘科技宅的碎碎念

## 引 | 何以macOS? 

第一个问题就是macOS系统与Windows或Linux系统的比较, 什么理由让我们使用一个相对封闭的系统? 

- UI. 不可否认Windows的很多新的设计语言足够优秀, 但在历史包袱之下总能在某些时候总能感觉到割裂, 而macOS反而因其独裁而又着极高的一体性. 
- 快捷键. 连Vim都用不太来者似乎没资格高谈快捷键, 很多Linux上的操作也确实很方便, 但不得不说cmd的位置和语法用起来很顺手. 
- 软件生态. 较高的用户基数和一定的付费意愿的产物. 当然官方软件的易用性也确实足够用. 

当然, 实际上都是一些很「软」的方面. 但体验正来源一些日常细节. 不求折腾的顺手 (本意), 接受一定规训的便捷, 大概算是macOS的使用哲学. 

这篇有些啥? 

- 系统的基本使用; 
- 个人向的使用习惯传教; 
- 基本(DL开发)软件介绍; 

## basics

- 基本的用户交互, 包括 鼠标/触控板方向, cmd按键 等, 应该在激活时有一个基本的介绍, 另外参见官方的 [《macOS 使用手册》](https://support.apple.com/zh-cn/guide/mac-help/welcome/mac) (点开目录找重点).
- 一些重要的系统软件
    - `Finder` 文件管理器, 作为最基本的软件, 可以进Preference看看配置项. 
    - `System Preference` 系统配置, 集成度很高, 初进系统可以翻翻, 比windows的系统设置要简单太多了. 
    - `Activity Monitor` 系统资源监控, 作为底配用户需要考虑一些软件的系统占用, 高配用户可能用不到. 
    - `Terminal` 不仅是程序员一般人也需要掌握的交互方式, 有很多人推荐的替代产品 `iTerm` 但实际上的功能没多大差别. 
- 其他可以看看的内置软件
    - Notes: 简单的笔记软件, 优势在iOS同步.
    - Maps: 桌面端做得最好的地图软件.
    - Contacts: 通讯录管理 (导入导出csv编辑很方便).
    - Automator: 自动化工具, 有一定的学习成本 (Apple Script). 
    - App Store (MAS): macOS上的商店, 相较于iOS的, 对于自己的存在感不是很大. 
    - Photos: 照片管理一级棒. 
    - Music: 交互设计上有些不太能接受, 但其实还挺好用. 

一些基本快捷键. 想要多看看的话推荐安装 `CheatSheet` 随时查看. 

```sh
cmd+C/V
cmd+W   withdraw?
cmd+Q   quit
cmd+T   new tab
cmd+N   new
```

## 程序猿向环境推介

!!! note
    first step: connect to the internet!

### 命令行使用指北

属于没有能力但喜欢折腾的人, 所以可能尝试过很多乱七八糟的新奇玩意, 留下来的却都是入手门槛低好用的~ (基本都可以brew安装)

```sh
tldr    解决man页面 TL;DR 的问题, 列出了命令的基本使用方式⭐️
brew    软件安装, 见下
htop    系统监控
zsh     优点是兼容bash, 还有一些好用的插件. 见下.
```

其他的一些命令行工具

```sh
tree    文件结构
wget    基本/强大的下载功能
axel    简介好用的多线程下载
bat     cat增强
trash   rm增强
ncdu    文件夹空间占用/管理

smartmontools
```


### brew: 软件管理

身为多设备用户, [brew](https://brew.sh/) 逐渐成为了最主要的软件安装方式. 只需要在命令行搜索, 一键安装, 有需求的话还可以配置整体迁移. 

基本使用

```sh
tldr brew   # 记得用 tdlr 查看一下就知道七七八八了.

# 搜索, 安装
brew search visual-studio-code      # 也可以 https://brew.sh/ 搜索
brew install visual-studio-code
# 有时可能需要注意 --cask

# 查看列表
brew list
```

- 软件 cask 源
    - 啥意思? “To install, drag this icon…” no more. 就是可能有一些非开源的软件, 提供了一种一键下载安装的方式.
    - 注意, 有些软件 Formulae和Casks 同名, 例如 `tailscale`, 官方的开源版本没有GUI, 因此若要安装发布的版本需要加上 `brew install --cask tailscale`.

例如下面是我目前一台机器的列表. 常用的GUI软件基本就是 Casks 的那些~

```sh
(base) ➜  ~ brew list
==> Formulae
autojump   gettext    libssh2    mpdecimal   qrencode   wget
axel    go    libunistring   ncdu    readline   xz
bat    google-authenticator-libpam libuv    ncurses    rust    zstd
brotli    htop    libzip    node@16    smartmontools
c-ares    icu4c    lz4    openssl@1.1   sqlite
ca-certificates   libidn2    mongodb-community@5.0  pandoc    tldr
cmake    libnghttp2   mongodb-database-tools  pkg-config   trash
gdbm    libpng    mongosh    python@3.10   tree

==> Casks
adrive    iina    neteasemusic   sensei    tencent-meeting   wechat
alt-tab    iterm2    obsidian   sublime-text   thunder
calibre    karabiner-elements  openinterminal   syncthing   ticktick
cinebench   mathpix-snipping-tool  postman    tailscale   utools
eudic    microsoft-edge   qq    telegram   visual-studio-code
geekbench   miniforge   rar    tencent-lemon   visual-studio-code-insiders
```

除了软件, brew 还可以进行系统服务管理 (类似 systemctl/services), 见 `brew services --help`.

### 开发相关软件推荐

!!! note
    基本原则: 倾向于开源的免费软件, 收费软件确实有需求的话考虑购入.

```sh
# 下面的软件一般都可以 `brew install --cask microsoft-edge` 的形式安装

visual-studio-code 最好有的编辑器, 甚至日常写md笔记也是. 唯一的缺点是Electron有点吃内存. ⭐️ 有时间整理一下当前的使用方案.
miniforge/miniconda Python包管理软件. DL开发必备. 在 Apple silicon 上似乎推荐 miniforge.
iterm2 前述终端软件
sublime-text 简洁高性能的代码编辑器, 不过日常用vscode
openinterminal 提供了在Finder中选择目录, 快速在 vscode/iterm 中打开的功能
postman API调试工具

# texshop 不过Latex空间占用确实很高.
```

### 其他一些收费软件

```sh
transmit SFTP工具, 同步配置很方便
navicat-premium 数据库连接工具
```


## 其他软件推介

简要列表: brew安装的

```sh
# 下面的软件一般都可以 `brew install --cask microsoft-edge` 的形式安装

# 网络
microsoft-edge 新宠浏览器, 看来微软不仅是「最佳苹果开发者」, 还是最佳 Chromium开发者.
tailscale 组虚拟内网, 从而实现不需要连VPN的情况下连接服务器等需求.
syncthing 多端同步需求
adrive 阿里云盘, 还挺好用.
thunder 下载. 

# 工具
tencent-lemon 良心的辅助软件. 提供了基本够用的功能 ⭐️
cheatsheet 长按cmd查看当前环境下的快捷键.
utools 良心的系统小工具.
alt-tab 提供了 `opt+tab` 在同一软件的不同 windows 切换的功能
karabiner-elements 改建, 但实际上不咋用.

# 文字
eudic 字典
mathpix-snipping-tool 好用的公式/文字识别工具 ⭐️
obsidian 挺好用的笔记软件, 能和vscode兼容.

# 其他
iina macOS上很强大的音视频播放软件
telegram 好用的通讯软件
```

其他

```sh
ishot 好用的截图软件, 免费, 但要 MAS 安装.
```


### 一些收费软件

!!! warning
    有些是一些小功能, 但确实带来了一定的便捷性. 但实际需求并不高.

```sh
# 文字
mweb-pro 很良心的mk笔记软件, 开发者人超好 (虽然已转向vscode)

# 实用小工具
magnet 窗口管理小工具.
popclip 滑词之后弹出一些小工具.
tinycal 漂亮的状态栏日历

# 系统工具
app-cleaner 好用的软件管理/清理工具
keyboard-maestro 好用的键盘/快捷键工具.
daisydisk 好用的磁盘可视化关联工具 (空间不够的时间挺有用)
```


