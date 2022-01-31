### 科学上网｜Clash

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
