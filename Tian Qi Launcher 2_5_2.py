
# 导入库Import Library
from queue import Queue
import time
import os
import requests
import random
import threading
import shutil
import os

path = os.getcwd() # 获得当前工作目录Get the current working directory

# ------------------------------下载程序部分开始--------------------------------
#                          Download program part starts

class DownloadThread(threading.Thread):
    def __init__(self, bytes_queue: Queue, url):
        super().__init__(daemon=True)
        self.bytes_queue = bytes_queue
        self.url = url

    def run(self):
        while not self.bytes_queue.empty():
            bytes_range = self.bytes_queue.get()
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84",
                "Range": "bytes={}".format(bytes_range[1])
            }
            response = requests.get(self.url, headers=headers)
            with open("temp/{}.tmp".format(bytes_range[0]), "wb") as f:
                f.write(response.content)

def get_file_size(url) -> int:
    response = requests.head(url)
    file_length = int(response.headers['Content-Length'])

    return file_length

def get_thread_download(file_length) -> list:
    bytes = Queue(20)

    start_bytes = -1
    for i in range(20):
        bytes_size = int(file_length/20)*i
        
        if i == 20-1: bytes_size = file_length
        bytes_length = "{}-{}".format(start_bytes+1, bytes_size)
        
        bytes.put([i, bytes_length])
        start_bytes = bytes_size

    return bytes

def create_threading(bytes_queue,url):
    thread_list = []
    for i in range(5):
        thread = DownloadThread(bytes_queue, url)
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()

def composite_file():
    if os.path.isfile("spigot.jar"): os.remove("spigot.jar")
    with open("spigot.jar", "ab") as f:
        for i in range(20):
            with open("temp/{}.tmp".format(i), "rb") as bytes_f:
                f.write(bytes_f.read())

def main(url):
    file_length = get_file_size(url)
    copies_queue = get_thread_download(file_length)
    create_threading(copies_queue,url)
    composite_file()
    
def download(url,version):
    try:
        os.mkdir('temp')
        os.mkdir(version)
    except:
        time.sleep(1)

    if __name__ == '__main__':
        main(url)

    shutil.rmtree('temp')
    shutil.move('spigot.jar',version + '/spigot.jar')

# ------------------------------下载程序部分结束--------------------------------
#                           End of download program
#__________
#封装清屏代码(Windows)
def clear():
    os.system(r"cls")
#__________
# 打印彩色字符
def colorprint(msg: str, color: str = "", timestamp: bool = True):
    str = ""
    if timestamp:
        str += time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  "
    if color == "red":
        str += "\033[1;31;40m"
    elif color == "green":
        str += "\033[1;32;40m"
    elif color == "yellow":
        str += "\033[1;33;40m"
    elif color == "black":
        str += "\033[1;30;40m"
    elif color == "blue":
        str += "\033[1;34;40m"
    elif color == "purple":
        str += "\033[1;35;40m"
    elif color == "beige":
        str += "\033[1;36;40"
    elif color == "white":
        str += "\033[1;37;40" 
    else:
        print(str + msg)
        return
    str += msg + "\033[0m"
    print(str)
#__________
def threedotwhile():
    os.system(r"cls")
    print("\033[0;37;40m启动中.\033[0m")
    time.sleep(0.25)
    os.system(r"cls")
    print("\033[0;37;40m启动中..\033[0m")
    time.sleep(0.25)
    os.system(r"cls")
    print("\033[0;37;40m启动中...\033[0m")
    time.sleep(0.25)

#------------------------------------------------------------------------------
# 启动器主程序
clear()#清除程序开始部分的内容
colorprint('天启启动器2.5，一款暂无UI的Minecraft启动器(Windows系统)，一款可以开服务器的启动器!',"blue")
print("")
time.sleep(random.randint(3,5))
# print('启动中...')
for i in range(random.randint(2,5)):
    threedotwhile()
