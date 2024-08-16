


> [Web_Stack_Debugging](https://stackedit.io/).
##  The task here is aimed at improving debugging skills set
  
  **Task:**
- Using  `strace`, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).
#### Hint:

-   `strace`  can attach to a current running process
-   You can use  [tmux](https://intranet.alxswe.com/rltoken/6GpArtwhw7thSyNub9s3qA "tmux")  to run  [strace](https://intranet.alxswe.com/rltoken/ueMevAif95DjyW2sqVCMoA "strace")  in one window and  `curl`  in another one

##### Requirements:

-   Your  `0-strace_is_your_friend.pp`  file must contain Puppet code
-   You can use whatever Puppet resource type you want for you fix

## For the machine level, you want to ask yourself these questions:

-	Does the server have free disk space? - df
Is the server able to keep up with CPU load? - w, top, ps
Does the server have available memory? free
Are the server disk(s) able to keep up with read/write IO? - htop

-	If the answer is no for any of these questions, then that might be the reason why things are not going as expected. There are often 3 ways of solving the issue:

-	free up resources (stop process(es) or reduce their resource consumption)
increase the machine resources (adding memory, CPU, disk space…)
distributing the resource usage to other machines
