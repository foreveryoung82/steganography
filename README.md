# steganography
将信息隐写入普通中文文本之中, 并且不增加文本长度, 同时几乎不改变文本含义

安装:
1. 安装python 3.7, 并关联.py文件(默认安装应该就会关键.py文件)
2. 下载或clone本项目到本地硬盘(假定下载目录为`C:\steganography`).打开项目目录, 你会看到大约类似下面的文件布局
    + steganography
        + 明文.txt
        + 密文.txt
        + 隐写.bat
        + 反隐.bat
        + ...(其它文件)

测试:
1. 运行`隐写.bat`. 正常情况下, 你会看到控制台窗口提示你把加密的信息写入了`密文.txt`
2. 运行`反隐.bat`. 正常情况下, 你会看到控制台窗口提示你把解密的信息写入了`明文.txt`
3. 打开`明文.txt`, 正常情况下, 你应该能看到里面有一个百度贴吧首页的链接地址:
<https://tieba.baidu.com/index.html>
4. 如果到这一步一切正常, 那么说明安装成功.

运行:
1. 隐写
    + 把你要隐写的文本(比如b站首页地址:`https://www.bilibili.com/`)写入`明文.txt`之中, 并保存.
    + 运行`隐写.bat`
    + 打开`密文.txt`, 里面就是生成的加密文本. 注意, 每次生成都会从三国演义中摘取随机段落. 所以即便明文一摸一样, 但是每次运行都会有不同的加密文本生成.
    + 把`密文.txt`里所有内容复制(按ctrl+A, ctrl+C)出来, 分享给其他人即可.
2. 反隐
    + 把你接收到的加密文本粘贴到`密文.txt`文件里, 并保存.(覆盖所有之前的内容)
    + 运行`反隐.bat`
    + 打开`明文.txt`, 里面就是反隐出来的隐藏信息.

原理和特点:
1. 基于简单的简体/繁体字文本变换来编码隐藏信息
2. 解密方理论上不需要密码本
3. 对于普通人来说, 用古文/武侠/玄幻小说做掩码, 隐写后的文本隐蔽性很强, 难于察觉到有隐藏信息.
4. 但是这个加密算法本身及其脆弱, ***不要用它来做任何重要数据的加密!!!***
它无法承受任何基于现代密码学的攻击! 它主要用于娱乐和绕过某些社交媒体过于严格的敏感字审查.