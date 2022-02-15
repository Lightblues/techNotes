# EFI 相关

- Windows 启动逻辑 [UEFI 下 Windows 启动引导的顺序（附带 linux 双系统）](http://www.cxyzjd.com/article/akimotomei/105102041)

## 相关软件

- Windows 下可以用 `EasyUEFI` 或者 [BOOTICE](https://bootice.en.softonic.com/)
- 磁盘工具 `DiskGenius`

## GRUB

- Arch [GRUB](https://wiki.archlinux.org/title/GRUB); 例如用到了其中的 rescue

```bash
# 配置文件
ls /etc/grub.d/        # /etc/default/grub

## Ubuntu
sudo update-grub
# 生成位置
ls /boot/efi/EFI/ubuntu

## CentOS
grub2-mkconfig -o "$(readlink -e /etc/grub2.cfg)"
# 生成结果
# /etc/grub2.cfg -> ../boot/grub2/grub.cfg        # 取决于是 BIOS 还是 UEFI
```

### grub rescue 进入系统

参见 [linux 开机如何进入 grub 命令行模式，并通过 grub 命令进入系统](https://www.cnblogs.com/peach-blossoms/p/15228957.html)

```bash
# rescue
grub rescue> set prefix=(hdX,Y)/boot/grub # ls 找到系统分区
grub rescue> insmod (hdX,Y)/boot/grub/i386-pc/normal.mod # 可能是 /boot/grub/x86_64-efi/normal.mod
rescue:grub> normal
```
