#有麸质食物

#True   代表可以食用
#False  代表不可以食用
gluten_food={
        "小麦":False,"麦芽":False,"黑麦":False,"大麦":False,
        "蒸粗麦粉":False,"淀粉":False,"全麦面粉":False,"斯佩耳特小麦":False,
        "黑小麦":False,"酱油":False,"黑醋":False,"料酒":False,"豆瓣酱":False,
        "辣椒酱":False,"沙拉酱":False,"包装高汤":False,"蛋黄酱":False,
        "奶酪":False,"罐头肉":False,"鸡蛋替代物(人造蛋黄)":False,
        "罐头豆制品":False,"啤酒":False,"速溶热饮":False,"巧克力牛奶":False,
        "大麦清汁":False,"伏特加":False,"燕麦片":False,"烤坚果":False,
        "肉丸子":False,"炸薯条":False,"能量棒":False,"冰激凌":False
        }


while True:
    print("请输入你要查询的食物:")
    food=input()
    if food=="q" or food=="quit":
        break
    if food in gluten_food.keys():
        print(food+"属于麸质食物，桥本甲状腺炎患者不推荐使用")
    else:
        print("暂未查询到该食物")





