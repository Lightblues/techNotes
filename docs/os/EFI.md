# EFI 相关

## GRUB

- Arch [GRUB](https://wiki.archlinux.org/title/GRUB); 例如用到了其中的 rescue

### grub rescue 进入系统

参见 [linux 开机如何进入grub 命令行模式，并通过grub命令进入系统](https://www.cnblogs.com/peach-blossoms/p/15228957.html)

```bash
# rescue
grub rescue> set prefix=(hdX,Y)/boot/grub # ls 找到系统分区
grub rescue> insmod (hdX,Y)/boot/grub/i386-pc/normal.mod # 可能是 /boot/grub/x86_64-efi/normal.mod
rescue:grub> normal
```
