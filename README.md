# osu-cn-mirror
osu.mengsky.net 是一个osu!面普的中国镜像，部署在京东CDN，正在迁移至七牛CDN。

### spider
包含了一个简单的镜像的爬虫work，一起七牛API接口的文件上传模块，数据库相关模块

### web
包含了一个flask以及简单的orm框架实现的web服务器，提供beatmap的检索以及下载。

#### qiniu
七牛API文件上传实现，因为官方SDK依赖第三方组建requests实行规范文件名标准必须为ascii无法满足需求。

# License
GPLv3
