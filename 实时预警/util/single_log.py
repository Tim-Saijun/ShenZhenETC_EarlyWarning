import random
import time
import datetime
import os
import sys
import shelve

# XH=sys.argv[1] # 车辆序号
XH = 1
CP = [  # 车牌
    "京", "津", "沪", "渝", "桂", "蒙", "新", "宁", "藏", "冀", "豫",
    "云", "辽", "黑", "湘", "皖", "鲁", "苏", "浙", "赣", "鄂", "甘",
    "晋", "陕", "吉", "闽", "贵", "粤", "青", "川", "琼", "粤"
]

CX = [  # 车型
    "二型车(货)", "二型车(客)", "六型车(货)",
    "三型车(货)", "三型车(客)", "四型车(货)",
    "四型车(客)", "五型车(货)", "一型车(货)",
    "一型车(客)"
]

SFZCKMC = [  # 收费站出口名称
    "广东罗田主线站",
    "广东水朗D站",
    "松山湖南"
]

# 出口时间
# time_now = time.localtime()
time_now = datetime.datetime.now()
time_out = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

SFZRKMC = [  # 收费站入口名称
    'SFZRKMC', '安徽鲍集站', '安徽亳州南站', '安徽曹庄站', '安徽滁州东站', '安徽宁马站', '福建大田站', '福建东山站', '福建福鼎北站', '福建海沧站', '福建蛟洋站', '福建连城站',
    '福建南靖站', '福建宁德北站', '福建平和安厚站', '福建平和三平站', '福建厦门站', '福建小陶站', '福建延平北站', '福建永定下洋站', '福建云霄火田站', '福建诏安东站', '福建诏安南站',
    '甘肃平凉东收费站', '广东安塘站', '广东白泥坑站', '广东白沙站', '广东白土站广肇', '广东白云前站', '广东白云仔站', '广东白云站', '广东板芙站', '广东宝安站', '广东北村站', '广东北惯站',
    '广东北滘站', '广东笔村站', '广东碧江站', '广东伯公坳站', '广东博爱路站', '广东博罗站', '广东沧江站', '广东草堂站', '广东常虎中心站', '广东常平站', '广东陈山站', '广东城北站粤赣',
    '广东城口南站', '广东城南站', '广东城区站', '广东城西站', '广东程村站', '广东池尾站', '广东赤岗站', '广东冲鹤站', '广东从化站', '广东翠亨站', '广东达濠站', '广东大夫山站',
    '广东大观路站', '广东大江站', '广东大朗站', '广东大沥站', '广东大岭山站', '广东大坪站莞深一二期', '广东大沙站', '广东大旺北站', '广东大旺站', '广东大溪站', '广东大雁山站', '广东大镇站',
    '广东丹灶站', '广东淡水东站', '广东淡水站', '广东道滘站', '广东灯塔站', '广东登岗站', '广东登云站', '广东鼎湖站', '广东东部快速路站', '广东东成站', '广东东阜站',
    '广东东莞东站', '广东东莞站莞深一二期', '广东东莞站广深', '广东东湖站', '广东东沙站', '广东东沙主线站', '广东东深路站', '广东东升站', '广东东源站', '广东斗门站沿海珠海', '广东端州站',
    '广东多祝站', '广东丰顺站', '广东凤岗站博深', '广东凤塘站', '广东佛冈站', '广东佛高区乐平站', '广东佛平路站', '广东福安站', '广东福民站', '广东福田站从莞惠州', '广东福永站',
    '广东附城站云罗', '广东富安站', '广东富地岗站', '广东岗美站', '广东港口站', '广东高赞站', '广东高州南站', '广东高州站', '广东古猛站', '广东古巷与潮漳主线连接处站', '广东古镇站',
    '广东观澜站', '广东官渡站', '广东官华路站', '广东官井头站', '广东莞龙站', '广东莞樟路站', '广东灌村站', '广东广从站', '广东广佛新干线站', '广东广清站', '广东广汕站', '广东广太站',
    '广东广园站', '广东广州南站', '广东归湖站', '广东桂丹站', '广东国泰站', '广东海布站', '广东海丰西站', '广东海丰站', '广东海门站', '广东海鸥岛站', '广东海湾站', '广东海五路站',
    '广东海洲站', '广东和平站', '广东河婆站', '广东河浦站', '广东河头南站', '广东河源站', '广东荷坳站机荷东', '广东荷城站', '广东荷塘站', '广东横岗站', '广东横江站', '广东横栏站',
    '广东虹岭路站', '广东洪梅站', '广东洪湾站', '广东厚街站', '广东鲘门站', '广东湖光站', '广东湖心站', '广东湖镇站', '广东虎门北站', '广东花山站', '广东华快广汕站', '广东华快花城站',
    '广东华快黄埔站', '广东华快龙洞站', '广东华快土华站', '广东华快新洲站', '广东华快中山站', '广东华阳路站', '广东化州北站', '广东化州西站', '广东环镇西站', '广东黄村站', '广东黄阁站广珠北段',
    '广东黄鹤站', '广东黄江站', '广东黄麻站', '广东黄埔主线站', '广东黄石南站', '广东黄田站广贺', '广东灰寨站', '广东惠东北站', '广东惠来站', '广东惠州东站', '广东惠州港站', '广东惠州站',
    '广东机场T3站', '广东机场西站', '广东机场站机场', '广东吉利大道站', '广东季华东站', '广东江口站', '广东街口站街北', '广东金谷站', '广东金鸡站', '广东金利站', '广东金龙站',
    '广东金沙站', '广东金山大道东站', '广东金台站', '广东金灶站', '广东军垦农场站', '广东开发大道站', '广东开平站', '广东科韵路站', '广东坑梓站', '广东蓝塘站', '广东蓝田站揭博',
    '广东榄核站', '广东乐村坪站', '广东乐平站', '广东勒流站', '广东雷岭站', '广东雷州站', '广东礼乐站', '广东里广路南侧站', '广东里广路站', '广东里和站', '广东立沙岛站', '广东沥林北站',
    '广东沥林站', '广东沥心沙站', '广东荔城站', '广东连南站清连', '广东连平南站', '广东连山站', '广东廉江东站', '广东廉江南站', '广东良井站', '广东梁村站', '广东两英站', '广东林村站',
    '广东霖磐站', '广东灵山站', '广东六花岗站', '广东六里站', '广东龙川东站', '广东龙川西站', '广东龙岗站惠盐深圳', '广东龙岗站水官', '广东龙华站', '广东龙江站南二环',
    '广东龙景站', '广东龙门站新博', '广东龙山站佛开', '广东龙潭站', '广东龙塘站玉湛', '广东龙湾站', '广东龙溪站', '广东龙仙东站', '广东隆江站', '广东陆丰北站', '广东陆河东站', '广东伦教站',
    '广东罗城站', '广东罗田主线站', '广东萝岗站广深', '广东麻陂站', '广东麻涌站广深', '广东麻涌站沿江', '广东麻章站', '广东马岭站', '广东马踏站', '广东马头站', '广东茂名电白站',
    '广东茂名东站', '广东茂名站', '广东梅花北站', '广东梅州站', '广东民众站', '广东睦洲站', '广东那洲站', '广东南岗站', '广东南华寺站', '广东南屏站', '广东南浦站', '广东南沙B站',
    '广东南山站', '广东南头站西线二期', '广东南香山站', '广东南丫匝道站', '广东南丫站', '广东南庄站', '广东内湖站', '广东泥沟站', '广东宁西东站', '广东蓬陵站', '广东平安站', '广东平湖站',
    '广东平南站', '广东坡头站', '广东埔边站', '广东埔前站', '广东埔田站', '广东七星岗站', '广东前海站', '广东浅水站', '广东青塘站', '广东清湖站', '广东清溪湖站', '广东清溪站',
    '广东清远站', '广东容桂站', '广东汝湖站', '广东乳源东站', '广东三栋站', '广东三江站', '广东三角站', '广东三水西站', '广东三水站', '广东三元里站', '广东沙澳站', '广东沙贝站',
    '广东沙富站', '广东沙湖站', '广东沙塘站', '广东沙田东站', '广东沙田站深汕西', '广东沙田站沿江', '广东沙湾站', '广东沙溪站汕揭', '广东沙溪站西线三期', '广东上亨站', '广东上屯站',
    '广东韶关北站', '广东韶关东站', '广东韶关南站', '广东韶关站', '广东畲江站', '广东神龙站', '广东狮岭站', '广东狮山站', '广东石坝站', '广东石大路站', '广东石鼓站', '广东石湖站',
    '广东石碣站', '广东石岭站', '广东石菉站', '广东石排站', '广东石碁站', '广东石头站', '广东石湾站', '广东石岩站', '广东始兴站', '广东数码园站', '广东双东站', '广东双合水台站',
    '广东水墩站', '广东水口站惠大', '广东水口站开阳', '广东水沥站', '广东水足塘站', '广东顺德站', '广东司马浦站', '广东思劳站', '广东四会西站', '广东四会站', '广东四角楼站',
    '广东泗水站', '广东松岗站', '广东松山湖站', '广东苏十顷站', '广东遂溪站', '广东隧华朝阳站', '广东隧华嘉禾站', '广东隧华平沙站', '广东隧华沙太站', '广东隧华同和站', '广东隧华永泰站',
    '广东台城站', '广东太成站', '广东太平站广深', '广东泰美站', '广东泰山站', '广东榃滨站', '广东潭水站', '广东潭洲会展站', '广东坦洲站', '广东炭步站', '广东棠下站', '广东塘清站',
    '广东塘头站', '广东塘缀站', '广东桃园站', '广东桃源站', '广东田心站龙林', '广东田心站深汕东', '广东亭角站', '广东潼湖站', '广东外海B站', '广东外砂站', '广东王子山站', '广东望牛墩站',
    '广东威远B站', '广东围底站', '广东温泉站', '广东文祠站', '广东文教站', '广东乌石站', '广东乌塘站', '广东五沙站', '广东西华站', '广东西坑站', '广东西龙站', '广东西樵站西二环南',
    '广东锡场站', '广东溪之谷站', '广东细沥站', '广东霞湖站', '广东霞涌站', '广东下安站', '广东下桥站', '广东仙村站', '广东仙桥站', '广东仙涌站', '广东蚬岗站', '广东香雪站',
    '广东小金口站广惠', '广东小榄站', '广东小楼站', '广东谢边站', '广东谢岗站', '广东新陂站', '广东新丰南站', '广东新桂路站', '广东新和站', '广东新华站', '广东新龙站', '广东新龙站花莞',
    '广东新桥站惠大', '广东新塘站', '广东新田站', '广东新圩站惠盐', '广东新圩站兴畲', '广东新兴站', '广东新墟站', '广东信宜北站', '广东信宜站', '广东兴宁西站', '广东兴业路站', '广东兴业站',
    '广东杏坛站', '广东徐闻港站', '广东浔峰洲站', '广东崖南站', '广东盐南公路站', '广东阳春北站', '广东阳春西站', '广东阳江站', '广东仰塘站', '广东仰天堂站', '广东义和站', '广东意溪站',
    '广东英德站', '广东迎宾站', '广东永汉站', '广东永和站惠大', '广东鱼窝头站南二环', '广东玉湖站', '广东园洲东站', '广东园洲站', '广东源水站', '广东源潭站', '广东约场站', '广东云东海站',
    '广东云浮东站', '广东云路站', '广东增城站增从', '广东增城站增莞', '广东湛江赤坎主线站', '广东樟木头南站', '广东樟木头站', '广东长安站广深', '广东长宁站', '广东长沙湾站', '广东长洲站',
    '广东知识城站', '广东中山西站', '广东中心站', '广东中新站', '广东中信大道站', '广东钟落潭站', '广东朱山岗站', '广东珠港站', '广东珠海站', '广东竹料东东站', '广东紫金西站', '广西八鲤站',
    '广西北流站', '广西博白站', '广西大安站', '广西福绵机场站', '广西桂平站', '广西河池东', '广西贺街站', '广西贺州东', '广西灵峰站', '广西柳州北', '广西龙门站', '广西梅花站',
    '广西蒙山收费站', '广西那洪站', '广西南宁东站', '广西平果站', '广西钦州港', '广西渠黎站', '广西容县站', '广西山口站', '广西山围站', '广西上思站', '广西昙容镇', '广西覃塘站',
    '广西藤县站', '广西铁山港主线', '广西梧州西', '广西五塘站', '广西武鸣站', '广西夏郢站', '广西兴业站', '广西玉林站', '广西云表站', '河北保定北站B', '河北大陈庄站', '河北邱县站',
    '河北万庄站',
    '河北永年站', '河南构林站', '河南会盟站', '河南泌阳东站', '河南桐柏东站', '河南西平站', '河南新乡站', '河南郑庵站', '湖北安山站', '湖北崇阳站', '湖北琴台站', '湖北松滋西站',
    '湖北武昌站', '湖北仙桃东站', '湖北阳新南站', '湖北永丰站', '湖南常德东站', '湖南郴州北站', '湖南郴州站', '湖南大托站', '湖南广福站', '湖南黄沙站', '湖南回龙桥站', '湖南酒埠江站',
    '湖南良田站', '湖南娄底南站', '湖南马家河站', '湖南汝城南站', '湖南泗汾站', '湖南锁石站', '湖南万家丽北站', '湖南湘潭北站', '湖南湘潭西站', '湖南新塘站', '湖南雁峰站', '湖南永兴站',
    '湖南永州东站', '湖南雨花站', '湖南岳阳站', '湖南云溪站', '湖南珠晖南站', '吉林长春东收费站', '江苏高港站', '江苏天池站', '江苏无锡北收费站', '江苏无锡新区站', '江西定南东站',
    '江西定南站', '江西鹅公站', '江西分宜站(新)', '江西赣县北站', '江西赣州东站', '江西赣州南站', '江西禾丰站', '江西横市站', '江西胡家坊站', '江西黄马站', '江西黄土岗站', '江西吉安南站',
    '江西吉安县站', '江西吉水南站', '江西江口站', '江西井冈山站', '江西九江站', '江西乐安北站', '江西莲花站', '江西临江站', '江西南城东站', '江西宁都北站', '江西宁都南站', '江西前湖虚拟站',
    '江西瑞昌站', '江西瑞金北站', '江西三百山站', '江西韶口站', '江西泰和东站', '江西泰和站', '江西万安站', '江西峡江站', '江西仙下站', '江西小江站', '江西新城站', '江西信丰北站',
    '江西兴国南站',
    '江西修水站', '江西杨家湖站', '江西永新站', '江西樟树东站', '辽宁北镇站', '辽宁东戴河站', '山东临沂南站', '山东武城东站', '山东兖州站', '陕西鄠邑收费站', '上海嘉松中路站沪常',
    '四川成南南充东站', '四川绕东成龙站', '松山湖南', '塘沽西收费站', '云南昆明北站', '浙江保国寺站', '浙江慈城站', '浙江枫桥南站', '浙江富春江站', '浙江嘉兴东站', '浙江龙泉南站',
    '浙江牟山站', '浙江萧江站', '浙江义亭站', '重庆百合站', '重庆金凤站', '重庆空港东站', '重庆潼南站'
]

