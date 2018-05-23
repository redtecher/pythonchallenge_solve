# PythonChallenge
解决[pythonchallenge.com](pythonchallenge.com)中题目的代码。
## 第0关
2的38次方，得到值赋值到url中
## 第1关
字符转义 每个字符串增加2
翻译出来后题目推荐你使用方法
`string.maketrans()`

*maketrans()
在Python3中，不存在maketrans方法
使用时使用内建函数*
`str.maketrans()`
```python
x='abcdefghijklmnopqrstuvwxyz'
y='cdefghijklmnopqrstuvwxyzab'
trans=str.maketrans(x,y)
string.translate(trans)

```
