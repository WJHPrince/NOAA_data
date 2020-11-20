# NOAA data process

## 介绍
应友人请求尝试写的一个简易的爬虫脚本，用于爬取NOAA GOES X射线爆发记录并处理
## Requirements
- Python > 3.6
- requests
- time
## 说明
主要方法为requests.get方法获取接口的json数据。
主要问题：
- json数据更新不及时，在爆发期间会被设置为未定义，在对时间进行解析的时候会报错。
- json数据传输不完整，不明原因，会导致json数据字符串末尾缺失`]}`中的一个或者两个，从而json解析出错。
- 访问频率过高导致链接被丢弃
## Feature
- 时间模块使用`datetime`替换`time`
- 时间改用datetime模块处理，而不是非常丑陋的使用+8
- 时间显示改用datetime模块内部标准时间格式输出
- 提供数据接口导出