# 入口时间=出口时间-随机值

BZ = "深圳入"  # 备注，值为1

def make_CP():
    return random.sample(CP, 1)[0]  # 随机产生一个

def make_CX():
    return random.sample(CX, 1)[0]

def make_SFZCKMC():
    return random.sample(SFZCKMC, 1)[0]

def make_CKSJ():  # 当前时间
    global time_out
    return time_out

def make_SFZRKMC():
    return random.sample(SFZRKMC, 1)[0]

def make_RKSJ():
    global time_out
    d = list(range(3))
    h = list(range(24))
    m = list(range(60))
    s = list(range(60))
    md = random.choice(d)
    mh = random.choice(h)
    mm = random.choice(m)
    ms = random.choice(s)
    time_in = ((time_now + datetime.timedelta(
        days=-md, hours=-mh, minutes=-mm, seconds=-ms))
               .strftime("%Y-%m-%d %H:%M:%S"))
    return time_in

def generate_log():
    global XH
    ETC_log = "{CP}\t{XH}\t{CX}\t{SFZCKMC}\t{CKSJ}\t{SFZRKMC}\t{RKSJ}\t{BZ}" \
        .format(CP=make_CP(), XH=int(XH), CX=make_CX(), SFZCKMC=make_SFZCKMC(),
                CKSJ=make_CKSJ(), SFZRKMC=make_SFZRKMC(), RKSJ=make_RKSJ(), BZ="深圳入")
    print(ETC_log.split())
    #os.system('echo {} >> /usr/data/rawETC.txt'.format(ETC_log))
    #os.system('echo %s >> /usr/data/rawETC.txt' %ETC_log)
    file = open('rawETC.log', 'a')
    file.write(ETC_log + '\n')

if __name__ == "__main__":
    generate_log()
