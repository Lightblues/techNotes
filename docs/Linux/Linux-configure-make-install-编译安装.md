
一般编译安装软件涉及到的命令

```sh
./configure  # 通过 --prefix 指定安装目录
make
make install # 复制相关文件到需要安装的目录
```

- 参见 [configure、 make、 make install 背后的原理(翻译)](https://zhuanlan.zhihu.com/p/77813702)

## 示例: 安装 gcc 到用户目录

- from <https://gcc.gnu.org/wiki/InstallingGCC>
- 下载: <https://github.com/gcc-mirror/gcc>

假设没有 sudo, 下例安装 gcc 到用户目录下

```sh
tar xzf gcc-4.6.2.tar.gz
cd gcc-4.6.2
./contrib/download_prerequisites
cd ..
mkdir objdir    # 编译目标目录
cd objdir
$PWD/../gcc-4.6.2/configure --prefix=$HOME/GCC-4.6.2 --enable-languages=c,c++,fortran,go
make -j 16      # If your computer has multiple processors or cores you can speed it up by building in parallel using make -j 2 (or a higher number for more parallelism).
make install    # 将可执行文件、第三方依赖包和文档复制到正确的路径

cd $HOME/GCC-4.6.2
bin/gcc --version   # 注意是在安装目录的相对路径下
```

## 相关命令说明

1. 配置

`configure` 脚本负责在你使用的系统上准备好软件的构建环境。确保接下来的构建和安装过程所需要的依赖准备好，并且搞清楚使用这些依赖需要的东西。

Unix 程序一般是用 C 语言写的，所以我们通常需要一个 C 编译器去构建它们。在这个例子中 `configure` 要做的就是确保系统中有 C 编译器，并确定它的名字和路径。

2. 构建

当 `configure` 配置完毕后，可以使用 `make` 命令执行构建。这个过程会执行在 `Makefile` 文件中定义的一系列任务将软件源代码编译成可执行文件。

你下载的源码包一般没有一个最终的 `Makefile` 文件，一般是一个模版文件 `Makefile.in` 文件，然后 `configure` 根据系统的参数生成一个定制化的 `Makefile` 文件。

3. 安装

现在软件已经被构建好并且可以执行，接下来要做的就是将可执行文件复制到最终的路径。`make install` 命令就是将可执行文件、第三方依赖包和文档复制到正确的路径。

这通常意味着，可执行文件被复制到某个 `PATH` 包含的路径，程序的调用文档被复制到某个 `MANPATH` 包含的路径，还有程序依赖的文件也会被存放在合适的路径。

因为安装这一步也是被定义在 `Makefile` 中，所以程序安装的路径可以通过 `configure` 命令的参数指定，或者 `configure` 通过系统参数决定。

如果要将可执行文件安装在系统路径，执行这步需要赋予相应的权限，一般是通过 sudo。

## 使用 autotools 打包发布 (autoconfig, automake)

- `configure` 脚本根据系统信息将 `Makefile.in` 模版文件转换为 `Makefile`文件
    - 然而, `configure` 和 `Makefile.in` 这两个文件很冗长, 一般是自动生成的
- 是通过一个叫做 `autotools` 的工具集打包的。这个工具集包含 `autoconf` 、`automake` 等工具
    - 通过创建一个描述文件 `configure.ac` 来描述 configure 需要做的事情。`configure.ac` 使用 m4sh 写，m4sh 是 `m4` 宏命令和 shell 脚本的组合。
    - 可以先写一个 `Makefile.am` 脚本，然后通过 `automake` 工具生成 `Makefile.in` 脚本

`.ac` autoconfig 配置 (相关说明见原文)

```sh
# configure.ac
AC_INIT([helloworld], [0.1], [george@thoughtbot.com])
AM_INIT_AUTOMAKE
AC_PROG_CC
AC_CONFIG_FILES([Makefile])
AC_OUTPUT
```

`.am` automake 配置

```sh
# Makefile.am
AUTOMAKE_OPTIONS = foreign
bin_PROGRAMS = helloworld
helloworld_SOURCES = main.c
```

然后

```sh
# 为 autotools 准备 m4 脚本环境
aclocal
# 使用 `autoconf` 将 `configure.ac` 生成 `configure` 脚本，用 `automake` 将 `Makefile.am` 生成为 `Makefile.in` 脚本
autoconf
automake --add-missing

make distcheck # 使用 Makefile 构建一个发布软件并测试
```

安装

```sh
./configure # 生成 Makefile 脚本
# 构建软件
make
# make dist # 生成 distribution (.tar.gz)
make install # 使用 Makefile 安装软件
```


