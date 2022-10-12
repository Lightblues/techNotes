# VS Code 使用指南

> v1 221012 @Lightblues

说明

1. 本文档是什么? 个人vscode工作流. 
2. 如何使用? 搭配参考链接; 实践第一. 
3. 插件使用
   1. 插件配置: 在进行插件配置时, 注意参看附的 [settings.json](#settingjson), 更加方便.
   2. 插件选择: 对于不是通用的插件, 可以选择「工作区打开」打开而非全局开启, 简洁并提升性能.
4. 性能说明: 
   1. 内存: 例如对于8G的Mac来说, 需要考虑的是内存占用问题. Electron 框架下没啥办法, 个人经验是少开点窗口 (个人经常开5+个项目就可能不太行了)
   2. 插件: 精简为妙. 

todo

- Python 工作流介绍 @221012
- debug (launch.json) 说明: 见 Python 部分 @221012
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

read official doc first!

- 参见 <https://code.visualstudio.com/docs/python/python-tutorial>. ⭐️
    - 其实官方的那一个拓展基本就够用了, Python的配置难度很低. 配合 Copilot 使用体验更佳.
    - 有一些偏向 Python开发的配拓展包 (Python Extension Pack), 例如 `donjayamanne.python-extension-pack` 等. 但不太适合DL编程, 不建议全部安装.
- testing <https://code.visualstudio.com/docs/python/testing>
- torch <https://code.visualstudio.com/docs/datascience/pytorch-support>

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

#### Python 基本配置

见官方的tutorial. 基本流程

- vscode 官方插件; 配置好 Python Interpreter
- 打开一个项目: Start VS Code in a project (workspace) folder
- **选择Python解释器** Select a Python interpreter
    - 可以通过 `Python: Select Interpreter` 命令, 直接右下角选择也行. 
- 如何运行 Run? 不像 cpp会有一些配置项, 这里就非常简单, 直接点右上角的三角即可, 一般没啥问题.
- Install and use packages 包管理习惯期间, 直接命令行 conda+pip 就很方便.

#### Python Debug 调试

可以看看下面的教程. 主要可以看配置项的说明, 见下.

- debugging <https://code.visualstudio.com/docs/python/debugging>

简要

- 通过 `.vscode/launch.json` 配置
    - 可进行多个配置, 左下角选择 (不同的通过 name 区分)
- 右下角选择 Python 解释器.
- 如何开始调试
    - 单个文件: 直接点右上角的按键即可. 
    - 需要个性化配置: 在 launch中设置, 然后左下角或者 F5开始. 

```json
        // 配置项说明见: https://code.visualstudio.com/docs/python/debugging#_set-configuration-options
        {
            // name: Provides the name for the debug configuration that appears in the VS Code dropdown list.
            "name": "Python: Current File",
            "type": "python",
            // 两种模式: 1) launch: 直接调试 program 中所定义的文件; 2) attach: 附加到一个已经运行的进程. 
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true, 
            // env: 设置环境变量. Sets optional environment variables for the debugger process beyond system environment variables, which the debugger always inherits. The values for these variables must be entered as strings.
            // "env": {
            //     "PYTHONPATH": "${workspaceFolder}/src"
            // }
            // cwd: 设置根目录 Specifies whether to enable subprocess debugging. Defaults to `false`, set to `true` to enable. For more information, see [multi-target debugging](https://code.visualstudio.com/docs/editor/debugging#_multitarget-debugging).
            // "cwd": "${workspaceFolder}"
            // python: 使用的Python解释器, 默认就是 workspace 的, 可以通过右下角选择不同的.
            // "python": "${command:python.interpreterPath}",
            // module 模块: Provides the ability to specify the name of a module to be debugged, similarly to the `-m` argument when run at the command line. For more information, see [Python.org](https://docs.python.org/3/using/cmdline.html#cmdoption-m)
            // "module": ""
        },
```


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


## 附录

### setting.json

见 <https://gist.github.com/Lightblues/7af038aef620ecebe64b96238324b546>

<script src="https://gist.github.com/Lightblues/7af038aef620ecebe64b96238324b546.js"></script>
