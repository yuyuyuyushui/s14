import shutil
import sys

print(sys.path)

f1 = open('dream', encoding='utf-8')
f2 = open('歌词.txt', 'w', encoding='utf-8')
#shutil.copyfileobj(f1, f2)
#shutil.copystat('dream', '歌词.txt')
#shutil.copytree('day5', 'new')#递归的拷贝目录树
#shutil.rmtree('day5', 'new')#递归的删除目录树
shutil.make_archive('make_arc', 'zip', 'D:\s14\day5')