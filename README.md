# py-bilibili-app-video
> python版本：3.x

### run.py

APP下载后的视频，根据章节自动整理

- 抓取网页信息
- 修改文件信息
- 删除多余文件（夹）

![demo](./demo.gif)

### join.py

通过 moviepy 将APP下载完的分段视频进行合并（不推荐，很耗CPU，速度慢，但是转换后文件会很小很多）

### m4s.py

m4s 音视频分开的格式文件进行重命名，配合格式工厂进行混流，速度很快

### rename.py

将第三方软件下载的文件进行自动分组、重命名

代码仅供学习，请无作他图