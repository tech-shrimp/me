import random

# 名字长度 2-7 的自然数
name_length = 2
# 南方1 北方2 分不清3
north_south = 1
# 男1 女2
gender = 1

cards = [1, 2, 3, 4]
cards = cards + cards
print(cards)
# [1, 2, 3, 4, 1, 2, 3, 4]

# 将队头的name_length张插入队尾
for _ in range(name_length):
    cards.append(cards.pop(0))
print(cards)
# [3, 4, 1, 2, 3, 4, 1, 2]

# 将队头的三个元素 插入中间
top_three = cards[:3]
last_five = cards[3:]
# 随机生成插入位置
location = random.randint(1, 4)
cards = last_five[:location] + top_three + last_five[location:]
print(cards)
# [2, 3, 3, 4, 1, 4, 1, 2]


under_butt = cards.pop(0)
print("屁股下的牌：" + str(under_butt))
# 屁股下的牌：2

top_cards = cards[:north_south]
last_cards = cards[north_south:]
# 随机生成插入位置
location = random.randint(1, 7-north_south-1)
cards = last_cards[:location] + top_cards + last_cards[location:]
print(cards)
# [3, 4, 3, 1, 4, 1, 2]

for _ in range(gender):
    cards.pop(0)
print(cards)
# [4, 3, 1, 4, 1, 2]

print("见证奇迹的时刻")
for _ in range(7):
    cards.append(cards.pop(0))
print(cards)
# [3, 1, 4, 1, 2, 4]

while len(cards) > 1:
    # 好运留下来
    cards.append(cards.pop(0))
    # 烦恼丢出去
    cards.pop(0)
    print(cards)
'''
[3, 3, 4, 1, 2, 1]
[4, 1, 2, 4, 3]
[2, 4, 3, 4]
[3, 4, 2]
[2, 3]
[2]
'''
assert cards[0] == under_butt
