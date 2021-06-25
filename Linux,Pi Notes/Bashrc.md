## Bashrc

**Introduction to Bashrc**

The `~/.bashrc` is kind of like a configuration file that runs whenever each terminal is open.  

To open your bashrc file, you use the command : `gedit ~/.bashrc`. I've set mine to an alias `bashrc` (covered later on), so I dont have to type this cancerous command which makes my fingers hurt every time.



On a new distribution, sometimes gedit is not installed. We install this via the command `sudo apt install gedit`



Sometimes, the bashrc may not update when you add stuff to it. In that case, just "refresh" it!  

We "refresh" by using the source command : `source ~/.bashrc`  



You may add `alias` to the bashrc so that you can "configure" your own commands. 



### Alias

`alias <aliasname>='<commands>'`

there can not be any whitespace btw `<aliasname>`,`=`, and `<commands>`

You append this command into the bashrc. It runs whenever you open a new terminal. Hence, whatever pseudo code you manage to come up with will be code for the system. Take a look at my personal list of aliases to get a general idea of its usefulness.



**My personal list of Aliases to copypaste across computers**

append this at the bottom of your bashrc, does not matter where.

```
# my own aliases
alias bashrc='gedit ~/.bashrc'
alias srcbashrc='source ~/.bashrc'
alias dl='curl -LJO'
alias temp='/opt/vc/bin/vcgencmd measure_temp'
```





------

------
