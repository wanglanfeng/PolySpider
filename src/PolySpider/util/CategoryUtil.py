#!/usr/bin/env python
# -*- coding: utf-8 -*-  

'''
使用方法：
    由于不同的应用商店对应的分类不同，抓取到的应用进行分类整理也不能完全按照分类名来新建分类
    为了统一分类，采取91助手的分类作为默认分类方式，并为每一个分类定义一个ID
    建立一个字典，key为应用市场中抓取的分类名，value为对应的分类ID
    当所有市场中的分类名称都已经在字典中定义以后，就可以直接通过抓取分类名来将应用对应到我们的分类列表中来。
'''
'''
应用名称    ID(后两位为00，预留，如果有子分类的话，可以利用，比如游戏有自分类的话可以是4601，4602这样)
new category  根据GooglePlay分类规则进行分类
个性化          1000
交通运输        1100
体育            1200
健康与健身      1300
动态壁纸        1400
动漫            1500
医药            1600
商务            1700
图书与工具书    1800
天气            1900
娱乐            2000
媒体与视频      2100
小部件          2200
工具            2300
摄影            2400
效率            2500
教育            2600
新闻杂志        2700
旅游与本地出行  2800
生活时尚        2900
社交            3000
财务            3100
购物            3200
软件与演示      3300    
通讯            3400
音乐与音频      3500
游戏            3600
其他            3700
'''

