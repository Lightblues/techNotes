# Hackintosh

> 黑苹果安装记录. 因为硬件基本是按照黑苹果需求配置的, 第一遍安 Clover 没追求细节便顺利上车; 之后由于分区管理问题放弃; 22年春节重新折腾了 OpenCore.

Apple Silicon 时代还去鼓捣黑苹果实在是费力不讨好的事情; 有所失也总归有所得; 尤其是 Marak 事件之后, 看到黑苹果开源社区, 教程编写者门的工作也十分感动.

逆势所为, 看个人选择吧, 以下简单做链接汇总.

### OpenCore 安装

- 主教程 | **国光的黑苹果安装教程** [https://apple.sqlsec.com/](https://apple.sqlsec.com/)
- 官方教程 [https://dortania.github.io/OpenCore-Install-Guide/](https://dortania.github.io/OpenCore-Install-Guide/)
- OC 编辑器
    - [ProperTree](https://github.com/corpnewt/ProperTree)
    - [OpenCore Configurator](https://mackie100projects.altervista.org/download-opencore-configurator/)
- 可以先找一个类似的配置好的 EFI 参考，例如 [hackintosh-opencore-z390-aorus-pro-wifi](https://github.com/timche/hackintosh-opencore-z390-aorus-pro-wifi); 我的放在了 [here](https://github.com/Lightblues/EFI-Aorus-Z390)

#### Debug

- 蓝牙
    - 原本以为不能用是网卡的问题, 尝试 [BrcmPatchRAM](https://github.com/acidanthera/BrcmPatchRAM) 无果; 结果还是 USB 的问题
- 有线网卡
    - IntelMausi
- 多引导
    - Fight Windows 引导: 还是直接看国光的 [教程6.6](https://apple.sqlsec.com/5-%E5%AE%9E%E6%88%98%E6%BC%94%E7%A4%BA/5-6.html) 吧, 就是用 [EasyUEFI](https://sqlsec.lanzouw.com/iDaQ1ubeg6h) 配置
    - 详见 [教程](https://dortania.github.io/OpenCore-Multiboot/empty/diffdisk.html)
- HDMI 睡眠后显示器无法唤醒: 启动参数添加 `igfxonln=1`; from [here](https://macoshome.com/hackintosh/hcourse/5449.html)
    - 休眠的问题比较复杂, [教程](https://dortania.github.io/OpenCore-Post-Install/universal/sleep.html)
    - 尝试过 [HibernationFixup](https://github.com/acidanthera/HibernationFixup) 没作用
    - 关于 macOS 的睡眠种类参见 [here](https://heipg.cn/tutorial/enable-sleep-mode-for-hackintosh.html#%E9%80%89%E6%8B%A9%E4%BC%91%E7%9C%A0%E6%A8%A1%E5%BC%8F)
- USB 映射
    - 遇到的: 要么是 USB3.0 失效, 要么 USB2.0 失效: 需要用到 [USBInjectAll](https://github.com/Sniki/OS-X-USB-Inject-All/releases) 和 [USBMap](https://github.com/corpnewt/USBMap).
    - 具体的 USB map 参见 [教程](https://dortania.github.io/OpenCore-Post-Install/usb/intel-mapping/intel.html)
    - 另外司波图也有一个自己定制的 [教程](https://www.bilibili.com/video/BV1Aa4y1j7CL)
- 关于 NTFS 挂载
    - 同一张硬盘上的分区会被自动只读形式挂载, 看着有点难受
    - 尝试配置了 fstab 但好像不太行; 参见 [here](https://gist.github.com/CharlesThierry/7305166b208d6f6cdd37962761d5ac23); 另外参见 [解决Linux无法读写U盘中的NTFS问题](https://juejin.cn/post/6897075697849171975)
    - 看到有用 ntfs-3g [实现](https://www.bilibili.com/read/cv13273551) 的, 有需求尝试吧
- 关于更新
    - 看到小红点没忍住, 尝试从 Monterey 10.1 更新到 10.2, 果然失败了; 然后发现 OC 好像回归到了很早的一个版本, 无论怎样修改 plist 都没用, 最后 **重置 NVRAM** 解决了
    - No zuo, no die
- 添加其他系统的引导
    - 参见 [OpenCore添加ubuntu引导，引导三系统（Macos+Windows+Linux）](https://blog.csdn.net/qlpdong/article/details/118572750) 其实就是在 OC 的配置项中添加了一列

### 回顾 Clover 安装

总结一下之前写的 Clover 安装过程, 以资比较.

- 安装主要参考了 Sleele 大佬的 [黑苹果入门教程](https://sleele.com/2019/07/14/gettingstartedtutorial/)
- 资源来自 [黑果小兵的部落格](https://blog.daliansky.net/)
- 选购指南 [TonyMacX86](https://www.tonymacx86.com/)

安装流程

- 下载, 制作安装 U盘
    - 这里用的是 App Store 下载的方式, `sudo /Applications/Install\ macOS\ Mojave.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume` 即可
    - 找到的对应机型的 EFI 文件复制到启动盘的 EFI 分区下, 参见 [Hackintosh 黑苹果长期维护机型 EFI 及安装教程整理](https://github.com/daliansky/Hackintosh)
- U盘 启动, 安装系统
- 配置 EFI
    - 第一次很顺利, 直接用了他人配置好的 EFI 就上车了, 因此没有太多研究
    - 用 `sudo diskutil mount disk0s1` 挂载替换 EFI 即可; 或者用 Clover Configurator 挂载

定制 USB

- 用了 sleele 的 [使用Hackintool定制黑苹果USB驱动](https://sleele.com/2019/06/07/%E4%BD%BF%E7%94%A8hackintool%E5%AE%9A%E5%88%B6%E9%BB%91%E8%8B%B9%E6%9E%9Cusb%E9%A9%B1%E5%8A%A8/)
- 关于 WiFi 等问题, 由于用了 PCIE 网卡, 需要禁用主板 WiFi
