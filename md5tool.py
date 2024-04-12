import hashlib
import tkinter as tk
from tkinter import filedialog, scrolledtext
from datetime import datetime


def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        md5_value = calculate_md5(file_path)
        timestamp = datetime.now().strftime("[%H:%M:%S] ")
        file_name = file_path.split("/")[-1]
        log_message = f"{'-' * 25}{'  '}{timestamp} {'-' * 25}\n文件：{file_name}\n文件MD5：{md5_value}\n文件路径：{file_path}\n{'-' * 64}\n\n"
        result_log.insert(tk.END, log_message)

        # 将文件路径显示在文本框中
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

        # 将文件的MD5值显示在文本框中
        md5_entry.delete(0, tk.END)
        md5_entry.insert(0, md5_value)


# 创建主窗口
root = tk.Tk()
root.title("文件MD5查看工具")

# 设置窗口大小并居中显示
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_x = int((screen_width - window_width) / 2)
position_y = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

# 创建一个容器框架用于横排显示文件相关内容
frame_file = tk.Frame(root)
frame_file.pack(pady=10)

# 添加标签和文本框到容器框架中，并靠左对齐
file_label = tk.Label(frame_file, text="文件：")
file_label.pack(side=tk.LEFT)
file_entry = tk.Entry(frame_file, width=50)
file_entry.pack(side=tk.LEFT)

browse_button = tk.Button(frame_file, text="浏览", command=browse_file)
browse_button.pack(side=tk.LEFT, padx=(5, 0))

# 创建一个容器框架用于横排显示MD5相关内容
frame_md5 = tk.Frame(root)
frame_md5.pack(pady=5)

# 添加MD5标签和文本框并横排显示
md5_label = tk.Label(frame_md5, text="MD5：")
md5_label.pack(side=tk.LEFT)
md5_entry = tk.Entry(frame_md5, width=50)
md5_entry.pack(side=tk.LEFT)

# 添加结果显示文本区域（日志形式）并放在最下方
result_log = scrolledtext.ScrolledText(root, width=60, height=15, font=("宋体", 12), spacing2=5)
result_log.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
result_log.pack(side=tk.BOTTOM)

root.mainloop()
