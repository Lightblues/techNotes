# VS Code 使用指南

> v1 221012 @Lightblues

说明

1. 本文档是什么? 个人vscode工作流. 
2. 如何使用? 搭配参考链接; 实践第一. 
3. 插件使用
   1. 插件配置: 在进行插件配置时, 注意参看附的 [settings.json], 更加方便.
   2. 插件选择: 对于不是通用的插件, 可以选择「工作区打开」打开而非全局开启, 简洁并提升性能.
4. 性能说明: 
   1. 内存: 例如对于8G的Mac来说, 需要考虑的是内存占用问题. Electron 框架下没啥办法, 个人经验是少开点窗口 (个人经常开5+个项目就可能不太行了)
   2. 插件: 精简为妙. 

todo

- Python 工作流介绍
- debug (launch.json) 说明: 参考 [here](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations)
- markdown 笔记工作流. @221012

## vscode 基本

理解vscode的各个窗口, 基本要素

- Command Palette: 命令面板, 搜索匹配软件和插件的一些功能. ⭐️
- 插件生态: vscode的好用很大程度上来源于其极其强大的插件生态. 见下
- 下侧面板: Terminal, 调试控制栏, 不同组件的输出记录.
- 快捷键: 提升编辑体验, 但需要一些肌肉记忆.
- 个性化: 主题配置.
- 同步: 作为多设备用户, 左下角 GitHub 账号登陆同步功能很好用.

### Command Palette 命令面板

默认按 `Cmd/Ctrl + Shift + P` 唤出 (`F1` 好像也可以)

下面是我用的一些常用命令. todo

```bash
# 常用的 Commands.
Help: Interactive editor playground     # 学习vscode编辑方式
Preferences: Open User Settings (JSON)  # 打开用户配置文件
Preferences: Open Keyboard Shortcuts    # vscode 快捷键设置.
Developer: Reload Window                # 重新加载窗口, 有一些插件停用或者窗口有bug的时候可以试试.
Developer: Open Process Explorer        # 资源管理器, 查看 vscode 占用

# 一系列的 fold/unfold 指令, 看比较长的代码的时候很有用
Fold Level 2

# 针对不同的编程语言配置 snippets, 自动补全
Snippets

# 文件编码
Change File Encoding        # 以不同的编码 打开/保存

# 查看当前变量的定义/饮用. 用鼠标即可操作.
Peek Definition
Peek References

# ================ 一些插件的 commands
# sftp: 配置本地代码同步到远程
sftp: config
# markdown all in one: mk编辑相关快捷键
markdown all in one: toggle list    # 给选中行快速设置为list
```


### 快捷键

说明: 常用的快捷键其实并不多, 下面根据指南做了摘录, 有机会缩减一下... 实际上直接 Command栏 `Help: Interactive editor playground` 过一遍即可...

