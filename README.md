<p align="center">
<img src="icon.png" width="100" >
</p>

## 连接到CPU

由于使用CPU访问外网时，每隔一段时间就需要验证（无线网与有线网均需要验证），故写了这个小工具运行在后台，每隔一段时间就检测能否访问外网，否则就尝试自动验证

> CPU 即 China Pharmaceutical University 的缩写，也代指其内网

#### 使用方式

下载<a href='https://github.com/wangtao2001/CPU/releases'>附件</a>，解压至任意位置，在`config.ini`中填写账号密码以及超时重连时间，双击`连接到CPU.exe`运行即可

#### 设置开机自启动

`Win + R`执行`shell:common startup`，将`连接到CPU.exe`的快捷方式放入其中即可

#### 规划

- 错误连接提示
- 内网穿透
- 适配更多平台
