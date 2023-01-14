# 导入库Import Library
import time
import os
import requests
import random

path = os.getcwd() # 获得当前工作目录Get the current working directory

# ------------------------------下载程序部分开始--------------------------------
#                          Download program part starts
# 1.8.8进度条模块1.8.8 Progress bar module
def progressbar_1_8_8(url):
    try:
        os.mkdir('1_8_8')
    except:
        print('已有目录，直接安装\n')
    start = time.time() #下载开始时间Download start time
    response = requests.get(url, stream=True)
    size = 0    #初始化已下载大小Initialize downloaded size
    chunk_size = 1024  # 每次下载的数据大小Data size per download
    content_size = int(response.headers['content-length'])  # 下载文件总大小Total size of downloaded files
    try:
        if response.status_code == 200:   #判断是否响应成功Judge whether the response is successful
            print('\n开始下载！[文件大小]:{size:.2f} MB'.format(size = content_size / chunk_size /1024))   #开始下载，显示下载文件大小
            with open(path + "\\1_8_8\\spigot.jar",'wb') as file:   #显示进度条Show progress bar
                for data in response.iter_content(chunk_size = chunk_size):
                    file.write(data)
                    size +=len(data)
                    print('\r'+'[下载进度]:%s%.2f%%' % ('>'*int(size*50/ content_size), float(size / content_size * 100)) ,end=' ')
        end = time.time()   #下载结束时间Download end time
        print('下载完成!,用时: %.2f秒' % (end - start))  #输出下载用时时间Output download time
    except:
        print('错误!')
    print('下载成功!')

def main_1_8_8():
    # 下载1.8.8服务端核心文件Download 1.8.8 server core file
    url = 'https://cdn.getbukkit.org/spigot/spigot-1.8.8-R0.1-SNAPSHOT-latest.jar'
    progressbar_1_8_8(url)

################################################################################

# 1.12.2进度条模块
def progressbar_1_12_2(url):
    try:
        os.mkdir('1_12_2')
    except:
        print('已有目录，直接安装\n')
    start = time.time() #下载开始时间
    response = requests.get(url, stream=True)
    size = 0    #初始化已下载大小
    chunk_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['content-length'])  # 下载文件总大小
    os.mkdir
    try:
        if response.status_code == 200:   #判断是否响应成功
            print('\n开始下载！[文件大小]:{size:.2f} MB'.format(size = content_size / chunk_size /1024))   #开始下载，显示下载文件大小
            with open(path + "\\1_12_2\\spigot.jar",'wb') as file:   #显示进度条
                for data in response.iter_content(chunk_size = chunk_size):
                    file.write(data)
                    size +=len(data)
                    print('\r'+'[下载进度]:%s%.2f%%' % ('>'*int(size*50/ content_size), float(size / content_size * 100)) ,end=' ')
        end = time.time()   #下载结束时间
        print('下载完成!,用时: %.2f秒' % (end - start))  #输出下载用时时间
    except:
        print('错误!')
    print('下载成功!')

def main_1_12_2():
    # 下载1.12.2服务端核心文件
    url = 'https://cdn.getbukkit.org/spigot/spigot-1.12.2.jar'
    progressbar_1_12_2(url)

################################################################################

# 1.16.5进度条模块
def progressbar_1_16_5(url):
    try:
        os.mkdir('1_16_5')
    except:
        print('已有目录，直接安装\n')
    start = time.time() #下载开始时间
    response = requests.get(url, stream=True)
    size = 0    #初始化已下载大小
    chunk_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['content-length'])  # 下载文件总大小
    try:
        if response.status_code == 200:   #判断是否响应成功
            print('\n开始下载！[文件大小]:{size:.2f} MB'.format(size = content_size / chunk_size /1024))   #开始下载，显示下载文件大小
            with open(path + "\\1_16_5\\spigot.jar",'wb') as file:   #显示进度条
                for data in response.iter_content(chunk_size = chunk_size):
                    file.write(data)
                    size +=len(data)
                    print('\r'+'[下载进度]:%s%.2f%%' % ('>'*int(size*50/ content_size), float(size / content_size * 100)) ,end=' ')
        end = time.time()   #下载结束时间
        print('下载完成!,用时: %.2f秒' % (end - start))  #输出下载用时时间
    except:
        print('错误!')
    print('下载成功!')

