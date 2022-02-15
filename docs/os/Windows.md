# Windows

## 软件列表

- 系统相关
    - 鲁大师?
    - refus, `balenaEtcher` USB刷写
    - CPU-Z， GPU-Z
    - DiskGenius 磁盘管理
    - CrystalDisk
    - EasyUEFI 直接配置 BIOS, 类似 `efibootmgr`
- 效率
    - `SpaceSniffer` 空间管理
    - `Uninstall Tool`
- 工作
    - Office 系列?
    - IDM 下载
    - PotPlayer
    - Everything
- Code
    - Xftp, Xshell
    - VS Code

可以试一试的软件？

- Wox 启动器，类似 macOS 的 Spotlight
- 系统监控
    - 找了这款状态栏工具 XMeters <https://entropy6.com/xmeters/>
    - 还有很多人推荐这款开源的 <https://github.com/zhongyang219/TrafficMonitor>

## Debug

### 开启http代理或配置pac后导致win10 MICROSOFT STORE无法联网

关联 Github 上的 [这个问题](https://github.com/2dust/v2rayN/issues/1083) ；之前还傻兮兮下载了 Fidder，原来 Clash 自带了 `UWP Loopback`。

### 命令行工具选择

- Git Bash 中无法使用 conda，应该是没有配置环境变量（安装 miniconda 的时候提示不建议设置）；
- 目前在 Anaconda Powershell Prompt 中可使用 `ls, conda, git` 还算够用。

### 命令行代理

参考 Clash 给出的命令，注意 CMD 和 Power Shell 是不同的

```bash
$Env:http_proxy="http://127.0.0.1:7890";$Env:https_proxy="http://127.0.0.1:7890"
set http_proxy=http://127.0.0.1:7890 & set https_proxy=http://127.0.0.1:7890

# git
git config --global http.proxy 'http://127.0.0.1:1080'
git config --global https.proxy 'http://127.0.0.1:1080'
```

### 设置开机启动

- 简言之，就是打开 `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`，把想要的软件创建一个快捷方式即可。

### 截图

- Win 自带的 `Win+Shift+S`；
- Shipaste：下载 <https://zh.snipaste.com/download.html>