colorprint('\n启动完毕！\n',"green")
time.sleep(random.randint(1,2))
print('\033[0;33;40m[关于作者]\033[0m \033[0;36;40m作者\033[0m : \033[0;34;40mTNTXZ\033[0m ,\033[0;33;40mQQ: 35266332\033[0m , \033[0;36;40m联合作者\033[0m ： \033[0;32;40mLion_Deer\033[0m , \033[0;33;40mQQ: 2964774820\033[0m !')
print("")
print('\033[1;31;40m [ 重 要 提 醒 ] \033[0m \033[0;31;40m以后不需要打开此启动器重新下载和打开，否则会出错(作者们懒得编检测代码)\n启动器会自动生成开服脚本在文件夹里(如1.8.8服务器在1_8_8文件夹里，里面有"开服务器.bat"双击启动)\033[0m')
time.sleep(5)
print("")
print('\033[4;37;40m[小建议] 1.8.8、1.12.2建议用JDK8，1.16.5建议JDK11，1.19.3建议JDK17 ~\033[0m')
print("")
xms = input('请选择服务器最小内存(单位：mb)只需要输入一个数字即可！\n')
print("")
xmx = input('请选择服务器最大内存(单位：mb)只需要输入一个数字即可！\n')
print("")
javapath = input('请输入您的java路径不用包含java.exe,要到bin文件夹为止( 如 C:\Program Files (x86)\Java\jdk1.8\ bin )\n')

wrongnum = 0
while True:
        option = input('\n请选择下载启动版本,目前支持 1.8.8 , 1.12.2 , 1.16.5 , 1.19.3 版本(1.8.8/1.12.2/1.16.5/1.19.3)\n')
        if option == '1.8.8':
            print('这就为您安装1.8.8服务器')
            time.sleep(1)
            download('https://cdn.getbukkit.org/spigot/spigot-1.8.8-R0.1-SNAPSHOT-latest.jar','1_8_8') # 安装1.8.8服务器
            print('下载完成！请自行用生成的脚本启动！')
            time.sleep(1)
            with open(path + "\\1_8_8\\开服务器.bat",'w') as file:
                file.write("@ECHO OFF\n")
                file.write("title [1.8.8]\n")
                file.write('"' + javapath + '\java.exe" -Xms' + xms + "m -Xmx" + xmx + "m -jar spigot.jar\n")
                file.write("pause")
            print('生成脚本成功！祝您愉快！拜拜')
            time.sleep(3)
            break

        elif option == '1.12.2':
            print('这就为您安装1.12.2服务器')
            time.sleep(1)
            download('https://cdn.getbukkit.org/spigot/spigot-1.12.2.jar','1_12_2') # 安装1.12.2服务器
            print('下载完成！请自行用生成的脚本启动！')
            time.sleep(1)
            with open(path + "\\1_12_2\\开服务器.bat",'w') as file:
                file.write("@ECHO OFF\n")
                file.write("title [1.12.2]\n")
                file.write('"' + javapath + '\java.exe" -Xms' + xms + "m -Xmx" + xmx + "m -jar spigot.jar\n")
                file.write("pause")
            print('生成脚本成功！祝您愉快！拜拜')
            time.sleep(3)
            break

        elif option == '1.16.5':
            print('这就为您安装1.16.5服务器')
            time.sleep(1)
            download('https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar','1_16_5') # 安装1.16.5服务器
            print('下载完成！请自行用生成的脚本启动！')
            time.sleep(1)
            with open(path + "\\1_16_5\\开服务器.bat",'w') as file:
                file.write("@ECHO OFF\n")
                file.write("title [1.16.5]\n")
                file.write('"' + javapath + '\java.exe" -Xms' + xms + "m -Xmx" + xmx + "m -jar spigot.jar\n")
                file.write("pause")
            print('生成脚本成功！祝您愉快！拜拜')
            time.sleep(3)
            break

        elif option == '1.19.3':
            print('这就为您安装1.19.3服务器')
            time.sleep(1)
            download('https://download.getbukkit.org/spigot/spigot-1.19.3.jar','1_19_3') # 安装1.19.3服务器
            print('下载完成！请自行用生成的脚本启动！')
            time.sleep(1)
            with open(path + "\\1_19_3\\开服务器.bat",'w') as file:
                file.write("@ECHO OFF\n")
                file.write("title [1.19.3]\n")
                file.write('"' + javapath + '\java.exe" -Xms' + xms + "m -Xmx" + xmx + "m -jar spigot.jar\n")
                file.write("pause")
            print('生成脚本成功！祝您愉快！拜拜')
            time.sleep(3)
            break
        else:     #如果输入不正确：
            wrongnum = wrongnum + 1
            if wrongnum < 10:
                print("无法识别的版本，请重新输入！\n(Tips:格式为 1.xx.x ,如： 1.19.3 )")
                time.sleep(0.25)
            elif wrongnum == 10:
                print("\033[3;36;40m已经输错十次啦！还有最后\033[1;31;40m1次输入机会！\033[0m\033[0m")
                time.sleep(2)
            elif wrongnum > 10:
                print("错误次数太多，自动退出程序！")
                time.sleep(2)
                break
