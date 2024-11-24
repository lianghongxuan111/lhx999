# Flask用户认证系统

## 一、简介
本项目是一个基于Flask的应用，展示了用户注册和登录功能。它使用Flask蓝图进行代码组织，并利用SQLAlchemy进行数据库交互。

## 二、前提条件
- 系统中已安装Python 3.x。
- 了解Flask、SQLAlchemy以及基本的Web开发概念。

## 三、安装步骤
1. **克隆仓库**
   - 使用以下命令将仓库克隆到本地机器：
2. **安装依赖项**
   - 进入项目目录。
   - 安装所需的Python包。如果使用虚拟环境，请先激活虚拟环境：

## 四、配置
- 应用使用`Config`类（来自`config.py`）来管理配置设置，如数据库连接字符串等。在运行应用之前，请确保根据您的环境正确配置了这些设置。

## 五、项目结构
1. **蓝图（Blueprints）**
   - `blueprints/blueprint1.py`：包含与主页相关的路由，例如`/`和`/error`。通过`home_bp`蓝图来组织这些路由。
   - `blueprints/blueprint2.py`：包含与用户注册和登录相关的路由，通过`user_bp`蓝图来组织。
2. **模型（Models）**
   - `models.py`：定义了`User`模型，包含`id`（主键）、`username`（唯一且不可为空）和`password`（不可为空）字段。这个模型与数据库中的`users`表相对应。
3. **应用启动文件（Main Application File）**
   - 在`main.py`（假设这是主应用文件，根据您的实际情况可能不同）中：
     - 创建了Flask应用实例`app`。
     - 从`Config`类加载配置。
     - 初始化数据库`db`并将其与应用关联。
     - 注册`home_bp`和`user_bp`蓝图。
     - 在应用上下文中创建数据库表（如果不存在）。

## 六、运行应用
1. **运行命令**
   - 如果一切正常，应用将在本地运行，您可以通过`http://localhost:5000/`访问主页，通过`http://localhost:5000/user`访问用户注册和登录页面。

## 七、功能演示
1. **注册功能**
   - 在`/user`页面，选择注册操作。
   - 输入用户名和密码，点击提交。如果用户名未被使用，将成功注册并显示注册成功消息。
2. **登录功能**
   - 在`/user`页面，选择登录操作。
   - 输入正确的用户名和密码，将成功登录并显示登录成功消息；如果用户名或密码错误，将显示错误提示，要求重新输入。
