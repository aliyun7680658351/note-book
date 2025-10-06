MAX_diary = 10#最高分10分
MIN_diary = 1#最低分1分
#数据层，准备数据，缺点:要知道制定了什么数据
diary_score1 = 5#存储单篇日记评分
diary_score2 = 8#存储单篇日记评分
diary_score3 = 10
#total_score = 10#累计总评分
#average_score = 7.5#平均评分
title_diary = 'python日记'#日记标题
content_diary = '今天学习了python基础语法'#日记内容
time_diary = '2025.10.10'#日期时间
#计算层:处理逻辑
diary_score1,diary_score2,diary_score3 = 6,9,10
Max_score = max(diary_score1,diary_score2,diary_score3)
Min_score = min(diary_score1,diary_score2,diary_score3)
point = diary_score1+diary_score2+diary_score3
average_score = (diary_score1+diary_score2+diary_score3)/3
with_high_score = Max_score - diary_score1#diary_score1与最高分的差值
is_high_score = diary_score1 >7
is_perfect_score = diary_score1>=10
can_imporve = diary_score1>  5
is_valid_score = diary_score1> 3 and can_imporve
#展示层:输出信息
print('日记1的评分'+str(diary_score1))
print('日记2的评分'+str(diary_score2))
print('日记3的评分'+str(diary_score3))
print('日记1的内容'+str(content_diary))
print('写日记的时间'+str(time_diary))
print('最高分是'+str(Max_score))
print('最低分是'+str(Min_score))
print('三个日记的总分'+str(point))
print('三个日记的平均分'+str(average_score))
print('日记1和最高分的差距'+str(with_high_score))
print('日记1属于高分吗?'+str(is_high_score))
print('日记1是满分吗?'+str(is_perfect_score))
print('日记需不需要修改'+str(can_imporve))
print('日记合格吗?'+str(is_valid_score))