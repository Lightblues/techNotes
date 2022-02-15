
## 软件列表

- Hackintosh
    - Hackintool
    - OpenCore Configurator: OC配置; EFI挂载
- 软件管理
    - [brew](https://brew.sh/):
        - [VS Code](https://formulae.brew.sh/cask/visual-studio-code): 官方下载安装包好慢来着
        - uTools: 启动管理
        - 其他列表见下
- 工具
    - 阿里云盘 aDriver: 文件下载
    - [Notion](https://www.notion.so/): 跨平台笔记同步
    - 效率
        - PopClip
        - Magnet 窗口管理
        - MacCleaner 系统清理/管理
- 常用
    - PDF Expert
    - MWeb
    - Transmit SFTP工具, 同步配置
    - MagNet 窗口管理
- Code
    - git: `ssh-keygen`
    - 其他的直接看下面代码吧
    - EasyConnect 学校 VPN

```bash
# brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# vim 复制已有的配置文件
cp code/00-config/configs/shell/.vimrc ~/

# 配置 zsh
brew install --cask iterm2
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
chsh -s $(which zsh) # 似乎  Monterey 默认就是 zsh?
# ! 因为备份了配置, 直接复制过来
cp code/00-config/configs/shell/.zshrc ~/
source ~/.zshrc
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
brew install autojump # j
source ~/.zshrc
# 基本软件
brew install tree
brew install trash # 用 trash 替换 rm
brew install carlocab/personal/unrar # x=extract 解压 rar 文件调用
brew install bat # 增强 cat

# VS Code; Sublime
brew install --cask visual-studio-code
brew install --cask sublime-text

# conda
brew install --cask miniconda
conda init zsh

# go
brew install go # VS Code 可以自动识别安装相关调试工具

# Applications
brew install --cask neteasemusic # 网易云音乐
brew install --cask iina # IINA
brew install --cask wechat qq # WeChat QQ
brew install --cask keka # 压缩软件

# Tools
brew install --cask utools # uTools
brew install --cask eudic # 欧路词典
brew install --cask karabiner-elements # 改键
```

记录一下目前安装列表

```bash
(base) ➜  code brew list
==> Formulae
autojump gdbm  mpdecimal python@3.10 sqlite  tree
ca-certificates go  openssl@1.1 readline trash  xz

==> Casks
eudic   miniconda  qq   visual-studio-code
iina   neteasemusic  sublime-text  wechat
iterm2   popclip
```
