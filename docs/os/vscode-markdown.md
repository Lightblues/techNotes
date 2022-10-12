
# VSCode Markdown 笔记方案

**说明**: 本篇介绍 VSCode 中的markdown编辑介绍, 主要用作个人笔记仓库, 但相关插件在日常, 比如 README 的编辑过程中也很好用. vscode 的介绍和使用推介参见 [[vscode]]. 


ref

- [doc](https://code.visualstudio.com/docs/languages/markdown)
- 参见 [在VSCode中高效编辑markdown的正确方式](https://www.thisfaner.com/p/edit-markdown-efficiently-in-vscode/). 本文部分参考了

## 基本介绍

vscode 原生支持的相关功能

- 自带预览功能
- 大纲视图：大纲视图是文件资源管理器底部的单独部分
- 为 markdown 提供 snippets
- 安全预览. 安全考虑默认仅用了一些功能. 可以通过 `Markdown: Change preview security settings` 修改
- 格式化: `"editor.defaultFormatter": "vscode.markdown-language-features"`


## 笔记管理碎碎念

个人笔记仓库搭建经验

- 基本思路: **纯文本 + Markdown语法 + 本地图片 + 版本管理**
- 为何选择纯文本? (而不交给某些软件/在线服务) 纯文本的好处包括
    - 检索功能; 软件兼容性
    - vscode 中编辑体验极佳
    - 速度响应更快
- 语法选择: Markdown语法
    - 语法简单, 学习成本低
    - 配合插件的快捷键生态.
    - **图片管理**: md 最困扰我的应该就是图片管理了, 尝试过图床但 免费+稳定性 不可兼得, 索性本地管理, 尽量减少图片的使用. 
        - 保存目录: 同级目录下的 `media/<fname>` 下
        - 文档移动: 在保证文件不重名的基础上, 自己写了一个Python脚本管理.
- 文件管理: **尽量集中在同一个 repo 中; 层级管理; 配合索引形成**
    - 整合在一个repo的好处: 
        - 目录清晰直观; 浏览体验
        - 配合vscode的搜索匹配功能, 检索
        - 链接: wiki语法 (见下 Foam)
    - 很热的「双向链接」? 配合 Foam 插件直接兼容. 但本质上, **双链的无序性还是抵不过层级管理的知识结构**.
    - 索引: 根据wiki语法构建一些手动索引页, 配合 Foam 的 wiki图+tag 功能.
- 折腾
    - 将笔记增量同步到博客, 见 [增量同步](#增量同步)

### 图片管理

图片保存: 目前用了 Paste Image `mushan.vscode-paste-image` 这个插件, 设置了快捷键 `Cmd+Shift+V` 保存到相应目录下.

```json
// settings.json
"pasteImage.path": "${currentFileDir}/media/${currentFileNameWithoutExt}",
```

图片移动: 本地管理的一个痛点是, 移动本地文件后, 图片的相对链接失效. 为此, 写了一个Python脚本, 见 [图片移动](#图片移动)

## Markdown 插件

基于一些好用的插件构建笔记体系.

插件列表

- Markdown All in One `yzhang.markdown-all-in-one` 提供了较多的md编辑辅助
    - 包括: keyboard shortcuts, table of contents, auto preview and more
- markdownlint `DavidAnson.vscode-markdownlint` 语法检查
    - Markdown linting and style checking for Visual Studio Code
- Foam `foam.foam-vscode` 新宠, 提供了tag, wiki语法, 笔记链接图等功能. 替换了之前的两个插件 
    - repo: <https://github.com/foambubble/foam>


一些被弃用的插件

- Markdown Preview Enhanced(MPE) 增强的预览功能, 但性能占用稍高, 发现原生的就不错.
    - 参见 [here](https://www.thisfaner.com/p/edit-markdown-efficiently-in-vscode/)
- Markdown Notes `kortina.vscode-markdown-notes` 提供了下面的一些语法, 被 foam 替换了
    - Use `[[wiki-links]]`, `backlinks`, `#tags` and `@bibtex-citations` for fast-navigation of markdown notes.
- markdown-hashtags `vanadium23.markdown-hashtags` tag列表, 同被 foam 替换
    - Hashtags for markdown: autocomplete, tree view and references.
- markdown-formatter `mervin.markdown-formatter` 格式化md文件, 被 markdownlint 取代.
    - [这里](https://github.com/sumnow/markdown-formatter/blob/HEAD/README_CN.md) 的配置项写得很清楚
- learn-markdown `docsmsft.docs-markdown` 微软的
    - 好像是 <http://learn.microsoft.com/> 的增强语法, 一些理念还不错. 参见 [here](https://www.thisfaner.com/p/edit-markdown-efficiently-in-vscode/)


### Markdown All in One

提供了一些好用的md编辑体验. 以下略看. 

- 增强的列表编辑功能
- 直接在选定文本上使用 `Ctrl+v` 来插入链接
- 增强的引用编辑功能
- 格式化表格
- 支持处理和预览 GFM

自动补全：在 `settings.json` 文件中添加

```json
  "[markdown]": {
  // 快速补全
  "editor.quickSuggestions": {
  "other": true,
  "comments": true,
  "strings": true
  },
  // 显示空格
  "editor.renderWhitespace": "all",
  // snippet 提示优先（看个人喜欢）
  "editor.snippetSuggestions": "top",
  "editor.tabCompletion": "on",
  // 使用enter 接受提示
  // "editor.acceptSuggestionOnEnter": "on",
  },
```

- 输入 `code` 就会弹出行内代码和代码块两种补全提示
- 输入 `ul` 或 `li` 就会弹出列表补全提示
- 类似的还有 `bold` 、`image`、`italic`、`link` 、`quote` 等。

提供了一些快捷方式

`Ctrl/Cmd + B` Toggle bold
`Ctrl/Cmd + I` Toggle italic
`Ctrl/Cmd + Shift + ]` Toggle heading (uplevel)
`Ctrl/Cmd + Shift + [` Toggle heading (downlevel)
`Ctrl/Cmd + M` Toggle math environment
`Alt + C` Check/Uncheck task list item
`cmd+]` 缩进. 是比行首Tab更规范一般的用法.

### makrdownlint

`markdownlint` Markdown 语法检查扩展工具. 配合默认的格式化工具.

- repo <https://github.com/DavidAnson/vscode-markdownlint>
- 配置项: [规则列表](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md). 一个 [中文说明](https://www.jianshu.com/p/51523a1c6fe1)
- Makrdown style <https://cirosantilli.com/markdown-style-guide/>

配置选项

```json
"markdownlint.config": {
        "default": true,
        "MD003": { "style": "atx_closed" },
        "MD007": { "indent": 4 },
        //禁用某条规则
        "MD013": false,
        //也可以使用某条规则的别名来配置
        "no-hard-tabs": false
    }
```

### Foam

- <https://foambubble.github.io/foam/>

相关的Command

```sh
Foam: Show Graph
Foam: Create New Note from Template
Foam: Open Daily Note
Foam: Open Random Note
```

实用功能

- wiki 语法 & 构成的图
    - 语法
        - 基本语法: `[[wiki]]`
        - 链接到文档的 section: `[[resource#Section Title]]`
        - Link Alias: `[[wikilink|alias]]`
    - Note embed: `![[note.md]]` (在预览中嵌入所引用的文档内容)
    - 可视化: Graph; 侧栏中的 Backlinks.
- Tag 标签功能
    - 语法: 
        - 长词: `#my-tag1`
        - 层级 `#parent/child`

#### 介绍的功能

wiki 链接相关的特性. 

- Graph Visualization: 在Command中输入 `Foam: Show Graph` 展现当前的笔记链接关系 ⭐️
- Link Autocompletion: 提供了wiki语法 `[[wiki]]`, 链接自动补全.
- Sync links on file rename: 文件重命名的时候, 自动更新wiki链接.
- Unique identifiers across directories
- Link Preview and Navigation
- Go to definition, Peek References
- Note embed: `![[note.md]]` 语法
- Support for sections: 也是 wiki 语法 standard wiki syntax of `[[resource#Section Title]]`.
- Link Alias: `[[wikilink|alias]]`

其他的一些功能

- Templates
    - 语法见 [doc](https://foambubble.github.io/foam/user/features/note-templates)
- Daily note
    - 见 [doc](https://foambubble.github.io/foam/user/features/daily-notes)

可视化

- Backlinks Panel
- Tag Explorer Panel
- Orphans and Placeholder Panels
- Syntax highlight

### Markdown Notes

Use `[[wiki-links]]`, `backlinks`, `#tags` and `@bibtex-citations` for fast-navigation of markdown notes.


### Markdown Preview Enhanced(MPE)

- `Markdown Preview Enhanced(MPE)` 插件
    - 扩展语法的支持，例如 `==` 高亮
    - 图片助手
    - 图片渲染
        - Mermaid

还可以自定义主题？选择 `none.css` 用原生的就很好！

## 附录


### 图片移动

移动md文件后移动引用的图片

见 <https://gist.github.com/Lightblues/76467909fb70d14a8f5135e91774c261>

<script src="https://gist.github.com/Lightblues/76467909fb70d14a8f5135e91774c261.js"></script>

### 增量同步

见 <https://gist.github.com/Lightblues/c80533ffc29f901eecfd859eeb72abde>

<script src="https://gist.github.com/Lightblues/c80533ffc29f901eecfd859eeb72abde.js"></script>

