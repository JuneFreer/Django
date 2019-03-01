# Django
Django Documentation Learning

step by step:
建立虚拟环境：python3 -m venv EnvironmentName
激活虚拟环境：source ll_env/bin/activate 
终止并退出虚拟环境：deactivate
安装django：pip install Django
新建一个django项目：django-admin.py startproject ProjectName . #末尾的句点使新项目拥有合适的目录结构，这样开发完成后可轻松的将应用程序部署到服务器
#名为manage.py的文件,是一个简单的程序,它接受命令 并将其交给Django的相关部分去运行,我们将使用这些命令来管理诸如使用数据库和运行服务器等任务
#Django将大部分与项目相关的信息都存储在数据库中,因此我们需要创建一个供Django使 用的数据库
给项目创建数据库：python manage.py migrate
#我们将修改数据库称为迁移数据库 migrate
Django启动一个服务器，让你能够查看系统中的项目，了解它们的工作情况: python manage.py runserver

