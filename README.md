# NOAA data process
## Update
### 2020-11-29更新
将提取最大值更新为提取全部数据，获取数据抽象为一个独立函数，返回一个dict。使得这个程序可以作为后续新程序的一个基本模块来调用。
## 介绍
应友人请求尝试写的一个简易的爬虫脚本，用于爬取NOAA GOES X射线爆发记录并处理
## Requirements
- Python > 3.6
- requests
- time
- datetime
- pyecharts > v1.0
- sqlite3
- sqlalchemy = 1.3
## 说明
主要方法为requests.get方法获取接口的json数据。
主要问题：
- json数据更新不及时，在爆发期间会被设置为未定义，在对时间进行解析的时候会报错。
- json数据传输不完整，不明原因，会导致json数据字符串末尾缺失`]}`中的一个或者两个，从而json解析出错。
- 访问频率过高导致链接被丢弃
- 部分Windows操作系统在CMD中执行时会出现进程停止但是不退出也不执行的情况，没有找到合适的解决办法，目前解决办法是->用Linux跑这个脚本
## Feature
- 时间模块使用`datetime`替换`time`
- 时间改用datetime模块处理，而不是非常丑陋的使用+8 -> In Process
- 时间显示改用datetime模块内部标准时间格式输出
- 提供数据接口导出 ✓
- 对于获取的请求需要进一步优化而不是直接丢弃非法请求
- 可能需要添加图表绘制，即可视化
## Others
其中有注释掉一些Windows10中的API，据传在Windows中可以使用，但是由于我缺失实验环境，没有进行处理，同时由于代码曾经全部重构过，抛出Windows Alert部分的代码被移除了，只留下了被注释掉的部分API调用。
