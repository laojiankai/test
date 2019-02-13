#!/bin/bash
diff -ruNaq /root/test1/ /root/test2/
if [ $? -ne 0 ]; then
    echo "Both file are different"
    echo $?
else
    echo "Both file are same"
    echo $?
fi

function lsdir()
{
for i in `ls`;do
  if [ -d "$i" ] ;then
     cd ./$i
     lsdir
  elif [ "x$i" != "x" ];then
     echo $i
  else 
     continue   
fi
done
}
cd /root/test1
lsdir