- doc [Key Bindings for Visual Studio Code](https://code.visualstudio.com/docs/getstarted/keybindings) 下面的内容摘录from此.
- 官方的快捷键清单 <https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf>，
- 另见命令行 `Help: Interactive editor playground`；

基本

- `cmd+\` 拆分编辑器
- `cmd+O` 打开文件
- `ctrl+R` 打开最近项目
- `cmd+J` 切换视图，隐藏 terminal 栏
- `cmd+B` 视图：侧边栏；但是在 Markdown 环境下 `markdown.extension.editing.toggleBold` 冲突·
- `cmd+K cmd+S` 键盘快捷方式

我自定义的一些快捷键

- `ctrl+Space` 代码补全和 macOS 的输入法切换撞了；暂无
- `shift+opt+~` 新建Terminal, 好反人类，换成了 `cmd+T`

#### 导航

- `opt` 配合左右是词级别；`cmd` 句子级别
- `cmd` 上下 移动到文档头尾
- `opt` 配合上下，移动整行
- `shift` 修饰，进行选择
- `cmd+]` 控制整行的缩进

##### Multi-cursor editing

- `opt+cmd+` 上下 进行进行多 cursor；`opt` 配合鼠标添加一个 cursor

##### Line actions

- `shift+opt+` 上下 复制整行
- `shift+cmd+K` 删除整行
- `opt` 配合上下，移动整行

##### Rename refactoring

- `F2` 或者右键选择

##### Formatting

- `shift+opt+F` 格式化整个文档
- `cmd+k cmd+F` 格式化当前行

可以配置 `editor.formatOnSave` 自动

##### Code folding

- `opt+cmd+[/]` 收缩展开 fold/unfold. 添加了新的快捷键 `opt+q/w`
- `cmd+K cmd+0` `cmd+K cmd+]` 完全收缩/展开

##### Errors and warnings

- `F8` 定位到错误处



### 主题配置

**为啥折腾编辑器主题**? 好的主题看上去比较舒服 (比如在不同的光线环境下); 新鲜的, 优雅的UI提升工作效率.

**配置方法**: Commands搜索 `theme`, 包括 Color, File Icon, Dark/Light 切换.

#### Color Theme 颜色主题

推荐

- Light: Quiet, Solarized, defaults.
- Dark: defaults, One Dark Pro.

#### File Icon 文件图标主题

需要搜索下载插件. 推荐

- VSCode Icons
- Material Icon Theme

## 推荐插件

一些基本好用的vscode插件, 配合自己的工作流. 具体编程语言的环境配置见下. 

强推的

- 代码补全: GitHub Copilot `GitHub.copilot` Your AI pair programmer ⭐️
- 远程开发: Remote - SSH `ms-vscode-remote.remote-ssh` ⭐️
    - 打开远程服务器, 直接 编辑/调试, 超好用. 
    - **推荐工作流**: 本地编辑, 配合下面的 SFTP进行代码上传, 然后远程调试. 
    - 对应了侧边栏的 `Remote Explorer` 页, 还记录了历史访问, 很方便.
        - 默认会读取 `~/.ssh/config` 中的SSH配置项, 显示在侧边栏. 
    - 如何关联服务器? 因此可以直接编辑 `~/.ssh/config` 文件, 还可以搭配ssh的免密登录方案.
- 文件同步: SFTP `Natizyskunk.sftp`
- 浏览器打开: Live Server `ritwickdey.LiveServer`
    - Launch a development local Server with live reload feature for static & dynamic pages
- ASCII编码转换: Native-ASCII Converter `cwan.native-ascii-converter`
    - Convert characters with Unicode escapes or vice versa. The same as 'native2ascii' tool of JDK.
    - 例如一些 Unicode escapes 的JSON文件, 可以转为中文字符.


其他的

- 中文插件: `MS-CEINTL.vscode-language-pack-zh-hans` 影响不大, 但中文翻译不错
- 二进制文件查看: Hex Editor `ms-vscode.hexeditor` 用的不多
- 文件模板: `rhangai.file-template`. 比较小众的需求? 
- 背单词: Qwerty Learner `kaiyi.qwerty-learner` 肌肉记忆背单词. 摸🐟版

### Copilot

微软nb! 申请 GitHub 学生认证之后开箱即用.

### SFTP

**作用**: 在本地编辑文件, 保存的时候自动上传到服务器. 好处是在本地留有代码存档, 而代码运行和模型文件都在服务器上. 

- 版本说明: 原先的一个好像不维护了, 现在用的是 `Natizyskunk.sftp` 这个版本
- 需求
    - 如何同步到多台服务器? 若是分别同步不同的文件夹, 见下. 若要直接同步, 暂不清楚, 我的解决方案是在服务器上安装 `syncthing`.

#### 需求: 多个服务器同步

from Liximomo 版本的插件说明 <https://github.com/liximomo/vscode-sftp#multiple-context> ；

多个服务器同步：目前用 `multi-context` ，这里 context 指的是（见wiki） string - A path relative to the workspace root folder. Using this when you want to map a subfolder to the remotePath.

例如，以下配置中，分别将 build 和 src 两个文件夹部署到了两台服务器上。

```json
[
  {
  "name": "server1",
  "context": "project/build",
  "host": "host",
  "username": "username",
  "password": "password",
  "remotePath": "/remote/project/build"
  },
  {
  "name": "server2",
  "context": "project/src",
  "host": "host",
  "username": "username",
  "password": "password",
  "remotePath": "/remote/project/src"
  }
]
```

## 各编程语言插件配置


### Markdown

在笔记软件上折腾了挺多, 现在的基本方案是 vscode 为主进行纯文本编辑, 并考虑一定的软件兼容性. 由于内容较多, 另见 [[vscode-markdown.md]]


### Python

参见 <https://code.visualstudio.com/docs/python/python-tutorial>. 其实官方的那一个拓展基本就够用了, Python的配置难度很低. 配合 Copilot 使用体验更佳.

有一些Python开发的配拓展包 (Python Extension Pack), 例如 `donjayamanne.python-extension-pack` 等. 但不太适合DL, 不建议全部安装.

在用的拓展

- 官方的 Python 拓展 `ms-python.python` 很好用 ⭐️ 
    - IntelliSense (Pylance), Linting, Debugging (multi-threaded, remote), Jupyter Notebooks, code formatting, refactoring, unit tests, and more.
- 缩进 `KevinRose.vsc-python-indent` Python Indent 提供了更方便的Python代码编辑体验
    - Correct python indentation. 
- IntelliCode `VisualStudioExptTeam.vscodeintellicode` 测试使用中.
    - AI-assisted development
    - 注意需要配置 `Pylance` as the Python language server

其他/没用过的

- 环境管理 `donjayamanne.python-environment-manager` Python Environment Manager
    - View and manage Python environments & pacakges.
    - 但一般直接用conda命令来管理也很方便, 没咋用过.
- 自动化文档 `njpwerner.autodocstring` autoDocstring - Python Docstring Generator
    - Generates python docstrings automatically 有助于写比较规范的文档, 正式开发可能有用? 

文档! doc first!

- debugging <https://code.visualstudio.com/docs/python/debugging>
- testing <https://code.visualstudio.com/docs/python/testing>
- torch <https://code.visualstudio.com/docs/datascience/pytorch-support>

### C/C++

refs

- 官方的基本配置教程 <https://code.visualstudio.com/docs/languages/cpp>. 
- 搭配更详细的文档, 根据不同的编译环境有区别, 例如 macOS 下的 clang <https://code.visualstudio.com/docs/cpp/config-clang-mac>. 下面基本是教程翻译.

插件

- 官方的 C/C++ `ms-vscode.cpptools` ⭐️
    - C/C++ IntelliSense, debugging, and code browsing.

其他没用过的插件

- ms-vscode.cpptools-themes: UI Themes for C/C++ extension.
- twxs.cmake: CMake langage support for Visual Studio Code
- ms-vscode.cmake-tools: Extended CMake support in Visual Studio Code
- The bleeding edge of the C++ syntax: Let me generate Doxygen documentation from your source code for you.
    - jeff-hykin.better-cpp-syntax: The bleeding edge of the C++ syntax
- `mitaki28.vscode-clang` C/C++ Clang Command Adapter
    - Completion and Diagnostic for C/C++/Objective-C using Clang Command

#### C++ Run (运行)

关联名词: **生成 Build** 

- 和 Run 的区别, 大概在于, 仅编译不运行
- **如何Build**? 点击 `Terminal > Run Build Task` (终端/运行生成任务); 快捷键 `Shift+cmd+B`. 
- 没有 bug的话可以在相同目录下看到生成的文件了.

基本的 Run

- **如何配置Run**? 同样可以点选 `Terminal > Configure Default Build Task` (终端/运行任务) 来运行配置好的任务. 对于active的文件, 也可以简单点击右上角的三角形, 「Run C/C++ Code」以运行. 
    - 第一次出来会提示选择配置. 例如macOS环境下可以选择 `clang++`
    - 配置文件见下
- **运行的时候发生了什么**? 先 Build 然后运行.
    - 具体而言, 根据配置task执行相应的命令行命令.
    - 本质上, tasks 的配置影响了vscode如何调用命令行命令来进行编译.
    - 例如, 下面的配置就会运行 `/usr/bin/clang++ -fcolor-diagnostics -fansi-escape-codes -g "xxx.cpp" -o "xxx"`
    - 点击运行, 可以在Terminal窗口看到编译记录; 在 Debug 窗口看到程序的输出结果.

`tasks.json` 文件: 

- 根据上面的选择, 会在 `.vscode/tasks.json` 中记录配置项. 见下面默认生成的配置.
- 可以有多条配置的 task, 通过 group.isDefault 进行控制默认运行哪个.
- 相关参数
    - `args`: 编译选项

补充: 若是安装了 `Code Runner` 插件, 也可以在三角形上点「Run Code」, 直接可以运行, 不需要配置 tasks 还不会生成 `*.dSYM` 文件夹, 推荐 ⭐️


```json
// .vscode/tasks.json
// 配置项说明见 https://code.visualstudio.com/docs/editor/variables-reference
{
    "version": "2.0.0",
    "tasks": [
        // 自动生成的 clang++ 配置文件.
        // 运行的命令: /usr/bin/clang++ -fcolor-diagnostics -fansi-escape-codes -g "xxx.cpp" -o "xxx"
        {
            "type": "cppbuild",
            "label": "C/C++: clang++ 生成活动文件",
            "command": "/usr/bin/clang++",
            "args": [
                "-fcolor-diagnostics",
                "-fansi-escape-codes",
                "-g",
                "${file}",
                "-o",
                "${fileDirname}/${fileBasenameNoExtension}"
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "调试器生成的任务。"
        }
    ]
}
```


#### C++ Debug (调试)

- 基本使用: 和 Run一样, 在右上角的三角的地方, 下拉选择「调试 C/C++ 文件」即可.
    - 调试控制栏比较直观, 详见doc

自定义调试: `F5` 

- **是什么**? 相较于上面的基本调试方式, 还可以按 `F5` 进行个性化的配置. 一个需求: specifying arguments to pass to the program at runtime.
- **如何配置**? 在active的文件中, 点击右上角的齿轮⚙️ 进行配置 (好像也可以 `Run/Add Configuration...` 添加). 同样选择 clang++
- **如何开始调试**? start debug with `Run > Start Debugging` or simply press `F5`

`launch.json` 文件 

- 默认也会生成 `.vscode/launch.json` 配置文件. 相关选项说明见下.
- 相关参数
    - `program`: 指定调试的文件
    - `args`: 传入的命令行参数
    - `preLaunchTask`: 运行的编译命令, 注意要和 `tasks.json` 中的相对应!!

```json
// .vscode/launch.json
// 配置说明见 https://code.visualstudio.com/docs/editor/debugging#_launch-configurations
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "C/C++: clang++ 生成和调试活动文件",
            "type": "cppdbg",
            "request": "launch",
            // The `program` setting specifies the program you want to debug.
            "program": "${fileDirname}/${fileBasenameNoExtension}",
            // The `args` property is an array of arguments to pass to the program at runtime.
            "args": [],
            "stopAtEntry": false,
            "cwd": "${fileDirname}",
            "environment": [],
            // Change the `stopAtEntry` value to `true` to cause the debugger to stop on the `main` method when you start debugging.
            "externalConsole": false,
            "MIMode": "lldb",
            // Ensure that the `preLaunchTask` value matches the `label` of the build task in the `tasks.json` file.
            "preLaunchTask": "C/C++: clang++ 生成活动文件"
        }
    ]
}
```

#### C/C++ configuration

- 什么用? 
- 在 Command 中搜索 `C/C++: Edit Configurations (UI)` 可以打开配置UI, 对应了文件 `.vscode/c_cpp_properties.json`
- 一些选项说明
    - `includePath`: 用于用于一些非标准库
    - `compilerPath`: 指定编译器路径, 插件以此来推断头文件位置, 以启用更准确的 IntelliSense
    - `cppStandard`: 影响插件的语法高亮和标错等行为



```json
{
    "configurations": [
        {
            "name": "Mac",
            // You only need to modify the Include path setting if your program includes header files that are not in your workspace or the standard library path.
            "includePath": [
                "${workspaceFolder}/**"
                // "/usr/local/Cellar/gcc/11.3.0_1/include/c++/11/x86_64-apple-darwin20"
                // "/usr/bin/**"
            ],
            "defines": [],
            
            // Mac framework path. ensure that Mac framework path points to the system header files. 
            "macFrameworkPath": [
                "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/System/Library/Frameworks"
            ],
            // Compiler path 重要!! 指定正在使用的编译器的完整路径(例如 /usr/bin/gcc), 插件以此来推断头文件位置, 以启用更准确的 IntelliSense
            // 例如, 决定了 smart completions and Go to Definition navigation 这些功能
            // The extension uses it to infer the path to the C++ standard library header files. 
            "compilerPath": "/usr/bin/clang++",

            // 用于 IntelliSense 的 C 语言标准的版本。注意: GNU 标准仅用于查询设置编译器以获取 GNU 定义，并且 IntelliSense 将模拟等效的 C 标准版本。
            "cStandard": "c11",
            // 用于 IntelliSense 的 C++ 语言标准的版本。注意: GNU 标准仅用于查询设置用来获取 GNU 定义的编译器，并且 IntelliSense 将模拟等效的 C++ 标准版本。
            "cppStandard": "c++17",
            // 要使用的、映射到 MSVC、gcc 或 Clang 的平台和体系结构变体的 IntelliSense 模式。
            "intelliSenseMode": "clang-x64"
            // 可为源文件提供 IntelliSense 配置信息的 VS Code 扩展的 ID。
            // "configurationProvider": "ms-vscode.makefile-tools"
        }
    ],
    "version": 4
}
```


### go

ref

- 中文教程，讲得很系统 <https://learnku.com/courses/go-video/2022>
- base <https://code.visualstudio.com/docs/languages/go>
- debugging <https://github.com/golang/vscode-go/blob/master/docs/debugging.md>
- install go: <https://golang.org/dl/>
- go语言基础 [Go语言学习之路/Go语言教程](https://www.liwenzhou.com/posts/Go/golang-menu/)


插件

- `Go`: Rich Go language support for Visual Studio Code

以下 from [learnku](https://learnku.com/courses/go-video/2022/vscode-go-plug-in-details/11314)

- 悬停信息
- 代码补全
- 包自动引入
- 参数辅助
    - 书写函数，在传参括号里输入 `,`  即可查看参数信息
- 代码跳转
    - 按住 Command 鼠标点击函数名称
    - 按住 Control 加 - 号（减号）
- 查找调用
    - 光标放置于函数上，右键 `Go to References`
    - 光标放置于函数上，右键 `Show call Hierarchy`
- 自动格式化（默认，无需配置）
- 提取变量（选中一个表示式之后，前面自动出现一个小黄灯）
- 代码生成
    - 生成 tag
    - 生成 struct
    - 生成单元测试
    - 生成接口的实现代码
- 重构函数名和变量
- 代码调试 —— Debuging


### Java

略

- `vscjava.vscode-java-pack` 拓展包
    - redhat.java Language Support for Java(TM) by Red Hat
        - Java Linting, Intellisense, formatting, refactoring, Maven/Gradle support and more...
    - vscjava.vscode-java-debug A lightweight Java debugger for Visual Studio Code

### R

R语言的支持似乎没有 Rstudio 的体验那么好. 略.

- `R` Extension for Visual Studio Code <https://github.com/REditorSupport/vscode-R> base
    - `radian`: A modern R console that corrects many limitations of the official R terminal and supports many features such as syntax highlighting and auto-completion.
    - `VSCode-R-Debugger`: A VS Code extension to support R debugging capabilities.
    - `httpgd`: An R package to provide a graphics device that asynchronously serves SVG graphics via HTTP and WebSockets.
    - installation: <https://github.com/REditorSupport/vscode-R/wiki/Installation:-macOS>
    - R Markdown: <https://github.com/REditorSupport/vscode-R/wiki/R-Markdown>
- `TianyiShi.rmarkdown` R Markdown All in One
    - R Markdown, Bookdown and Blogdown Support


### SQL

**说明**: vscode 写sql的优势在于编辑体验+补全等功能. 不过数据库管理等还是用 Navicat 更为直观.

- SQL Tools
    - `mtxr.sqltools` 插件本体
    - mtxr.sqltools-driver-mysql 搭配的 mysql 驱动

配置如下:

```json
// settings.json
    "sqltools.connections": [
        {
            "mysqlOptions": {
                "authProtocol": "default"
            },
            "previewLimit": 50,
            "server": "10.88.3.55",
            "port": 3306,
            "driver": "MySQL",
            "name": "BOC",
            "database": "bocom",
            "username": "boc",
            "password": "boc"
        },
    ]
