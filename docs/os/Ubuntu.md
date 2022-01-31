# Ubuntu

## 包管理

一般的deb包（包括新立得或者apt-get下载的）都在 `/usr/share` 。自己下载的压缩包或者编译的包，有些可以选择安装目录，一般放在 `/usr/local/` ，也有在 `/opt` 的。

Ubuntu软件包格式为deb，安装方法如下：

```bash
dpkg -i package.deb 安装包
dpkg -r package 删除包
dpkg -P package 删除包（包括配置文件）
dpkg -L package 列出与该包关联的文件
dpkg -l package 显示该包的版本
dpkg –unpack package.deb 解开 deb 包的内容
dpkg -S keyword 搜索所属的包内容
dpkg -l 列出当前已安装的包
dpkg -c package.deb 列出 deb 包的内容
dpkg –configure package 配置包
```

### apt-get 管理包

```bash
apt-cache search # ------(package 搜索包) 
apt-cache show # ------(package 获取包的相关信息，如说明、大小、版本等) 
sudo apt-get install # ------(package 安装包) 
sudo apt-get install # -----(package - - reinstall 重新安装包) 
sudo apt-get -f install # -----(强制安装?#"-f = --fix-missing"当是修复安装吧...) 
sudo apt-get remove # -----(package 删除包, 保留配置文件) 
sudo apt-get remove --purge # ------(package 删除包，包括删除配置文件等) 
sudo apt-get autoremove --purge # ----(package 删除包及其依赖的软件包+配置文件等（只对6.10有效，强烈推荐）) 
sudo apt-get update # ------更新源 
sudo apt-get upgrade # ------更新已安装的包 
sudo apt-get dist-upgrade # ---------升级系统 
sudo apt-get dselect-upgrade # ------使用 dselect 升级 
apt-cache depends # -------(package 了解使用依赖) 
apt-cache rdepends # ------(package 了解某个具体的依赖?#当是查看该包被哪些包依赖吧...) 
sudo apt-get build-dep # ------(package 安装相关的编译环境) 
apt-get source # ------(package 下载该包的源代码) 
sudo apt-get clean && sudo apt-get autoclean # --------清理下载文件的存档 && 只清理过时的包 
sudo apt-get check # -------检查是否有损坏的依赖 
```

## 软件列表

```bash
sudo apt-get install gparted # GParted 分区管理
sudo apt-get install filezilla # FileZilla FTP工具
sudo apt-get install vlc -y # VLC 播放器
sudo apt-get install gedit
sudo apt-get install transmission # BitTorrent 客户端软件
sudo apt-get install thunderbird # 邮箱
sudo apt-get install shutter # 截图

# Chrome
wget -q -O - https://raw.githubusercontent.com/longhr/ubuntu1604hub/master/linux_signing_key.pub | sudo apt-key add
sudo sh -c 'echo "deb [ arch=amd64 ] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt-get update
sudo apt-get install google-chrome-stable
```

## Debug

### 首次 Root 登陆

如果是正常 GUI 安装的 Ubuntu，默认是普通用户登陆，此时没有 root 账户的密码；因此

```bash
sudo passwd root
```

### 重置/忘记 root 密码

编辑启动项（在 GRUB 界面按 `e` 编辑）；又看到两种

- Ubuntu 基本选项，将 `ro quiet splash $vt_handoff` 部分修改为 `rw init=/bin/bash`，目的是给root文件系统设置读和写的命令
- 高级的 recovery mode，修改 `ro recovery nomodeset` 为 `quiet splash rw init=/bin/bash`

然后通过 Ctrl + x 或 F10 启动；利用 passwd 修改密码后，`exec /sbin/init` 重启进入Ubuntu系统

### 修改HOST, 重启网络

修改完之后要重启网络。

```bash
sudo /etc/init.d/networking restart
```

## 快捷键

1. [最全整理 | 121个Ubuntu终端常用快捷键](https://zhuanlan.zhihu.com/p/32878307)

### Terminal

`CTRL+ALT+T`：打开终端

`CRTL+SHIFT+V`：粘贴

### Desktop

1. `Alt+F2` : Run console
2. `Super` : Opens Activities search
3. `Super+L` or `Ctrl+Alt+L` : Locks the screen
4. `Super+D` or `Ctrl+Alt+D` : Show desktop 显示桌面、隐藏桌面
5. `Super+A` : Shows the application menu
6. `Super+Tab` or `Alt+Tab` : Switch between running applications
7. `Super+Arrow` : Snap windows
8. `Super+M` : Toggle notification tray
9. `Super+Space` : Change input keyboard (for multilingual setup)
10. `Ctrl+Alt+arrow` : Move between workspaces 切换工作区
11. `ALT+F4` : 关闭窗口