##比如将其分类设置为需要额外一些工作来进行确认的分类
#比如一个应用如果是办公分类，首先查看其是否已经gab到数据库中，如果数据库中对这个应用已经有记录，那么直接那个记录我在想，如果有些分类比较笼统话，是否可以做出一定的策略，而不是将该分类之间确定为某一个我们的分类
#比如App_star中的办公分类，实际上是一个笼统概念，无法直接与我们的分类进行对应
#比如将其分类设置为需要额外一些工作来进行确认的分类
#比如一个应用如果是办公分类，首先查看其是否已经gab到数据库中，如果数据库中对这个应用已经有记录，那么直接那个记录来分类
#如果没有记录，则指定某个默认分类来记录，等待别的应用商店上传该应用，来分类，或者该应用进行人工分类的操作等等
CATEGORY_ID = {
    ## Common
    '未分类'    :  '0',
    '其他'      :   '1000',
    ## App_star分类字典 By Eric Wang
    '阅读资讯'  :   '2700',
    '电子书'    :   '1800',
    '输入法'    :   '2300',
    '休闲益智'  :   '3600',
    '动作竞技'  :   '3600',
    '体育竞速'  :   '3600',
    '健康美食'  :   '1300',
    '系统工具'  :   '2300',
    '主题桌面'  :   '1000',
    '音乐视频'  :   '3500,2100',
    '社交'      :   '3000',
    '办公'      :   '2500',
    '交通地图'  :   '1100',
    ## 应用宝
    ## 小米商城
    '影音视听':'3500,2100',
    '图书与阅读':'1800',
    '效率办公':'2500',
    '生活':'2900',
    '摄影摄像':'2400',
    '体育运动':'1200',
    '娱乐消遣':'2000',
    '实用工具':'2300',
    '聊天与社交':'3000',
    '学习与教育':'2600',
    '时尚与购物':'3200',
    '旅行与交通':'1100,2800',
    '医疗与健康':'1300',
    '新闻':'2700',
    '理财':'3100',
    '策略':'3600',
    '竞速':'3600',
    '棋牌':'3600',
    '音乐游戏':'3600',
    '飞行模式':'3600',
    '动作冒险':'3600',
    '角色扮演':'3600',
    '体育运动':'3600',
    '益智解密':'3600',
    '重力感应':'3600',
    #安卓市场
    '工具':'2300',
    '对战格斗':'3600',
    '其他游戏':'3600',
    '便捷生活':'2900',
    '网购支付':'3100',
    '资讯':'2700',
    '赛车竞速':'3600',
    '拍摄美化':'2400',
    '模拟经营':'3600',
    '聊天通讯':'3400',
    '动态壁纸':'1400',
    '出版-生活情感':'1800',
    '社交网络':'3000',
    '网络模拟':'2300',
    '策略游戏':'3600',
    '站外应用':'2300',
    '淘宝店铺':'3200',
    '效率':'2500',
    '射击游戏':'3600',
    '其他软件':'3700',
    '金融理财':'3100',
    '新闻资讯':'2700',
    '通讯':'3400',
    '辅助工具':'2300',
    '棋牌桌游':'3600',
    '影音':'2100,3500',
    '经营':'3600',
    '书籍阅读':'1800',
    '浏览器':'3300',
    '系统安全':'2300',
    '通信':'3400',
    '益智游戏':'3600',
    '学习办公':'2500',
    '阅读':'1800',
    '卡片棋牌':'3600',
    '主题插件':'1000',
    '出版-文史小说':'1800',
    '出行':'2800',
    '虚拟养成':'3600',
    '健康':'1300',
    '生活实用':'2900',
    '影音图像':'3500,2100',
    '体育':'1200',
    '休闲':'3600',
    '壁纸美化':'1400',
    '拍照':'2400',
    '通话通讯':'3400',
    '角色冒险':'3600',
    '动作格斗':'3600',
    '个性化':'1000',
    '原创-言情':'1800',
    '角色':'3600',
    '原创-都市':'1800',
    '购物':'3200',
    '安全':'2300',
    '网游':'3600',
    '射击':'3600',
    '图书阅读':'1800',
    '教育':'2600',
    '购物娱乐':'3200,2000',
    '飞行射击':'3600',
    '原创-玄幻':'1800',
    '原创-历史':'1800',
    '经营策略':'3600',
    '经营养成':'3600',
    '影音播放':'2100,3500',
    '益智':'3600',
    '手机网游':'3600',
    '网络社区':'3000',
    '地图导航':'2800',
    '理财购物':'3100,3200',
    '原创-仙侠':'1800',
    '原创-竞技':'1800',
   
    '出版-养生保健':'1800',
    '儿童':'2600',
    '原创-屌丝':'1800',
    '原创-穿越':'1800',
    '游戏':'3600',
    '原创-惊悚':'1800',
    '原创-军事':'1800',
    '原创-网络':'1800',
    
    '原创-科幻':'1800',
    '出版-时尚娱乐':'1800',
    '出版-经管励志':'1800',
    '原创-同人':'1800',
    '休闲益智':'3600',
    '动作射击':'3600',
    '体育竞技':'3600',
    '网络游戏':'3600',
    '棋牌游戏':'3600',
    '策略塔防':'3600',
    '卡牌策略':'3600',

'动漫':'3600',
'生活时尚':'2900',
'回合战斗':'3600',
'媒体与视频':'2100',
'精选游戏':'3600',
'交通运输':'1100',
'音乐与音频':'3500',
'射击冒险':'3600',
'健康与健身':'1300',
'词典':'2300',
'娱乐':'2000',
'必备软件':'3300',
'益智和解谜':'3600',
'有声读物':'1800',
'休闲其它':'3600',
'天气':'1900',
'新闻杂志':'2700',
'最新游戏':'3600',
'软件与演示':'3300',
'图书与工具书':'1800',
'摄影':'2400',
'纸牌和赌博':'3600',
'财务':'3100',
'中文游戏':'3600',
'医药':'1600',
'旅游与本地出行':'2800',
'商务':'1700',
'即时动作':'3600',
'网站应用':'3300',
'街机和动作':'3600',



}
CATEGORY_NAME = {
'0'   :'未分类',  
'1000':'个性化',
'1100':'交通运输',
'1200':'体育',
'1300':'健康与健身',
'1400':'动态壁纸',
'1500':'动漫',
'1600':'医药',
'1700':'商务',
'1800':'图书与工具书',
'1900':'天气',
'2000':'娱乐',
'2100':'媒体与视频',
'2200':'小部件',
'2300':'工具',
'2400':'摄影',
'2500':'效率',
'2600':'教育',
'2700':'新闻杂志',
'2800':'旅游与本地出行',
'2900':'生活时尚',
'3000':'社交',
'3100':'财务',
'3200':'购物',
'3300':'软件与演示',
'3400':'通讯',
'3500':'音乐与音频',
'3600':'游戏',
'3700':'其他'

}

def get_category_id_by_name(category_name,item):
    '''
    *   根据抓取来的应用名来获取对应在分类系统中的适合的id
    *   如果没有找到对应项，则说明抓取到的该分类属于新分类，记录在`un_record_category.txt`文件中，等待人工进行分类确认
    *   input: category_name
    *   output: category_id
    '''
    if not CATEGORY_ID.get(category_name):
        flag = True
        category_map = {}
        for line in open('un_record_category.txt','r'): 
            if line.strip() == category_name:
                flag = False
                break
            category_map[line.strip()] = 1
	category_map[category_name] = 1
        if flag:
            with open('un_record_category.txt','w') as f: 
                for key in category_map.keys(): 
                    f.write(key +' '+ item['app_name']+' '+item['platform']+"\n")
        return "0"
    return CATEGORY_ID.get(category_name)

def get_category_name_by_id(category_id):
    '''
    *   根据category_id来获取对应在分类系统中的名称，如果没有找到，则输出'无'，不过应该不会出现这种情况
    *   input:  category_id
    *   output: category_name
    '''
    if not CATEGORY_NAME.get(category_id):
        return "无"
    else:
        return CATEGORY_NAME.get(category_id)