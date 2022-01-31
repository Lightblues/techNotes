# Arch Linux

- Important
  - Arch 安装教程 [Install](https://wiki.archlinux.org/title/installation_guide)
  - 包管理 [Pacman](https://wiki.archlinux.org/title/Pacman_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
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

## 软件列表

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
