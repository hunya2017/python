#循环
# python循环有两种,

#####
#一种是  for...in循环.例如 依次把list或tuple中的每个元素迭代出来
names = ['a','b','c']
for name in names:
    print(name)         #把每个元素代入变量nama


#计算1-100的整数之和
#python提供了一个 range() 函数,可以生成一个整数序列,再通过 list()函数转换为list
print(list(range(5)))
#range(101)就是生成0-100的整数序列
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

#####
#另一种是while循环,只要条件满足就一直循环,条件不满足时退出循环

#例如计算100以内的奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#break 提前结束循环
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#continue可以结束本轮循环,并开始下一轮循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
