## Linux General

## 系统服务

一般都用 [[systemd.md]] 了.


## 系统硬件信息检测

磁盘检测可使用 [smartmontools](https://archlinux.org/packages/extra/x86_64/smartmontools/)

```bash
sudo smartctl -A /dev/sda #硬盘 sudo smartctl -d sat -A /dev/sdc #usb设备
```

磁盘空间分析可直接使用 dh 命令，也可使用 [Filelight](https://archlinux.org/packages/extra/x86_64/filelight/)图形化界面直观查看磁盘占用情况

```bash
df -h
```

cpu 与显卡的信息查看可使用如下两款软件

```bash
yay -S cpu-x 
yay -S gpu-viewer
```

使用 [dmidecode](https://archlinux.org/packages/extra/x86_64/dmidecode/) 可以完整查看系统绝大部分硬件信息，包括较难得到的内存频率，主板 BIOS 等等。

```bash
sudo dmidecode
```

## 其他

### 科学上网 | Clash

- Clash <https://github.com/Dreamacro/clash>
- 推荐教程 | [Linux下安装&配置Clash以实现代理上网](https://zhuanlan.zhihu.com/p/369344633)

#### 安装

```bash
su
wget https://github.com/Dreamacro/clash/releases/download/v1.6.5/clash-linux-amd64-v1.6.5.gz 
x clash-linux-amd64-v1.5.0.gz
mkdir /opt/clash
mv clash-linux-amd64 /opt/clash/clash
cd /opt/clash
wget -O config.yaml [订阅链接] 
wget -O Country.mmdb https://www.sub-speeder.com/client-download/Country.mmdb
chmod +x clash
# 启动，-d 设置配置路径 -f 配置文件
./clash -d .
./clash -f config.yaml
```

- 启用系统代理
    - 填写 HTTP 和 HTTPS 代理为 127.0.0.1:7890，填写 Socks 主机为 127.0.0.1:7891
- 图形化配置地址 <http://clash.razord.top/>

#### 配置开机自启

```bash
vim /etc/systemd/system/clash.service
# 粘贴下面的内容，注意文件路径

# 重载 systemctl deamon
systemctl daemon-reload
systemctl start clash.service
systemctl enable clash.service
```

```ini
[Unit]
Description=clash daemon

[Service]
Type=simple
User=root
ExecStart=/opt/clash/clash -f /opt/clash/config.yaml
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

#### 配置定时更新

Clash For Linux 到目前为止没有自动订阅方式，我们做一个计划任务实现更新`config.yaml` ；用Cron执行计划任务

```bash
crontab -e
# 输入下面的内容后，重启 crond 服务
systemctl restart crond.service
```

```text
29 6    * * *   root    pgrep clash | xargs kill -s 9 
30 6    * * *   root    mv /opt/clash/config.yaml /opt/clash/configbackup.yaml 
31 6    * * *   root    wget -P /opt/clash/ -O config.yaml [你的订阅链接]
32 6    * * *   root    nohup /opt/clash/clash -d /opt/clash/
```

## Debug

### 关闭图形界面

可以查看 `/etc/inittab`，大概就是

```bash
# 查看默认的target，执行：
systemctl get-default

# 开机以命令模式启动，执行：
systemctl set-default multi-user.target
# 开机以图形界面启动，执行：
systemctl set-default graphical.target
```

### 系统显示中文异常

from [简单解决Ubuntu修改locale的问题](https://www.cnblogs.com/williamjie/p/9303115.html)

> 本文针对的问题是“Ubuntu 安装中文语言包”“Ubuntu Server中文问题”，“Ubuntu更改语言环境”，“Ubuntu locale的设定”，“cannot change locale (zh_CN.UTF-8)”，“Linux中文乱码”，“Linux字符集的修改”，“Linux乱码的解决办法”等问题，提供一站式解决。如果系统显示中文异常，例如出现显示中文乱码等，可以参考本文章。关于CentOS系统的修改办法，请参考文章末尾的描述。

正确的变量配置应该是

```bash
LANG=zh_CN.UTF-8   
LANGUAGE=zh_CN:zh:en_US:en   
LC_ALL=LC_ALL=zh_CN.UTF-8
```

相关命令

```bash
sudo dpkg-reconfigure locales # 重新配置 locales
man locale
locale
localectl list-locales # 注意在 docker 中会报错没有 bus
```

!!! warning
    自己遇到的问题是中文无法显示, 命令 `locale` 报错
    locale: Cannot set LC_CTYPE to default locale: No such file or directory
    locale: Cannot set LC_MESSAGES to default locale: No such file or directory
    locale: Cannot set LC_ALL to default locale: No such file or directory

#### 重新按照中文语言包

```bash
sudo apt-get -y install language-pack-zh-hans
sudo apt-get -y install language-pack-zh-hant # 繁体字

locale-gen zh_CN.UTF-8
# or
sudo dpkg-reconfigure locales # 重新配置 locales
```

### 找不到man页面

比如 `man man` 也会返回 `No manual entry for man`

最后看了一下, 发现主要的文档路径为 `/usr/share/man/`, 然后 **从其他服务器上复制了一份** 过来就可以了.

```bash
# manpath - 确定手册页的搜索路径
# 查看搜索路径
manpath -g
# 配置文件在 /etc/manpath.config

# mandb - 创建或更新手册页索引缓存
mandb -c # create, 默认情况下，mandb 会尝试更新任何以前创建的数据库。

# 提出的一些意见
sudo apt-get install manpages manpages-dev
sudo apt-get install --reinstall coreutils
sudo apt-get install manpages-zh # 中文?

# -d 指令 debug
man -d ls
```

man 参见 [Linux 命令 man 全知全会](https://segmentfault.com/a/1190000041180612)
