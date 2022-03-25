# Arch Linux

- 入门
    - [Help:Reading (简体中文)](https://wiki.archlinux.org/title/Help:Reading_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)) Arch wiki 阅读指南
    - **包管理工具** [Category:Package management](https://wiki.archlinux.org/title/Category:Package_management_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
        - [Pacman](https://wiki.archlinux.org/title/Pacman_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
        - [AUR helpers](https://wiki.archlinux.org/title/AUR_helpers_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)) 比如其中的 `yay`
        - 软件包自动编译脚本 [makepkg](https://wiki.archlinux.org/title/Makepkg_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
        - 另外还尝试过 `snapd`
    - 系统维护 [System maintenance](https://wiki.archlinux.org/title/System_maintenance_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)) 备份、更新、清理、检查错误
- Important
    - Wiki 索引 [General recommendations](https://wiki.archlinux.org/title/General_recommendations_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
    - Arch 安装教程 [Install](https://wiki.archlinux.org/title/installation_guide)
    - [UEFI](https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)) 统一可扩展固件界面. 例如其中提到使用 `efibootmgr` 来操作 UEFI 固件启动管理器设置, 似乎很赞!
    - 引导过程 [Arch Boot Process](https://wiki.archlinux.org/title/Arch_boot_process_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
    - [Rsync](https://wiki.archlinux.org/title/Rsync) 带有权限全盘拷贝
    - 分区 [partition](https://wiki.archlinux.org/title/Partitioning_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
    - 文件系统 [file system](https://wiki.archlinux.org/title/File_systems_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
    - [fstab](https://wiki.archlinux.org/title/fstab)
    - [GRUB](https://wiki.archlinux.org/title/GRUB_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
- 实用
    - Arch 迁移到另外的硬盘 [migrate installation](https://wiki.archlinux.org/title/Migrate_installation_to_new_hardware_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
    - 编辑器 [Vim](https://wiki.archlinux.org/title/Vim_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
    - 软件列表 [List of Applications](https://wiki.archlinux.org/title/List_of_applications)
- 参考
    - 篝ノ雾枝的魔法学院｜<https://archlinuxstudio.github.io/ArchLinuxTutorial/#/> 安装和使用指南

## 包管理

包管理基本语法; 安装软件

```bash
# pacman
# 卸载
pacman -Qs gold # 查询相关软件
sudo pacman -Rs goldendict # 卸载包及用不到的依赖

# yay
# 注意 yay 不要用 sudo
yay -S google-chrome
yay -S eudic        # 欧陆词典
yay -S notion-app   # Notion
```

```bash
sudo pacman -S package_name     # 安装软件包
sudo pacman -Syyu               # 升级系统 yy标记强制刷新 u标记升级动作
sudo pacman -R package_name     # 删除软件包
sudo pacman -Rs package_name    # 删除软件包，及其所有没有被其他已安装软件包使用的依赖包
sudo pacman -Qdt                # 找出孤立包 Q为查询本地软件包数据库 d标记依赖包 t标记不需要的包 dt合并标记孤立包
sudo pacman -Rs $(pacman -Qtdq) # 删除孤立软件包
sudo pacman -Fy                 # 更新命令查询文件列表数据库
sudo pacman -F xxx              # 当不知道某个命令属于哪个包时，用来查询某个xxx命令属于哪个包
```

一个图形化包管理软件

```bash
yay -S octopi # 包管理器前端界面
```

### 软件列表

```bash
yay -S visual-studio-code-bin
```

## 安装

- 禁用reflector
- 确保为UEFI模式
- 网络
    - 无线 iwctl
- 更新系统始终
- 更换国内源
- 分区
- 格式化
- 挂载
- 安装系统
- 生成 fstab 文件
- Change root
- 设置主机名和时区
- 硬件时间设置
- 设置Locale
- Root 密码
- 安装微码
- 安装引导程序

```bash
# 禁用11
systemctl stop reflector.service

# 若有输出则为 UEFI
ls /sys/firmware/efi/efivars

# 网络
# 无线用 iwctl
iwctl                           #进入交互式命令行
device list                     #列出设备名，比如无线网卡看到叫 wlan0
station wlan0 scan              #扫描网络
station wlan0 get-networks      #列出网络 比如想连接CMCC-5AQ7这个无线
station wlan0 connect CMCC-5AQ7 #进行连接 输入密码即可
exit                            #成功后exit退出
# 测试网络
ping www.gnu.org

# 更新系统时钟
timedatectl set-ntp true    #将系统时间与网络时间进行同步
timedatectl status          #检查服务状态

# 国内源
vim /etc/pacman.d/mirrorlist    #不会vim的同学，此处注意视频中的vim操作步骤
# 把 ustc 的放到最前面

# 分区
# 将磁盘转为 GPT 类型
lsblk                       #显示分区情况
parted /dev/sdx             #执行parted，进行磁盘类型变更
(parted)mktable             #输入mktable
New disk label type? gpt    #输入gpt 将磁盘类型转换为gpt 如磁盘有数据会警告，输入yes即可
quit                        #最后quit退出parted命令行交互
# 用 cfdisk 进行分区
cfdisk /dev/sdx #来执行分区操作,分配各个分区大小，类型
fdisk -l #复查磁盘情况

# 格式化
#磁盘若有数据会问 'proceed any way?' y回车 即可
mkfs.ext4  /dev/sdax            #格式化根目录和home目录的两个分区
mkfs.vfat  /dev/sdax            #格式化efi分区

# 挂载
mount /dev/sdax  /mnt
mkdir /mnt/home
mount /dev/sdax /mnt/home
mkdir /mnt/efi
mount /dev/sdax /mnt/efi

# 安装系统
# 基础包
pacstrap /mnt base base-devel linux linux-firmware  #base-devel在AUR包的安装是必须的
# 功能性软件
pacstrap /mnt dhcpcd iwd vim sudo bash-completion   #一个有线所需 一个无线所需 一个编辑器  一个提权工具 一个补全工具 iwd也需要dhcpcd

# 生成 fstab
genfstab -U /mnt >> /mnt/etc/fstab
cat /mnt/etc/fstab #检查

# 将环境切换到新系统的 /mnt 下
arch-chroot /mnt

# 主机名
vim /etc/hostname        # 比如写 myarch
# hosts
vim /etc/hosts
#127.0.0.1   localhost
#::1         localhost
#127.0.1.1   myarch.localdomain    myarch
# 设置时区
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# 系统时间同步到硬件时间
hwclock --systohc

# 设置 Locale
vim /etc/locale.gen
# 去掉 en_US.UTF-8 和 zh_CN.UTF-8  前的注释
# 生成 locale
locale-gen
echo 'LANG=en_US.UTF-8'  > /etc/locale.conf

# root 密码
passwd root

# 微码（32位支持？）
pacman -S intel-ucode   # Intel
pacman -S amd-ucode     # AMD

# 安装引导程序
pacman -S grub efibootmgr   # grub是启动引导器，efibootmgr被 grub 脚本用来将启动项写入 NVRAM。
grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=GRUB # 取名为GRUB 并将grubx64.efi安装到之前的指定位置
# 这里仅生成 /efi/EFI/GRUB/grubx64.efi 这一份文件（efi分区中仅有）
# 编辑
vim /etc/default/grub
# 生成配置文件
grub-mkconfig -o /boot/grub/grub.cfg

# 完成安装
exit                # 退回安装环境#
umount -R  /mnt     # 卸载新分区
reboot              # 重启
# 重启后连接网络，要开启 hdcp 服务
systemctl start dhcpcd  # 立即启动dhcp
ping www.gnu.org      # 测试网络连接
# 若是无线仍然要 iwctl
systemctl start iwd # 立即启动iwd
iwctl               # 和之前的方式一样，连接无线网络
```

### 安装Grub引导程序

> 接下来编辑/etc/default/grub 文件，去掉 `GRUB_CMDLINE_LINUX_DEFAULT` 一行中最后的 quiet 参数，同时把 log level 的数值从 3 改成 5。这样是为了后续如果出现系统错误，方便排错。同时加入 nowatchdog 参数，这可以显著提高开关机速度。

```bash
GRUB_DEFAULT=0 
GRUB_TIMEOUT=5 
GRUB_DISTRIBUTOR="Arch" 
GRUB_CMDLINE_LINUX_DEFAULT="loglevel=5 quiet nowatchdog" 
GRUB_CMDLINE_LINUX=""
```

## 桌面环境

- 系统更新
- 非 root 用户
- 安装 KDE Plasma 桌面
- 配置 greeter [sddm](https://wiki.archlinux.org/title/SDDM_(简体中文))
- 设置交换文件 swap
- 开启 32 位支持库与 ArchLinuxCN 支持库
- 安装基础功能包
- 设置系统为中文
    - 打开 System Settings > Regional Settings > Language -> Add languages 中选择中文加入，再拖拽到第一位
    - 再将System Settings > Regional Settings > Formats 中的值设为`中文-简体中文(zh_CN)`
    - 重新登陆生效
- 输入法
    - 打开 系统设置 > 区域设置 > 输入法，先点击`运行Fcitx`即可，拼音为默认添加项。如你还需要更多输入法如五笔，则再点击`添加输入法`，找到简体中文下的五笔 ，点击添加即可加入五笔输入法
    - 接下来点击 拼音 右侧的配置按钮，点选`云拼音`和`在程序中显示预编辑文本` 最后应用
    - 回到输入法设置，点击`配置附加组件`，找到 经典用户界面 在主题里选择一个你喜欢的颜色 最后应用
    - 重新登陆
- 配置系统默认编辑器
- 启动蓝牙

```bash
pacman -Syyu    #升级系统中全部包

useradd -m -G wheel -s /bin/bash testuser  # wheel附加组可sudo进行提权 -m同时创建用户家目录
passwd testuser
EDITOR=vim visudo
# 去掉这一行的注释符
#%wheel ALL=(ALL) ALL

# plasma
pacman -S plasma-meta konsole dolphin  # 安装plasma-meta元软件包以及终端和文件管理器

# sddm
systemctl enable sddm

# swap
dd if=/dev/zero of=/swapfile bs=1M count=16384 status=progress # 创建16G的交换空间 大小根据需要自定
chmod 600 /swapfile # 设置正确的权限
mkswap /swapfile # 格式化swap文件
swapon /swapfile # 启用swap文件
# 在/etc/fstab 中追加
#/swapfile none swap defaults 0 0

# archlinuxCN
vim /etc/pacman.conf
# 去掉 [multilib] 一节 中的注释，开启32位库支持
#[archlinuxcn]
#Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch
pacman -Syyu

# 桌面系统中的网络设置
sudo systemctl disable iwd                                                  # 确保iwd开机处于关闭状态，其无线连接会与NetworkManager冲突
sudo systemctl stop iwd                                                     # 同上，立即关闭iwd
sudo systemctl enable --now NetworkManager       
# 基础功能包
sudo pacman -S ntfs-3g                                                      # 识别NTFS格式的硬盘
sudo pacman -S adobe-source-han-serif-cn-fonts wqy-zenhei                   # 安装几个开源中文字体 一般装上文泉驿就能解决大多wine应用中文方块的问题
sudo pacman -S noto-fonts-cjk noto-fonts-emoji noto-fonts-extra             # 安装谷歌开源字体及表情
sudo pacman -S firefox chromium                                             # 安装常用的火狐、谷歌浏览器
sudo pacman -S ark                                                          # 与dolphin同用右键解压 注意可同时安装可选解压支持项
sudo pacman -S packagekit-qt5 packagekit appstream-qt appstream             # 确保Discover(软件中心）可用 需重启
sudo pacman -S gwenview                                                     # 图片查看器
sudo pacman -S steam      
# archlinuxcn 源
sudo pacman -S archlinuxcn-keyring                                          # cn源中的签名(archlinuxcn-keyring在archLinuxCn)
sudo pacman -S yay  

# 输入法
sudo pacman -S fcitx5-im # 基础包组
sudo pacman -S fcitx5-chinese-addons # 官方中文输入引擎
sudo pacman -S fcitx5-anthy # 日文输入引擎
sudo pacman -S fcitx5-pinyin-moegirl # 萌娘百科词库 二刺猿必备(ArchLinuxCn)
sudo pacman -S fcitx5-material-color # 主题       
# 设置环境变量konsole 以及 dophin 都需要这些环境变量，倒是 chrome 和 firefox 都不需要就可以输入中文
sudo vim /etc/environment
# GTK_IM_MODULE=fcitx
# QT_IM_MODULE=fcitx
# XMODIFIERS=@im=fcitx
# SDL_IM_MODULE=fcitx

# 默认编辑器
vim ~/.bashrc 
#export EDITOR='vim'

# 蓝牙
sudo systemctl enable --now bluetooth
```
