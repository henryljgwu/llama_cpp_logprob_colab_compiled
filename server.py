import subprocess
import threading
import time
from flask import Flask
from flask_cloudflared import _run_cloudflared

# 定义运行C++程序的函数
def run_llama_program():
    subprocess.run(["./llama-simple"])

# 启动C++程序线程
llama_thread = threading.Thread(target=run_llama_program)
llama_thread.start()

# 定义Flask应用
app = Flask(__name__)

@app.route('/')
def home():
    return "Llama program is running!"

# 启动flask_cloudflared进行端口转发并打印URL
def run_flask_cloudflared():
    public_url = _run_cloudflared(port=8080)
    print(f"Public URL: {public_url}")

# 启动flask_cloudflared线程
cloudflared_thread = threading.Thread(target=run_flask_cloudflared)
cloudflared_thread.start()

# 启动Flask应用
app.run(port=8080)