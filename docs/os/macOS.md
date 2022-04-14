
关联 [[Hackintosh.md]]; [[macOS-softwares.md]];

## 功能: 同步

- iCloud
    - 设置 iCloud Drive 同步桌面和文档文件夹
- TamperMonkey 可以通过 Google Drive 同步

## 快捷键

一些常见的就不讲了，如 `Cmd+N`, `Cmd+T`, `Cmd+W`, `Cmd+Q`, `Cmd+,`。[这篇文章](https://zhuanlan.zhihu.com/p/77724113) 还介绍了

- ``Cmd+` `` 在同一软件的不同 Window 间切换，类似 `Cmd+Tab` ；
- `Cmd+Shift+[` 或 `Cmd+Shift+]`，在不同标签下移动；
- `Cmd+Control+Space` 自带的特殊符号和表情；
- `F11` 查看桌面；

### 快捷键迁移

- 快捷键迁移：[如何将所有键盘快捷键从一台Mac迁移到另一台?](https://qastack.cn/superuser/670584/how-can-i-migrate-all-keyboard-shortcuts-from-one-mac-to-another)
    - 用 `defaults find NSUserKeyEquivalents` 查看自定义应用快捷键

### 查看快捷键占用

参见 [How to Find Conflicting Keyboard Shortcuts on Mac](https://sayzlim.net/find-conflicting-shortucts-mac/)，里面提到的 [ShortcutDetective](http://www.irradiatedsoftware.com/labs/)
 软件很好用，使用前需要 Accessibility 权限。

一切的原因，是因为 Alfred 的 `Opt+Space` 被占用了，最后通过这个软件找到居然是 Eudic……

另外，发现这个网站似乎还不错 <https://www.irradiatedsoftware.com>

## 需求与配置

### 重启 Finder

- 按住 Option 后右键 Docker 上的 Finder 图标
- 组合键 `Command+Option+Escape` 可以强制关闭应用
- 当然也可以打开 `Activity Monitor` 关闭
- Terminal `killall Finder`

### Time Machine 备份速度加速

- 加快 Time Machine 的备份速度 [Time Machine 开启全速备份](https://sleele.com/2020/05/10/time-machine-%e5%bc%80%e5%90%af%e5%85%a8%e9%80%9f%e5%a4%87%e4%bb%bd/)
其实只需要一条指令即可：`sudo sysctl debug.lowpri_throttle_enabled=0`，若要重置则重新设置为 1 即可。
- 排查备份文件 [解决Time Machine每次备份都很大问题](https://sleele.com/2019/01/30/time-machine/)

### 光标移动慢

设置: `System Preference - Keyboard` 中将 `Key Repeat` 和 `Delay Until Repeat` 调到最快即可。

### 启动项管理

- 在 `System Preference - Users & Groups - Login Items` 中设置即可。
- 当然也第三方软件配置也可

## Debug

### 重制 SMC（系统管理控制器）

我重置了一次 SMC 即解决了问题：在关机状态下长按 `Shift+Control+Option+电源键` 会亮一下图标；等待十秒之后再开机即可。【根据是否有 T2 芯片似乎要分别按左右 Shift，详见官方教程】
摘录 **系统管理控制器 (SMC)** 的作用：电源，包括电源按钮和 USB 端口的电源；电池和充电；风扇和其他热能管理功能；指示灯或感应器，例如状态指示灯（睡眠状态、电池充电状态等）、突发移动感应器、环境光传感器和键盘背光；打开和合上笔记本电脑盖时的行为。
简而言之，SMC 对应的是 **与睡眠、唤醒、电源、为 Mac 笔记本电脑电池充电有关的问题或其他与电源相关的症状**。

### 重置 NVRAM 和 PRAM

顺便摘录 NVRAM 和 PRAM 的作用：
「NVRAM（非易失性随机访问存储器）是一小部分内存，Mac 使用这些内存来储存某些设置并对其进行快速访问。PRAM（参数 RAM）储存着类似的信息，且 NVRAM 和 PRAM 的重置步骤相同。
可储存在 NVRAM 中的设置包括音量、显示屏分辨率、启动磁盘选择、时区，以及最近的内核崩溃信息。储存在 NVRAM 中的设置取决于您的 Mac 以及与这台 Mac 搭配使用的设备。
如果您遇到与这些设置或其他设置有关的问题，那么重置 NVRAM 可能会有帮助。例如，如果 Mac 并非从“启动磁盘”偏好设置中选定的磁盘启动，或者在 Mac 启动前短暂地显示了一个问号图标，则可能需要重置 NVRAM。」
重置的方法是在关机状态下长按 `Option+Command+P+R` 约 20 秒。

另外摘录使用「系统诊断」的方法：Intel CPU 的电脑是在启动时长按 `D` 键进入。
