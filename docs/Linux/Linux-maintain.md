# Linux 系统维护

TODO: 建立一个索引

## 相关命令

```bash
ls /dev/sd*

# fdisk
sudo fdisk -l
sudo fdisk /dev/sdb    # 输入 m，查看命令帮助

lsblk -f

# mkfs
sudo mkfs.ext4 /dev/sdb5 # 将/dev/sdb5格式化成ext4文件系统
```

## 查看系统信息

```bash
# 系统信息
uname -a
# 发行版本
cat /etc/os-release
```

### 显卡

```bash
lshw -numeric -C display
hwinfo --gfxcard --short # 需要安装
# or 还可以显示推荐的驱动版本
ubuntu-drivers devices
```

### 检测 lm_sensor TODO

- repo <https://github.com/lm-sensors/lm-sensors>
- 参见 <https://wiki.archlinux.org/title/Lm_sensors>

### 驱动

```bash
# 驱动操作
insmod / modprobe  加载驱动  
rmmod              卸载驱动  
lsmod              查看系统中所有已经被加载了的所有的模块以及模块间的依赖关系  
modinfo            获得模块的信息

# 查看已经加载的驱动模块的信息
lsmod              能够显示驱动的大小以及被谁使用  
cat /proc/modules  能够显示驱动模块大小、在内核空间中的地址
cat /proc/devices  只显示驱动的主设备号，且是分类显示 
ls /sys/modules   下面存在对应的驱动的目录，目录下包含驱动的分段信息

cat /proc/driver/nvidia/version # 查看内核驱动版本
```

