# combo-gen.py: Combo Generator

## Use Case

Wrote this when trying to decide on how we wanted to build our BBQ combo. When we made up our minds and ordered, the restaurant told us that we didn't actually have a choice :| 得亏他们家做的烤串和涮串都还挺好吃……

## How to Run
This script is command-line enabled. Use ```$ ./combo-gen.py -h``` to see help.

It can recognize Chinese characters and switch to Chinese. Otherwise, English output strings will be used.

Example 1: Chinese input. Remember to put ascii double quotes around text list if containing whitespaces in between.
```bash
./combo-gen.py 鹌鹑蛋，鱼豆腐，菜卷，毛肚，油豆腐，鱼丸，大白菜，海带结，木耳，蘑菇 30
```
Output:
```
鹌鹑蛋：    2份
鱼豆腐：    4份
菜卷　：    2份
毛肚　：    1份
油豆腐：    3份
鱼丸　：    3份
大白菜：    2份
海带结：    2份
木耳　：    5份
蘑菇　：    6份
共10种，共计30份
```

Example 2: Non Chinese input, remember to put double quotes around list text.
```bash
./combo-gen.py "chocolate chip, oatmeal rasin, sugar, molasses, ginger snap" 20
```
Output:
```
chocolate chip 3         
oatmeal rasin  4         
sugar          4         
molasses       5         
ginger snap    4         
Total types: 5
Total count: 20
```

## Notes
### Formatting alignment with Chinese characters
See problem and solution stated in [this CSDN post](https://blog.csdn.net/weixin_42280517/article/details/80814677).

### Generating fixed numbers with fixed sum
Use ```np.random.multinomial(_sum, np.ones(n)/n, size=1)[0]``` to get a random integer array of size ```n``` that sums to ```_sum```. Idea see [this post](http://sunny.today/generate-random-integers-with-fixed-sum/). 

### Determine if text contains Chinese characters
```re.compile``` with Chinese unicode pattern ```u'[\u4e00-\u9fa5]+'``` seems to be the most efficient. More Discussion see [this blog post](https://blog.csdn.net/wds2006sdo/article/details/52801533).

