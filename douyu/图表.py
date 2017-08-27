import pyecharts as p
from pyecharts import Timeline
#这些数据是经过excel处理的
attr = ['19:03:00', '19:33:00', '20:03:00', '20:33:00', '21:03:00', '21:33:00',
        '22:03:00','22:33:00','23:03:00','23:33:00']
  
wu1 = [34000,783000,1540000,1150000,1580000,1490000,1630000,1720000,2210000,2120000]
zh1 = [2950000,3020000,2990000,2840000,3040000,2800000,2950000,2800000,2970000,2800000]
line1 = p.Line('8月17号')
line1.add('五五开',attr,wu1)
line1.add('张大仙',attr,zh1,is_smooth=True)

wu2 = [1140000,1640000,1960000,2380000,1890000,1720000,2120000,2850000,3280000,2850000]
zh2 = [2300000,2530000,2770000,2760000,2690000,2690000,2690000,2680000,2760000,2800000]
line2 = p.Line('8月10号')
line2.add('五五开',attr,wu2)
line2.add('张大仙',attr,zh2,is_smooth=True)

wu3 = [1130000,2470000,2730000,2500000,2930000,3330000,3550000,3180000,2780000,2700000]
zh3 = [2100000,2200000,2780000,2800000,2790000,2670000,2830000,2800000,2720000,2810000]
line3 = p.Line('8月9号')
line3.add('五五开',attr,wu3)
line3.add('张大仙',attr,zh3,is_smooth=True)

wu4 = [1140000,1940000,2590000,2550000,2220000,2540000,2660000,2420000,2520000,2450000]
zh4 = [2750000,2720000,2770000,2680000,2850000,2790000,2770000,2700000,2730000,2800000]
line4 = p.Line('8月8号')
line4.add('五五开',attr,wu4)
line4.add('张大仙',attr,zh4,is_smooth=True)

timeline = Timeline(is_auto_play=False, timeline_bottom=0)
timeline.add(line1, '8月17号')
timeline.add(line2, '8月10号')
timeline.add(line3, '8月9号')
timeline.add(line4, '8月8号')
timeline.render()





