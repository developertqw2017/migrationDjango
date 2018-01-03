# migrationDjango

在每次数据迁移后  python dist-packages  包文件  django/contrib/auth/migrations  会更新一次依赖

![](https://img1.tuicool.com/2ayYzqQ.png!web)

如果删除工作目录下的迁移文件，该 migrations文件里面记录的依赖信息会 爆出错误。