```

运行: 选中查询语句, 然后两次 `Cmd+E` 执行.

### Latex

整理中, 略.

#### VSCode-LaTeX-Workshop

参见: Latex 项目中的配置文件.

- 简单配置方案：[MacOS10.15.3+MacTex (TexLive2019)+VS Code的LaTex教程](https://zhuanlan.zhihu.com/p/107393437)
    - 更详细的参数参见 [Visual Studio Code (vscode)配置LaTeX](https://zhuanlan.zhihu.com/p/166523064)
- 若要配置外部PDF浏览器（Skim），参见 [macOS 配置 LaTeX（MacTeX + VSCode + Skim）](https://www.jianshu.com/p/4aee83e66ab8)
- Latex 资源
    - ElegantLatex [https://elegantlatex.org/cn/](https://elegantlatex.org/cn/) 提供了三套模版
- 蔡老板的作业模版 [https://github.com/YZ-Cai/latex-homework-template](https://github.com/YZ-Cai/latex-homework-template)

注意一定要添加 Latex 路径 `export PATH=/Library/Tex/texbin:$PATH`

```sh
export PATH=/usr/local/texlive/2021/bin/x86_64-linux:$PATH
export PATH=/usr/local/texlive/2021/texmf-dist/scripts/latexindent:$PATH
export MANPATH=/usr/local/texlive/2021/texmf-dist/doc/man:$MANPATH
export INFOPATH=/usr/local/texlive/2021/texmf-dist/doc/info:$INFOPATH
```

快捷键

```js
编译快捷键：Command+Option+B
显示快捷键：Command+Option+V
正向搜索：选中代码Command+Option+J
反向搜索：shift+command点击预览PDF
```


#### 使用 VS Code 远程编译

- 参见 [使用 VSCode 编写 LaTeX](https://codeswift.top/posts/vscode-latex/) ⭐️
- [东南大学研究生 Latex 模版](https://github.com/TouchFishPioneer/SEU-master-thesis)
    - 其中用到的字体 [CodeSwift-Comment](https://github.com/NiallLDY/CodeSwift-Comment)

远程安装 TexLive

```sh
# 安装 TexLive
sudo apt update
sudo apt upgrade
sudo apt install texlive-full
```

VS Code 远程连接，安装 LaTeX Workshop 拓展

进行配置，注意 Preferences: Open Workspace Settings (JSON) （Ctrl + Shift + P 命令面板）等选项中，工作区设置、远程设置、本地设置 这些区别。注意配置更新之后 Reload Window 重新加载窗口。

另外，字体问题，从 [这里](https://github.com/NiallLDY/CodeSwift-Comment) 下载放置好之后，以下刷新字体缓存

```sh
# 查看字体
fc-list :lang=zh