from [here](https://blog.csdn.net/Jerry_1126/article/details/55003027)

#### 显卡驱动

```bash
# 查看
cat /proc/driver/nvidia/version
# sudo rmmod nvidia_drm nvidia_modeset nvidia 实现卸载了内核驱动？
modinfo nvidia
```

### 时间

```bash
date -R     # 查看时区
```

#### 设置时区

```bash
apt-get install tzdata tzselect
```

注意如果没有 `tzdata` 会报缺少 `/usr/share/zoneinfo/iso3166.tab` 的错。

实际上，系统时区配置（似乎）仅仅依赖于 `/etc/localtime` 文件，在没有安装 tzdata 的情况下，从其他的机器上复制时区文件为 `/etc/localtime` 即可进行设置。

```bash
cp /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
```

### 日志

```bash
dmesg   # 查看启动信息
```

### Show LISTEN ports 查看监听端口

- Linux
    - [How to check if port is in use on Linux or Unix](https://www.cyberciti.biz/faq/unix-linux-check-if-port-is-in-use-command/)

```bash
lsof -nP -i    #参见 macOS
netstat -tulpn | grep LISTEN

# 20210731 更新：似乎下面的记住就行
lsof -i:8080
```

- macOS
    - [Who is listening on a given TCP port on Mac OS X?](https://stackoverflow.com/questions/4421633/who-is-listening-on-a-given-tcp-port-on-mac-os-x)
    - 用 `lsof`
        - lsof - list open files
        - `-i i   select by IPv[46] address: [46][proto][@host|addr][:svc_list|port_list]`，注意 `-i` 指定TCP协议后有端口，可以放最后一个参数 `-nPi`
        - `-P no port names`
        - `-n no host names` 如果不加会很慢

```bash
lsof -nP -i | grep LISTEN        # 指定 n 速度比较快
```

## 制作启动盘

```bash
su
# 两个分区分别格式化为 NTFS 和 FAT32
fdisk -l  # 检查U盘，例如是 /dev/sdd
fdisk /dev/sdd # 分区，两个，留30M给第二个分区
yum install ntfsprogs # 安装处理NTFS的软件
mkfs.ntfs /dev/sdd1  # 速度比较慢
mkfs.vfat -F 32 /dev/sdc

wget https://software-download.microsoft.com/sg/Win10_21H1_Chinese(Simplified)_x64.iso?t=1e1d7d9d-a5d6-4c51-aa8d-38b35c627f1d&e=1632986672&h=53a28504164261a06e63f0c446241fc1
wget https://github.com/pbatard/rufus/blob/master/res/uefi/uefi-ntfs.img

sudo dd if=Win10_21H1_Chinese(Simplified)_x64.iso of=/dev/sdd1 bs=4M status=progress
sudo dd if=uefi-ntfs.img of=/dev/sdd2  # 也可以挂在两个，然后复制过去，注意需要把 img 下的隐藏文件也复制过去保留文件结构（而非仅仅是 EFI 文件夹）
```

from [在Linux下制作Linux&windows启动盘](https://www.cnblogs.com/rongyupan/p/13126840.html)

### 挂载LVM

在Ubuntu下挂载 CentOS 中的LVM

```bash
# 安装lvm2软件
sudo apt-get install  lvm2
#  扫描 LVM 找到 VG
sudo vgscan
# 激活
sudo vgchange -ay VolGroup01
sudo lvs # 列出
# 挂载
sudo mount /dev/VolGroup01/LogVol00   /mnt
```

## 系统迁移

尝试过一次

### Arch Linux 将系统转移到新的分区

这里将西数盘上(nvme0) 安装的 Arch 系统转移到三星 (nvme1) 的一个分区下, EFI 统一管理.

- 主教程
    - Arch 迁移到另外的硬盘 [migrate installation](https://wiki.archlinux.org/title/Migrate_installation_to_new_hardware_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
    - Arch 安装教程 [Install](https://wiki.archlinux.org/title/installation_guide)
    - [UEFI](https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)) 统一可扩展固件界面. 例如其中提到使用 `efibootmgr` 来操作 UEFI 固件启动管理器设置, 似乎很赞!
    - 另外参见 [Arch Linux 系统迁移](https://juejin.cn/post/6990623175906164772)
- 具体包括
    - [Rsync](https://wiki.archlinux.org/title/Rsync) 带有权限全盘拷贝
    - 分区, [partition](https://wiki.archlinux.org/title/Partitioning_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
    - 文件系统 [file system](https://wiki.archlinux.org/title/File_systems_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
    - [fstab](https://wiki.archlinux.org/title/fstab)
    - [GRUB](https://wiki.archlinux.org/title/GRUB_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
- 其他的
    - 引导过程 [Arch Boot Process](https://wiki.archlinux.org/title/Arch_boot_process_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
    - 包管理 [Pacman](https://wiki.archlinux.org/title/Pacman_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
    - 编辑器 [Vim](https://wiki.archlinux.org/title/Vim_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
    - 软件列表 [List of Applications](https://wiki.archlinux.org/title/List_of_applications)

简单记录相关命令

```bash
# 1. 将系统复制到新驱动器
# 分区，构建文件系统
sudo fdisk /dev/nvme1n1
lsblk -f # --fs 输出文件系统信息
sudo mkfs.ext4 /dev/nvme1n1p5
# 用 rsync 将全盘复制到新分区
sudo pacman -Syy rsync
rsync -aAXHv --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"} / /mnt
lsblk -f # 检查一下

# 2. 更新fstab
sudo mount /dev/nvme1n1p5 /mnt
sudo arch-chroot /mnt
# 这里进了新系统的环境，生成新的 fstab, 因此需要根据新系统下的挂载情况挂载相应的磁盘
mount /dev/nvme1n1p2 /efi # 这块磁盘上的 EFI 分区
sudo pacman -S --needed arch-install-scripts # 包括 arch-chroot, genfstab 等
genfstab -U / >> /etc/fstab # 如果是直接 mount 的话应该是 genfstab -U /mnt >> /mnt/etc/fstab

# 3. 重新安装引导加载程序 grub
# 安装，这里的 esp 即EFI系统分区，例如上面 mount /dev/nvme1n1p2 /efi 就是用 /efi
grub-install --target=x86_64-efi --efi-directory=[esp] --bootloader-id=GRUB
# 下面配置 grub，采用 grub-mkconfig 自动生成 (也可以手动写)
# 多系统引导，采用 os-prober 
sudo pacman -S os-prober 
# 挂载其他系统所在分区; 经测试 Windows 也可以识别
sudo mount /dev/nvme1n1p6 /root/sysA
grub-mkconfig -o /boot/grub/grub.cfg

# 完成!
sudo reboot
```

## 工具

### 格式转换工具

比较讨厌的是 doc 格式不好处理；win 平台可以利用 Python 打开 Word 另存为来解决，Linux 平台就不太好搞。

- `Pandoc` 不支持doc，对于docx可识别表格等格式

```bash
pandoc -i some.docx -t plain > some.txt
```

- antiword 可以 doc2docx ，但是输出的好像都是固定每行字数的格式？没法保留整段内容
- docx2txt 支持docx转txt 格式没有pandoc好；也不支持doc
- textract 支持的格式似乎挺多，但处理doc后台调用的是antiword

## Debug

### 自动挂载

编辑 `/etc/fstab` 文件实现自动挂载

```bash
sudo gedit /etc/fstab

# 在已有内容的后面新起一行，写入下面了内容；
# 第一个参数为你要挂载的分区(/dev/sdb5)；
# 第二个参数为挂载的位置（/sdb5文件夹必须存在）；
# 第三个参数是分区文件类型(ext4)，格式化的时候的那个类型，后面的参数默认即可；
/dev/sdb5   /home/qing/sdb5  ext4   defaults    0  0
```

### 制作（Linux）启动盘

找到U盘设备号后（可用 `sudo fdisk -l` 或 `sudo lsblk` 等）

```bash
sudo dd if=~/ubuntu-16.04-desktop-amd64.iso of=/dev/sdc status=progress oflag=sync
```

- status=progress 用来输出刻录过程中的信息。
- oflag=sync 用来控制写入数据时的行为特征。确保命令结束时数据及元数据真正写入磁盘，而不是刚写入缓存就返回。

### 系统迁移/U盘

- 硬盘迁移｜[记一次Ubuntu完美迁移系统盘的折腾](https://juejin.cn/post/6952523655838433311) ；另参 [迁移linux系统到新硬盘](https://zhuanlan.zhihu.com/p/33341983)
- 备份恢复｜[【必看】Linux 系统的备份恢复](https://zhuanlan.zhihu.com/p/335035901) 似乎可行！TODO
- 备份整个系统 | Linux 备份整个系统

```bash
tar cvpzf backup.tgz –exclude=/proc –exclude=/lost+found –exclude=/backup.tgz –exclude=/mnt –exclude=/sys /
# 恢复
tar xvpfz backup.tgz -C /
mkdir sys mnt proc lost+found
```

安装到U盘

- 可以[直接在安装过程中指定](https://blog.csdn.net/Caesar6666/article/details/106077133)；

### Failed to connect to ip port

可能是配置了防火墙，参见 [here](https://blog.csdn.net/caiyqn/article/details/107317796)

```bash
# 通过命令查看防火墙策略
sudo iptables -L | more
# 如果输出内容为Chain INPUT (policy DROP)，再执行修改策略
sudo iptables -P INPUT ACCEPT
# 直到确认输出为Chain INPUT (policy ACCEPT)，才可清除所有规则停止防火墙
sudo iptables -F 
# 关闭防火墙
systemctl stop firewalld.service
```
