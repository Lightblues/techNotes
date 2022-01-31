# Linux 系统维护

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