# 在 /usr/share/fonts/myfonts 中下载字体，更新字体缓存
mkfontscale
# 如果提示 mkfontscale: command not found
# sudo apt install ttf-mscorefonts-installer
mkfontdir
fc-cache -fv
# 如果提示 fc-cache: command not found
# sudo apt install fontconfig
```

Latex 有很多编译工具，常见的主要有 LaTeXmk、pdfLaTeX、XeLaTeX、LuaLaTeX 等，因为我们需要输出包含中文的 PDF，因此我们使用 XeLaTeX 工具。


## archive

不再使用的插件, archive

- Bracket Pair Colorizer 2 高亮区分匹配的括号，方便查看代码块 (vscode 自带了)
- Emmet HTML 简写（vscode 自带了）
- Bookmark 代码标记
- Rest Client API 开发
- Thunder Client API开发，参见 <https://www.boredapi.com/>
- Prettier 开启 format on save 功能
- Auto Close Tag 自动关闭标签
- Auto Rename Tag 自动更新标签名称

git

- GitLens
- gitignore 预定义的一些 gitignore 配置

中文 <-> 转义后的ASCII (例如json)

- `cwan.native-ascii-converter` Native-ASCII Converter
    - Convert characters with Unicode escapes or vice versa. The same as 'native2ascii' tool of JDK.

## Debug

记录使用过程中踩过的坑.

### Copilot: 在 Markdown 环境下无法 tab 补全

主要是快捷键问题. 参见 [here](https://github.com/microsoft/vscode/issues/130674)

Copilot 的补全属于 `editor.action.inlineSuggest.commit`. 设置为 `Tab` 即可补全.

查下来的问题好像是和 `markdown.extension.onTabKey` 发生了冲突, 不过后来重新设置一下又可以了?


### 性能: 内存占用

主要的解决方案, 还是少开一些window.

### 性能问题 (高CPU)

参见 <https://github.com/microsoft/vscode/wiki/Performance-Issues>

相关工具

```sh
# 查看进程占用 (帮助 - 进程管理器)
Developer: open process explorer
# or 在终端运行 code --status

