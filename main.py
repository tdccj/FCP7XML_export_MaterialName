# coding=utf-8

import os
import time

path = input('输入FCP7XML文件（.xml)路径（包含文件名及格式')
export_path = os.path.split(path)[0]+'\\'+os.path.splitext(os.path.split(path)[1])[0]+'.txt'
print(export_path)
data_list = []
data_list_2 = []
rule_out = ['.m4a', '.png', '.jpg']


def read_xml():
    global data_list
    with open(path, 'r', encoding='utf-8') as xml:
        data = xml.read()
        start = data.find('<file id="')
        num = 0
        while start != -1:
            start = data.find('<file id="', start + 1)
            end = data.find('>', start + 1)
            # 此处有bug，但触发概率不大
            if start == -1:
                break
            else:
                # print(data[start + 10:end - 3])
                data_list.append(data[start + 10:end - 3])
                num = num + 1
                # print(num, start, end)

    return data_list


# 用以筛选重复和不需要的文件名
def screening_of_repeat():
    global data_list_2
    for i in data_list:
        # 剔除合成片段
        i = i.strip()   # 删除空格！！！
        format_i = os.path.splitext(i)[-1]  #提取后缀
        if i.find('.') == -1:   # 剔除合成
            pass

        elif format_i in rule_out:  # 剔除特定格式
            pass

        else:
            # 剔除重复的
            if i in data_list_2:
                pass
            elif i not in data_list_2:
                data_list_2.append(i)
                # print(data_list_2)
    # print(data_list_2)


def write_text():
    with open(export_path, 'w', encoding='utf-8') as text:
        # print(3,len(data_list_2))
        for i in data_list_2:
            text.write(i)
            text.write('\n')


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print('当前版本v0.1.5')
    print(f'0.1版本是简单匹配，输出列表中将不包含没有英文句号的内容（请不要在文件名中使用英文句号），同时也不包含{rule_out}等格式')
    print('请不要在素材文件名中使用‘.’和‘<’‘>’，要不然会得到意外的结果')
    print('如果配音不是m4a格式，需要在导出后手动删除(换句话说如果有素材是m4a格式，需要手动添加，或等待版本更新白名单机制')
    read_xml()
    print('data1', len(data_list))
    screening_of_repeat()
    print('data2', len(data_list_2))
    print(data_list_2)
    write_text()
    print('导出完成，五秒后自动退出')
    time.sleep(5)
