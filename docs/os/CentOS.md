# CentOS

```bash
# 换源参见 https://mirrors.tuna.tsinghua.edu.cn/help/centos/ 

######### zsh
# plugin
sudo yum install autojump-zsh   # 不同于 apt 下的 autojump，yum 中的 autojump 生成的文件夹 /usr/share/autojump 中缺失 autojump.zsh
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting

########## miniconda 
# see https://docs.conda.io/en/latest/miniconda.html 这里是 Linux 3.7
wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-Linux-x86_64.sh
bash Miniconda3-py37_4.10.3-Linux-x86_64.sh
```

## Software

### 软件安装

- EPEL 源
    - EPEL (Extra Packages for Enterprise Linux，企业版Linux的额外软件包) 是Fedora小组维护的一个软件仓库项目，为RHEL/CentOS提供他们默认不提供的软件包。这个源兼容RHEL及像CentOS和Scientific Linux这样的衍生版本。

开启

```bash
sudo yum -y install epel-release
sudo yum repolist

# 来试试看
sudo yum install htop
```

### NVIDIA driver

- 参见 [Centos 7 安装 Nvidia GPU 驱动及 CUDA](https://wilhelmguo.cn/blog/post/william/Centos-7-安装-Nvidia-GPU-驱动及-CUDA) ；另 [How to install Nvidia driver on CentOS 7 Linux](https://www.cyberciti.biz/faq/how-to-install-nvidia-driver-on-centos-7-linux/)
- 下载链接 <http://www.nvidia.com/Download/Find.aspx>
- Oficial <https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html#centos8>

```bash
# 0. 列出GPU
lspci | grep -i nvidia
# 验证系统是否是支持的
uname -m && cat /etc/redhat-release

# 1. 安装依赖
# install kernel-devel and gcc kernel 需要安装 gcc
sudo yum group install "Development Tools"
sudo yum install kernel-devel
# 或者｜验证系统是否安装了正确的内核头文件和开发包
sudo yum install kernel-devel-$(uname -r) kernel-headers-$(uname -r)

# 3. 禁用 nouveau
# nouveau是一个第三方开源的Nvidia驱动，一般Linux安装的时候默认会安装这个驱动。 这个驱动会与Nvidia官方的驱动冲突，在安装Nvidia驱动和和CUDA之前应先禁用nouveau
# 查看是否在使用
lsmod | grep nouveau
# 新建一个配置文件
sudo vim /etc/modprobe.d/blacklist-nouveau.conf
#配置
blacklist nouveau
options nouveau modeset=0
#备份当前的镜像
sudo mv /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r).img.bak
#建立新的镜像
sudo dracut /boot/initramfs-$(uname -r).img $(uname -r)
#重启
sudo reboot
#最后输入上面的命令验证
lsmod | grep nouveau

# 4. 下载、安装
# 方案1
rpm -i nvidia-diag-driver-local-repo-rhel7-396.82-1.0-1.x86_64.rpm
# 清除缓存
yum clean all
yum install cuda-drivers
# 方案2：我下载到的是 Linux 64 统一的一个 .run
udo bash NVIDIA-Linux-x86_64-470.63.01.run

# 重启shell后检验
nvidia-smi
```

### 开机启动

- 参见 [CentOS设置程序开机自启动的方法](https://www.huaweicloud.com/articles/12557280.html)

几个方案

- 写命令在文件 `/etc/rc.d/rc.local` 中，注意修改为 +x
- 把写好的启动脚本添加到目录 /etc/rc.d/init.d/，然后使用命令chkconfig设置开机启动

```bash
chkconfig 功能说明：检查，设置系统的各种服务。
语法：chkconfig [--add][--del][--list][系统服务] 或 chkconfig [--level <等级代号>][系统服务][on/off/reset]
--add 添加服务
--del 删除服务
--list 查看各服务启动状态
```

### 关闭图形界面

参见[这里](https://blog.csdn.net/op_zoro/article/details/44993881)

可以查看 `/etc/inittab`，大概就是

```bash
#查看默认的target，执行：
systemctl get-default

#开机以命令模式启动，执行：
systemctl set-default multi-user.target
#开机以图形界面启动，执行：
systemctl set-default graphical.target
```

## Debug

### 网络自动连接

配置 `/etc/sysconfig/network-scripts/` 下的网卡，修改为 `ONBOOT=yes`