# 查看插件占用
Developer: Show Running Extensions
# 命令行 code --disable-extensions

# 启动速度
Startup Performance.
# 命令行 code --prof-startup
```

介绍了常见的问题

- The Renderer/Window process consumes a lot of CPU
- The Shared process consumes a lot of CPU

### 无法监测大文件夹 "Visual Studio Code is unable to watch for file changes in this large workspace" (error ENOSPC)

参见 [这里](https://code.visualstudio.com/docs/setup/linux#_visual-studio-code-is-unable-to-watch-for-file-changes-in-this-large-workspace-error-enospc) ，到设置中添加 `files.watcherExclude` 项即可。很贴心的是，Code 的配置包括了 User, Remote, Workspace 不同的作用域。

```bash
**/venv/**
```

### VS Code调试Python时的执行路径

通过 `print(os.getcwd())` 打印当前路径

解决方案: 配置 launch.json

```json
"cwd": "${fileDirname}"
```

- os.chdir设置当前工作目录

```python
import os, sys
# 设置当前工作目录，放在import其他路径模块之前
os.chdir(sys.path[0])
 
# 导入上上级目录
sys.path.append("../../")
# 引入上上级目录下的模块
from submodulea.modulea import *
```

- sys.path.append添加顶层文件夹相对路径

```python
import os,sys
# 注意默认工作目录在顶层文件夹，这里是相对于顶层文件夹的目录
sys.path.append("./")
 
# 导入上上级目录
sys.path.append("../../")
```

### windows 环境说明

- `git`: 根据vscode的提示下载, 若安装之后提示招不到, 可以在设置中配置 `git.path` 参数.
- 中文设置采用英文标点: 在 `设置-语言-微软拼音-常规设置` 中点开 `中文输入时使用英文标点`.
    - 好吧, 实际上在底部的输入中也可以设置, 快捷键 `Ctrl+。`.


## 附: setting.json

```json
{
    /*vscode 配置参考
    v1 221011 @Lightblues 
    
    本文档是什么? vscode的全局配置文件, 主要是vscode及其插件的配置项.
        在command中搜索 `Preference: Open User Settings (JSON)` 即可打开 (对应的命令是 `@command:workbench.action.openSettingsJson`)
        对应了 `Preference: Open User Settings` 是可视化的编辑
        地址: 例如在macOS中是 `~/Library/Application Support/Code/User/settings.json`, 该目录下还有vscode的其他配置文件.
    主要内容 & 作用
        以下主要包括: 1) vscode 的基本配置项; 2) 常用语言的简单配置; 3) 其他一些插件 推介/配置.
        作用: 结合vscode的官方doc, 参考阅读下面的配置, 可以更快的理解vscode的基本功能和插件生态.
    使用建议
        不建议无脑复制使用. 请在阅读下面官方文档, 理解每一条配置项含义的基础上, 按需选择. 
        **less is more**. 有些配置项的含义我也有些模糊了, 时间原因暂且留着, 不理解具体作用的话不建议使用. 
        有些配置项是针对插件的, 需要安装后才能生效. (例如 `"markdownlint.confi"`) 若没有安装该插件, vscode会标灰. 按需安装使用.
        插件搜索: 一般搜索名字即可, 可以通过 `@id:DavidAnson.vscode-markdownlint` 语法进行更精准的搜索.
    ref
        官方文档: https://code.visualstudio.com/docs
    申明: 仅个人使用记录, 颇多谬误, 仅供参考.
    */

    /* ####################### PART 1. 基础/通用 配置 #######################
    vscode (或者自带的一些插件?) 的基本配置项. 例如editor类下定义的一些行为对于所有编程语言都生效. 
    */
    // 同步时要忽略的扩展列表。扩展的标识符始终为 "${publisher}.${name}"。例如: "vscode.csharp"。
    "settingsSync.ignoredExtensions": [
        "ms-vscode.cpptools-extension-pack",
        "mitaki28.vscode-clang",
        "vscjava.vscode-java-pack"
    ],

    // ======== editor ========
    // bracket matching 原本是插件功能现在原生了 https://github.com/CoenraadS/Bracket-Pair-Colorizer-2
    "editor.bracketPairColorization.enabled": true,     // 控制是否启用括号对着色
    "editor.guides.bracketPairs": "active",
    // 限制缩略图的宽度，控制其最多显示的列数。
    "editor.minimap.maxColumn": 40,                     // 左侧 minimap 更窄一点
    // 执行单词相关的导航或操作时作为单词分隔符的字符。
    "editor.wordSeparators": "`~!@#$%^&*()-=+[{]}\\|;:'\",.<>/?·～！￥…（）—【】、；：‘’“”，。《》？ 「」", // 设置分词，在双击选中一串字符序列时，VSCode就会依此来区分词
    // "editor.fontFamily": "'Source Code Pro', Consolas, 'Courier New', monospace",
    "editor.suggest.localityBonus": true,               // 控制排序时是否首选光标附近的
    "editor.suggestSelection": "first",         // 控制在建议列表中如何预先选择建议。
    "editor.linkedEditing": true,               // 控制编辑器是否已启用链接编辑。相关符号(如 HTML 标记)在编辑时进行更新，具体由语言而定。
    "editor.inlineSuggest.enabled": true,
    "editor.codeActionsOnSave": {
        // 在保存文件时自动进行修复
        "source.fixAll.markdownlint": true
    },
    // 定义一个默认格式化程序, 该格式化程序优先于所有其他格式化程序设置。必须是提供格式化程序的扩展的标识符。
    // "editor.defaultFormatter": "esbenp.prettier-vscode",   // "esbenp.prettier-vscode",
    "editor.formatOnSave": true, // 自动进行 format
    // ps 下面这一段抄了 [markdown] 配置部分，但不知道为啥 Markdown 无法显示提示
    "editor.quickSuggestions": {
        "other": true,
        "comments": true,
        "strings": true
    },
    "editor.snippetSuggestions": "top",     // snippet 提示优先
    "editor.tabCompletion": "on",           // 启用 Tab 补全。
    // 控制除了 Tab 键以外， Enter 键是否同样可以接受建议。这能减少“插入新行”和“接受建议”命令之间的歧义。
    "editor.acceptSuggestionOnEnter": "on",
    // 控制在基于文件内容打开文件时是否自动检测 #editor.tabSize# 和 #editor.insertSpaces#。
    "editor.detectIndentation": false,      // 关闭检测第一个tab后面就tab
    "editor.renderControlCharacters": true, // 制表符显示->
    "editor.renderWhitespace": "all",       // 空格显示...
    "editor.tabSize": 4,                    // tab为四个空格
    "editor.insertSpaces": true,            // 按 Tab 时插入空格。
    "editor.inlayHints.enabled": "on",      // 在编辑器中启用内联提示。
    "editor.accessibilitySupport": "off",   // 控制编辑器是否应在对屏幕阅读器进行了优化的模式下运行。设置为“开”将禁用自动换行。
    // 去除容易混淆的例如中文括号的高亮显示
    "editor.unicodeHighlight.allowedLocales": {
        "zh-hans": true,
        "zh-hant": true
    },
    "editor.unicodeHighlight.allowedCharacters": {
        "：": true
    },

    // ================ windows =================
    // "window.title": "${dirty}${activeEditorLong}${separator}${rootName}${separator}${appName}", // 标题名字
    // "window.zoomLevel": 1,
    // "window.titleBarStyle": "custom",

    // ================ workbench =================
    "workbench.iconTheme": "material-icon-theme",   // 图标
    "workbench.colorTheme": "One Dark Pro",         // 颜色
    // "workbench.sideBar.location": "right",       // 移动控制栏的位置
    "workbench.editorAssociations": {
        "*.ipynb": "jupyter-notebook",
        "*.pdf": "default"
    },
    // 单击文件进入预览模式, 默认即为 true
    "workbench.editor.enablePreview": true,

    "explorer.confirmDragAndDrop": false,
    "explorer.confirmDelete": false,


    // ======== others ==========
    // 控制如何处理在受信任的工作区中打开不受信任的文件。
    "security.workspace.trust.untrustedFiles": "open",

    // 允许在任何文件中设置断点。
    "debug.allowBreakpointsEverywhere": true,
    
    // 要使用的代理设置。如果未设置，则将从 "http_proxy" 和 "https_proxy" 环境变量中继承
    // "http.proxy": "http://127.0.0.1:7890",

    // A map of the remote hostname to the platform for that remote.
    "remote.SSH.remotePlatform": {
        "124": "linux"
    },

    // ================ terminal =================
    "terminal.integrated.inheritEnv": false,
    // 将多行粘贴到终端时显示警告对话框
    "terminal.integrated.enableMultiLinePasteWarning": false,

    // ============== files =================
    // Code Helper high CPU usage
    // https://github.com/microsoft/vscode/issues/11963#issuecomment-317830768
    "files.watcherExclude": {
        ".pycharm_helpers/**": true,
        "**/miniconda3/**": true,
        "**/.git/objects/**": true,
        "**/.git/subtree-cache/**": true,
        "**/node_modules/**": true,
        "**/bower_components/**": true,
        "**/dist/**": true
    },
    // 直接将文件排除显示
    "files.exclude": {},
    // 配置语言的文件关联 (如: "*.extension": "html")。这些关联的优先级高于已安装语言的默认关联。
    "files.associations": {
        "*.jsonl": "jsonc"
    },

    /* ####################### PART 2. 按编程语言的 (插件)配置 #######################
    以下是分编程语言的配置. 请根据自己的需要进行修改.
    使用建议: 
        首先根据官方文档安装相应插件, 理解插件的作用.
        下面的部分是默认就有的配置项, 部分是需要安装好插件之后才可启用的.
    */
    // ================== 插件配置: Python ==================
    // https://code.visualstudio.com/docs/python/python-tutorial
    // "python.defaultInterpreterPath": "/Users/easonshi/miniconda3/bin/python",
    "[python]": {
        // 控制是否根据文档中的文字计算自动完成列表。
        "editor.wordBasedSuggestions": false
    },
    // Python格式化工具. Provider for formatting. Possible options include 'autopep8', 'black', and 'yapf'.
    // "python.formatting.provider": "autopep8",

    "jupyter.sendSelectionToInteractiveWindow": true,
    "jupyter.askForKernelRestart": false,
    "jupyter.alwaysTrustNotebooks": true,
    "jupyter.interactiveWindowMode": "perFile",

    "notebook.cellToolbarLocation": {
        "default": "right",
        "jupyter-notebook": "left"
    },
    "notebook.lineNumbers": "on",

    // ================ 插件配置：markdown =================
    // Markdown 配置 see https://www.thisfaner.com/p/edit-markdown-efficiently-in-vscode/
    "[markdown]": {
        // 快速补全
        "editor.quickSuggestions": {
            "other": true,
            "comments": true,
            "strings": true
        },
        "editor.renderWhitespace": "all",
        "editor.snippetSuggestions": "top",
        "editor.tabCompletion": "on",
        "editor.acceptSuggestionOnEnter": "on",     // 使用enter 接受提示
        // "editor.defaultFormatter": "yzhang.markdown-all-in-one"
        "editor.defaultFormatter": "vscode.markdown-language-features"
    },
    // === markown === 
    "markdown.preview.breaks": true,
    // === markdownlint === 
    "markdownlint.config": {
        "default": true,
        "no-multiple-blanks": false,
        "MD003": {
            "style": "atx"
        },
        "MD007": {
            "indent": 4
        },
        "MD009": false,
        "MD013": false,
        "MD001": false,
        "MD022": false,
        "MD025": false,
        "MD040": false,
        "MD029": false,
        "MD036": false,
        "MD041": false,
        "MD045": false,
        "MD046": false,
        "MD033": false,
        "MD052": false
    },
    // === Markdown Preview Enhanced | shd101wyy.markdown-preview-enhanced ===
    "markdown-preview-enhanced.previewTheme": "none.css",
    // === markdown-all-in-one ===
    // 设置 list 中的缩进, inherit 表示和 VSCode 右下角的设置一样; 和 markdownlint 冲突
    // "markdown.extension.list.indentationSize": "inherit",
    // === Paste Image | mushan.vscode-paste-image ===
    "pasteImage.path": "${currentFileDir}/media/${currentFileNameWithoutExt}",


    // ================ 插件配置：go =================
    "go.useLanguageServer": true,
    "go.toolsManagement.autoUpdate": true,
    "go.inferGopath": true,
    "go.lintTool": "golint",

    // ================ 插件配置：R =================
    // https://github.com/REditorSupport/vscode-R/issues/431 在环境中配置 R_Home (使用 R 中 R.home 函数查看)
    "terminal.integrated.env.osx": {
        "R_HOME": "/Library/Frameworks/R.framework/Resources",
        "PATH": "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/Library/Frameworks/R.framework/Resources/bin:$PATH",
        "FIG_NEW_SESSION": "1"
    },
    // "terminal.integrated.defaultProfile.osx": "zsh",
    // "r.rpath.mac": "/usr/local/bin/radian", //"/Users/easonshi/miniconda3/bin/radian",
    "r.alwaysUseActiveTerminal": true,
    "r.bracketedPaste": true,
    "r.rterm.mac": "/usr/local/bin/radian", //
    // "r.rterm.mac": "/Users/easonshi/miniconda3/bin/radian",
    "r.rterm.option": [
        "--no-site-file"
    ],
    "r.rtermSendDelay": 8,
    "r.plot.useHttpgd": true,

    // ================ 插件配置：cpp =================
    // 推荐的 C/C++ Extension Pack 包中包括了下面这些插件，以及远程开发包
    // C/C++ | ms-vscode.cpptools:  IntelliSense and debugging
    // C/C++ Extension | ms-vscode.cpptools-themes: 颜色主题
    // CMake | twxs.cmake: provides support for CMake in Visual Studio Code.
    // CMake Tools | ms-vscode.cmake-tools: provides the native developer a full-featured, convenient, and powerful workflow for CMake-based projects in Visual Studio Code.
    // Doxygen Documentation Generator | cschlosser.doxdocgen: 帮助写文档/注释
    // Better C++ Syntax | jeff-hykin.better-cpp-syntax: 语法高亮 the bleeding-edge syntax highlighting for C++
    // == mitaki28.vscode-clang
    "clang.cxxflags": [
        "-std=c++17" // 不然类似 vector<int> children = {1, 2, 3} 的会语法报错
    ],
    "[cpp]": {
        "editor.wordBasedSuggestions": false,
        "editor.suggest.insertMode": "replace",
        "editor.semanticHighlighting.enabled": true,
        "editor.formatOnSave": false
    },
    // cmake
    "cmake.configureOnOpen": true,

    // ================ 插件配置：sql =================
    "[sql]": {
        "editor.formatOnSave": false,
        "editor.formatOnPaste": false,
        "editor.formatOnType": false
    },
    // ================ 插件配置：json =================
    "[json]": {
        "editor.defaultFormatter": "vscode.json-language-features",
        // "editor.defaultFormatter": "esbenp.prettier-vscode"

        "editor.formatOnSave": false
    },
    "[jsonc]": {
        "editor.defaultFormatter": "vscode.json-language-features",
        "editor.formatOnSave": false
    },

    // ================ 插件配置：html =================
    "[html]": {
        "editor.defaultFormatter": "vscode.html-language-features"
    },

    // ================ 插件配置：git =================
    "git.autofetch": true,
    "git.confirmSync": false,
    "git.enableSmartCommit": true,
    // === gitlens ===
    "gitlens.hovers.currentLine.over": "line",



    /* ####################### PART 3.1 其他的一些好用的插件配置 #######################
    */
    // ==== Copilet ====
    "github.copilot.enable": {
        "*": true
        // "yaml": true,
        // "plaintext": true,
        // "markdown": true,
        // "go": true
    },


    /* ####################### PART 3.2 其他的一些 较少使用/已弃用 的插件配置 #######################
    其中的部分已弃用, 没必要查看, 有时间再做整理.
    */
    // === code-runner === 
    "code-runner.runInTerminal": true,
    "code-runner.saveAllFilesBeforeRun": true,
    "code-runner.saveFileBeforeRun": true,
    "code-runner.clearPreviousOutput": true,
    // === Live Server | ritwickdey.liveserver ===
    "liveServer.settings.donotShowInfoMsg": true,
    "liveServer.settings.donotVerifyTags": true,

    // ==== projectManager ===
    "projectManager.git.baseFolders": [
        "/Users/frankshi/Projects"
    ],
    "projectManager.any.maxDepthRecursion": 2,
    "projectManager.any.baseFolders": [
        "/Users/frankshi/Projects"
    ],

    // === qwerty ===
    "qwerty-learner.phonetic": "us",

    // === kite ===
    "kite.showWelcomeNotificationOnStartup": false,
    // === dendron ===
    "dendron.serverPort": 8090,
    "dendron.trace.server": "verbose",
    "redhat.telemetry.enabled": true,
    "hexo.sortMethod": "date",

    // === prettier ===
    "prettier.embeddedLanguageFormatting": "off",
    // 和 "MD030" 有一定冲突, 见 https://github.com/DavidAnson/markdownlint/blob/v0.25.1/doc/Prettier.md
    "prettier.tabWidth": 4,
    
    // === tabnine ===
    // "tabnine.experimentalAutoImports": true,
    //  === todohighlight ===
    "todohighlight.isEnable": false,
    // === leetcode ====
    // https://github.com/LeetCode-OpenSource/vscode-leetcode/blob/master/docs/README_zh-CN.md
    // "leetcode.endpoint": "leetcode-cn",
    // "leetcode.hint.configWebviewMarkdown": false,
    // "leetcode.workspaceFolder": "/Users/easonshi/Projects/leetcode/plugin",
    // "leetcode.hint.commentDescription": false,
    // "leetcode.defaultLanguage": "golang",
    // "leetcode.editor.shortcuts": ["submit", "solution", "test", "star"], // "staticcheck"
    // "leetcode.hint.commandShortcut": false,
    // "leetcode.hint.setDefaultLanguage": false,

    // === bookmarks ===
    "bookmarks.useWorkaroundForFormatters": true
}
```
