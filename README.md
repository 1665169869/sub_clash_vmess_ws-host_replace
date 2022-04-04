# CLASH订阅把vmess节点ws混淆改其他host

如标题 效果自测

python >= 3.10

flask框架，可自行搭配nginx

运行教程如下：

```
pip install -r requirements.txt
python main.py
```

*GET方法*

> http://127.0.0.1:4561/api/sub

|参数|可空|备注|
|---|---|---|
|sub_url|false|你的订阅地址|
|host|false|需要改的host混淆|

