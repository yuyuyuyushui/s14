def selectChina(currentGroup, history):
    print("Choice Menu. 'b' for back to upper menu, 'q' for exit.")
    if currentGroup == {}:
        print("it is last menu.")
    else:
        for i1 in currentGroup:
            print(i1)
    choice = input('enter your choice: ')
    if choice == 'b':
        if len(history) <= 0:
            print("it is top menu.")
            return selectChina(China, [])
        else:
            history.pop()
            print(history)
            return selectChina(history.pop(), history)

    if choice == 'q':
        exit()
    if choice in currentGroup:
        try:
            # currentGroup[choice]
            history.append(currentGroup)
            return selectChina(currentGroup[choice], history)
        except:
            print("it is last menu.")
    return selectChina(currentGroup, history)
China = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'Google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            }
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{}
            },
            '天通苑':{},
            '回龙观':{}
        },
        '朝阳':{},
        '东城':{}
    },
    '上海':{},
    '湖北':{},
    '广东':{}
}
selectChina(China, [])