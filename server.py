import subprocess
import threading
import time
from flask import Flask
from flask_cloudflared import run_with_cloudflared
import os

# 定义运行C++程序的函数
def run_llama_program():
    subprocess.run([os.path.join(os.path.curdir(),"build","bin","llama-simple"),"-m","model.gguf"])

# 启动C++程序线程
llama_thread = threading.Thread(target=run_llama_program)
llama_thread.start()

# 定义 Flask 应用
app = Flask(__name__)

@app.route('/')
def home():
    return "Llama program is running!"

# 启动 flask_cloudflared 并打印 URL
def run_flask_cloudflared():
    run_with_cloudflared(app)

# 启动 flask_cloudflared 线程
cloudflared_thread = threading.Thread(target=run_flask_cloudflared)
cloudflared_thread.daemon = True
cloudflared_thread.start()

# 保持主线程运行
while True:
    time.sleep(1)