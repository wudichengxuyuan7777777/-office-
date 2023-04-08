from flask import Flask  # 导包

app = Flask(__name__)  # 创建app，__name__表示指向程序所在的包


@app.route("/")  # 路由视图函数
def index():
    return "hello world"


if __name__ == '__main__':
    app.run()  # 运行app

