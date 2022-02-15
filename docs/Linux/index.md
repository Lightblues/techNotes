## Linux General

## 系统服务 systemctl

以 dhcpcd 为例

```bash
systemctl start dhcpcd          # 启动服务
systemctl stop dhcpcd           # 停止服务
systemctl restart dhcpcd        # 重启服务
systemctl reload dhcpcd         # 重新加载服务以及它的配置文件
systemctl status dhcpcd         # 查看服务状态
systemctl enable dhcpcd         # 设置开机启动服务
systemctl enable --now dhcpcd   # 设置服务为开机启动并立即启动这个单元:
systemctl disable dhcpcd        # 取消开机自动启动
systemctl daemon-reload dhcpcd  # 重新载入 systemd 配置 扫描新增或变更的服务单元 不会重新加载变更的配置 加载变更的配置用 reload
```

拓展链接: [systemctl 官方文档](https://wiki.archlinux.org/index.php/Systemd#Basic_systemctl_usage) ；[systemd 配置文件样例解释](https://www.freedesktop.org/software/systemd/man/systemd.service.html#Examples)  

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
#查看默认的target，执行：
systemctl get-default

#开机以命令模式启动，执行：
systemctl set-default multi-user.target
#开机以图形界面启动，执行：
systemctl set-default graphical.target
```