def main_1_16_5():
    # 下载1.16.5服务端核心文件
    url = 'https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar'
    progressbar_1_16_5(url)

################################################################################

# 1.19.3进度条模块
def progressbar_1_19_3(url):
    try:
        os.mkdir('1_19_3')
    except:
        print('已有目录，直接安装\n')
    start = time.time() #下载开始时间
    response = requests.get(url, stream=True)
    size = 0    #初始化已下载大小
    chunk_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['content-length'])  # 下载文件总大小
    try:
        if response.status_code == 200:   #判断是否响应成功
            print('\n开始下载！[文件大小]:{size:.2f} MB'.format(size = content_size / chunk_size /1024))   #开始下载，显示下载文件大小
            with open(path + "\\1_19_3\\spigot.jar",'wb') as file:   #显示进度条
                for data in response.iter_content(chunk_size = chunk_size):
                    file.write(data)
                    size +=len(data)
                    print('\r'+'[下载进度]:%s%.2f%%' % ('>'*int(size*50/ content_size), float(size / content_size * 100)) ,end=' ')
        end = time.time()   #下载结束时间
        print('下载完成!,用时: %.2f秒' % (end - start))  #输出下载用时时间
    except:
        print('错误!')
    print('下载成功!')

def main_1_19_3():
    # 下载1.19.3服务端核心文件
    url = 'https://download.getbukkit.org/spigot/spigot-1.19.3.jar'
    progressbar_1_19_3(url)


# ------------------------------下载程序部分结束--------------------------------
#                           End of download program
# 启动器主程序
print('天启启动器1.0，一款暂时无UI的MC启动器(windows系统)，一款可以开服务器的启动器!')
print("")
time.sleep(random.randint(2,3))
print('启动中')
time.sleep(random.randint(1,2))
print('启动完毕\n')
time.sleep(random.randint(1,2))
print('[ 公 告 ] 作者:TNTXZ,QQ:35266332')
print("")
print('[ 重 要 公 告 ] 以后不需要打开此启动器重新下载和打开，否则会出错(作者懒得编检测代码)\n启动器会自动生成开服脚本在文件夹里(如1.8.8服务器在1_8_8文件夹里，里面有"开服务器.bat"双击启动)')
time.sleep(5)
print("")
print('[ 提 示 ] 1.8.8、1.12.2建议用JDK8，1.16.5建议JDK11，1.19.3建议JDK17！')
print("")
xms = input('请选择服务器最小内存(单位：mb)只需要输入一个数字即可！\n')
print("")
xmx = input('请选择服务器最大内存(单位：mb)只需要输入一个数字即可！\n')
print("")
javapath = input('请输入您的java路径不用包含java.exe,要到bin文件夹为止( 比如 C:\Program Files (x86)\Java\jdk1.8\ bin )\n')

while True:
        option = input('\n请选择下载启动版本,目前支持1.8.8,1.12.2,1.16.5,1.19.3版本(1.8.8/1.12.2/1.16.5/1.19.3)\n')
        if option == '1.8.8':
            print('这就为您安装1.8.8服务器')
            time.sleep(1)
            main_1_8_8() # 安装1.8.8服务器
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

        if option == '1.12.2':
            print('这就为您安装1.12.2服务器')
            time.sleep(1)
            main_1_12_2() # 安装1.12.2服务器
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

        if option == '1.16.5':
            print('这就为您安装1.16.5服务器')
            time.sleep(1)
            main_1_16_5() # 安装1.16.5服务器
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

        if option == '1.19.3':
            print('这就为您安装1.19.3服务器')
            time.sleep(1)
            main_1_19_3() # 安装1.19.3服务器
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
