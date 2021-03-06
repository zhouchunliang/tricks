#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipreacher'


import os
import zhihuapi as api
import urllib.request


# 配置 cookie
def set_cookie():
    if os.path.isfile('cookie'):
        print('cookie 已存在')
    else:
        print('由于 Terminal 本身对输入内容长度的限制')
        cookie_content1 = input('请先输入 cookie 的前一半\n>  ')
        cookie_content2 = input('请继续输入 cookie 的后一半\n>  ')
        cookie_content = cookie_content1 + cookie_content2
        with open('cookie', 'w') as f: 
            f.write(cookie_content)
        print('cookie 已保存')

    with open('cookie') as f:
        api.cookie(f.read())
    print('cookie 已配置完成')


r1 = []
r2 = []
r3 = []


# 拉取 followee 名单，page 根据名单页数确定
def followees(me, page):
    print('正在获取 followee 名单...')
    for i in range(page):    
        data = api.user(me).followees(offset=(20 * i))
        for j in range(len(data)):
            r1.append(data[j]['name'])    # 关注者的昵称
            r2.append(data[j]['url_token'])    # 关注者的个性域名
            r3.append(data[j]['avatar_url_template'][: 11] + '3'+ data[j]['avatar_url_template'][12: - 10] + 'xll.jpg')    # 关注者头像的地址


# 创建文件夹
def folder():
    if os.path.exists('zhihu_img'):
        print('文件夹已存在')
    else:
        os.mkdir('zhihu_img')
        print('文件夹已建立')


# 获取 followee 头像并保存到本地
def save():
    for i in range(len(r3)):
        try:
            print('正在保存_' + str(r1[i]) + '_的头像到本地...')
            filename = str(i) + '_' + str(r1[i]) + '.jpg'
            url = r3[i]
            web = urllib.request.urlopen(url)
            data = web.read()
            with open('zhihu_img/' + filename, 'wb') as f:
                f.write(data)
        except urllib.error.HTTPError:
            pass


if __name__ == '__main__':
    set_cookie()
    me = input('请输入个性域名 \n>  ')
    page = int(input('请输入 followee 页数 \n>  '))
    folder()
    followees(me, page)
    save()





            