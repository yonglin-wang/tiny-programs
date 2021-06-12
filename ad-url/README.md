# ad_url: Automated Serial URL Opener

## Use Case

For some work I am doing right now, I need to open a serial of pages with incremental IDs at the end of the url, e.g. ```some.link.com/locationID=0```,  ```some.link.com/locationID=50```,  ```some.link.com/locationID=100```, etc, all the way up to some specific location, e.g.  ```some.link.com/locationID=450```. Entering each address in one by one for each template was *slightly* inefficient, and I also sometimes forgot which number I was at...

In other words, I have a work routine where I have a template url, e.g. ```some.link.com/locationID=```, and a maximum ```locationID```, $\text{maxID}$, which the location should always be smaller than. The task is to open multiple tabs in one browser window, each tab containing an url starting from ```locationID=0```, going up by 50 each time, and all the way up to ```location ID=50*n``` where $50 \times n<\text{maxID}$ and $50 \times (n+1)\geq\text{maxID}$.

## How to Run

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

## Notes

There's several tutorials I used to understand the unique blend of natural language and bash-like syntax (am I complaining? I don't know.) of AppleScript: [variables and increments](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/conceptual/ASLR_variables.html#//apple_ref/doc/uid/TP40000983-CH223-SW10), [controlling Chrome with Apple Script through commandline](https://apple.stackexchange.com/questions/306627/how-can-i-open-multiple-urls-in-a-new-chrome-window-from-the-terminal), [string concatenation](https://alvinalexander.com/blog/post/mac-os-x/applescript-concatenate-strings/), and [while loops](https://alvinalexander.com/apple/applescript-for-loop-while-loop-examples/).  

This script talks (thanks to the ```say``` syntax), wooo! 
