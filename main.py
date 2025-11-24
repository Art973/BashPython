while(c:=input('> '))not in['exit','quit']:print(__import__('os').popen(c).read())
