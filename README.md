# 可以用来填充秘密花园的Python程序
1. 被填充图案必须由纯黑色(RGB(0,0,0))线条勾勒而成，图案必须是封闭的，连通区域只填充一次颜色。
2. 程序寻找色块使用广度优先搜索，未做优化，实际使用中5000px*5000px包含1500种颜色的图片填充需要90秒。
3. 程序需要引用PIL第三方库。

# Python program to fill picture sketched by the black lines.
1. The lines used as sketch picture have to be black color(RGB(0,0,0)), lines must be closed.
2. The program need to refer to libraries PIL.