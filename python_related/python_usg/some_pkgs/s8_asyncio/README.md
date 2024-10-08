# asyncio协程

(下面的内容有点问题，但是不影响理解)

## 简单介绍
s8_1_asyncio

本质上还是一段正常的python运行的单进程单线程程序，并不能提高运算速度，比较适合处理那些需要等待的任务，比如网络的通讯

理解什么是coroutine(coroutine function跟coroutine object)和task

1. 运算核心就是`event loop`，就像一个大脑，面对很多可以执行的任务，然后决定执行哪个任务，同时执行的任务只能有一个。需要每个任务告诉`event loop`，我这边结束了，可以执行别的任务了
2. `async def`定义的都是`coroutine function`，返回的都是`coroutine object`。也就是说，如果定义一个`async def main`，当运行`main()`的时候并不会运行里面的程序，只会返回一个`coroutine object`
3. 要运行的话就要进入async模式，然后把`coroutine object`变成task
4. `asyncio.run` 的参数是一个`coroutine object`，它会做两件事，(1) 建立起`event loop`; (2) 把传进去的`coroutine object`变成`event loop`里的第一个task
5. `event loop`建立之后就会去找哪个task可以执行


## 怎么增加task
以s8_2_asyncio为例

1. `await say_after(1, "hello")`：`say_after(1, "hello")`是一个coroutine，await一个coroutine的时候发生如下几件事：
   1. coroutine被包装成一个task并告知event loop
   2. 告诉event loop，要等到`say_after`这个task完成之后，才能继续执行
2. 整个过程：
   1. `asyncio.run(main())`把`main()`作为一个task放到`event loop`，`event loop`寻找task执行，发现只有一个task main，就开始执行`main()`
   2. `main()`运行`say_after`这个`coroutine function`得到一个`coroutine object`
   3. await这个`coroutine object`，把它变成task，放回`event loop`里，同时告诉`event loop`需要等待它，然后把控制权交回给`event loop`
   4. 现在`event loop`里面有两个task，一个是main，一个是say_after，但是main运行不了，因为它要等say_after，所以`event loop`就运行say_after
   5. say_after里面做的事情其实也是类似的，`await asyncio.sleep`
   6. 这时候`event loop`里面有三个task，main、say_after、asyncio.sleep。main要等say_after，say_after要等asyncio.sleep
3. 所有控制权的返回都是显式的，就是`event loop`没有办法强行从一个task拿回控制权，必须这个task主动把控制权交回去，交回去的方式有两种：
   1. await交回
   2. 当这个函数运行完毕之后交回


## 同时等待
s8_3_asyncio

上面的例子，一个等待1秒，一个等待2秒，总共要等3秒，那么能不能同时等呢
`create_task`会把coroutine变成一个task并且把这个task注册到`event loop`里
后面await一个task就跟上面例子的await一个coroutine不一样了
再具体的看视频

## gather
s8_4_asyncio