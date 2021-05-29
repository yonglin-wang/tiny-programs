# tiny-programs
One-script utility programs created to handle daily tasks. Sometimes scripted in Chinese. Description also sometimes in Chinese. 

# AppleScript Programs

To run the executable AppleScripts in this directory like bash commands in the current session, export the directory the script is in to ```$PATH```: 

```bash
export PATH="$PATH:<absolute path to script's directory>"
```

To make the change permanent and use the script in every session, you can [append the above ```export``` command to ```~/.bashrc```](https://stackoverflow.com/a/19662865/6716783).

## ad_url: Automated Serial URL Opener

### Use Case

For some work I am doing right now, I need to open a serial of pages with incremental IDs at the end of the url, e.g. ```some.link.com/locationID=0```,  ```some.link.com/locationID=50```,  ```some.link.com/locationID=100```, etc, all the way up to some specific location, e.g.  ```some.link.com/locationID=450```. Entering each address in one by one for each template was *slightly* inefficient, and I also sometimes forgot which number I was at...

In other words, I have a work routine where I have a template url, e.g. ```some.link.com/locationID=```, and a maximum ```locationID```, $\text{maxID}$, which the location should always be smaller than. The task is to open multiple tabs in one browser window, each tab containing an url starting from ```locationID=0```, going up by 50 each time, and all the way up to ```location ID=50*n``` where $50 \times n<\text{maxID}$ and $50 \times (n+1)\geq\text{maxID}$.

### How to Run

1. Make sure you have Chrome installed. The script only works with Chrome browsers. 
2. Download the script "ad_url" from this repository. (e.g. you can right-click and choose "Download Linked File")
3. Put the file in a new, empty folder, e.g. ```my_adj_folder/```
4. Open terminal and enter the following command, substituting ```<absolute path to script's directory>``` with the absolute path to the folder you saved ```ad_url``` to:
    ```bash
    export PATH="$PATH:<absolute path to script's directory>"
    ```
    (Note: this ```export``` command is only effective for your current terminal session; to make the change permanent and use the script in every session, you can [append the above ```export``` command to ```~/.bashrc```](https://stackoverflow.com/a/19662865/6716783).
4. Use the command to open multiple pages, exciting!
    Remember to put double quotes around the template for the command to be parsed correctly. 

    ```bash
    ad_url "<template>" <max Location ID>
    ```

    For example, if I have a template of ```some.link.com/locationID=``` and want to open tabs with a maximum ID of 124, i.e. to open ```some.link.com/locationID=0```,  ```some.link.com/locationID=50```, and ```some.link.com/locationID=100```, I'll run:

    ```bash
    ad_url "some.link.com/locationID=" 124
    ```

    Upon opening, the script says (yes, says as in vocalizes) "opening chrome", then tells you how many total pages have been opened. 

### Notes

There's several tutorials I used to understand the unique blend of natural language and bash-like syntax (am I complaining? I don't know.) of AppleScript: [variables and increments](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/conceptual/ASLR_variables.html#//apple_ref/doc/uid/TP40000983-CH223-SW10), [controlling Chrome with Apple Script through commandline](https://apple.stackexchange.com/questions/306627/how-can-i-open-multiple-urls-in-a-new-chrome-window-from-the-terminal), [string concatenation](https://alvinalexander.com/blog/post/mac-os-x/applescript-concatenate-strings/), and [while loops](https://alvinalexander.com/apple/applescript-for-loop-while-loop-examples/).  

This script talks (thanks to the ```say``` syntax), wooo! 

# Python Programs

All python programs will be made executable, so no need to add ```python``` before the script name in command line. 

## combo-gen.py: Combo Generator

### Use Case

Wrote this when trying to decide on how we wanted to build our BBQ combo. When we made up our minds and ordered, the restaurant told us that we didn't actually have a choice :| 得亏他们家做的烤串和涮串都还挺好吃……

### How to Run
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

### Notes
#### Formatting alignment with Chinese characters
See problem and solution stated in [this CSDN post](https://blog.csdn.net/weixin_42280517/article/details/80814677).

#### Generating fixed numbers with fixed sum
Use ```np.random.multinomial(_sum, np.ones(n)/n, size=1)[0]``` to get a random integer array of size ```n``` that sums to ```_sum```. Idea see [this post](http://sunny.today/generate-random-integers-with-fixed-sum/). 

#### Determine if text contains Chinese characters
```re.compile``` with Chinese unicode pattern ```u'[\u4e00-\u9fa5]+'``` seems to be the most efficient. More Discussion see [this blog post](https://blog.csdn.net/wds2006sdo/article/details/52801533).





