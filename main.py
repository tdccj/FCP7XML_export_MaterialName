# coding=utf-8

import os

path = r'Z:\临时文件\Timeline 1.xml'
export_path = r'Z:\临时文件\Timeline 1.txt'
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


def screening_of_repeat():
    global data_list_2
    for i in data_list:
        # 剔除合成片段
        format = os.path.splitext(i)[-1]
        format = format.strip() # 以去除空格
        if i.find('.') == -1:

            pass

        elif format in rule_out:
            print(1)
            # print(i)
            # # 排除重复
            print(i)
            pass

        else:
            # print(2)
            if i in data_list_2:
                pass
            elif i not in data_list_2:
                data_list_2.append(i)
            print(data_list_2)
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
    read_xml()
    print('data1', len(data_list))
    print(data_list_2)
    screening_of_repeat()
    print('data2', len(data_list_2))
    print(data_list_2)
    write_text()
    print('v0.1')
    print(f'0.1版本是简单匹配，输出列表中将不包含没有英文句号的内容（请不要在文件名中使用英文句号），同时也不包含{rule_out}等格式')
