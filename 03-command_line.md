# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 
    pushd - push directory
    popd - pop directory
    less - page through a file
    cat - print a whole file
    apropos - find what man page is appropriate
    echo - print some arguments
    xargs - execute arguments
    cp - copy a file or directory
    mv - move a file or directory
    env - look at your environment

---

###Q2.  List Files in Unix   

What do the following commands do:  
> >
    `ls`     - lists files and directories 
    `ls -a`  - does not hide entries starting with .
    `ls -l`  - lists the files and directories. Also shows where they are located and when they were modified.
    `ls -lh` - lists the files and directories. Also shows where they are located and when they were modified. Prints sizes in human readable format
    `ls -lah`- same as lh except it does not hide entries starting with .
    `ls -t`  - sort the lists of files by modification time
    `ls -Glp`- inhibit display of group information, file type, and includes l's function


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> >
    'ls -d'  - displays only dictionaries
    'ls -r'  - displays files in reverse order
    'ls -u'  - displays files by access time
    'ls -1'  - displays each entry on a line
    'ls -R'  - displays subdirectories as well

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 
    'xargs' executes arguments.
    An example of how to use it is with "echo a b c d e f| xargs". This will return "a b c d e f".

 

