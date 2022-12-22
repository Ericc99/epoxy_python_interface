# Python Threading 多线程
Eric CUI 2022.12.21

## Multi-Threading 101: Life Cycle
线程的生命周期大概可以如下:
![Threading Life Cycle](https://img-blog.csdn.net/20180713112621182?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JydWNld29uZzA1MTY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
函数调用的复杂点就在于一个线程在不同生命周期阶段之间的切换，有很多内置函数。
主要的状态就是Running态和Blocked态，Blocked态当中有包含不同的原因造成的阻塞。
阻塞状态：
睡眠：线程主动调用sleep()或者join()函数
等待：线程主动调用wait()函数，需要其他线程通过notify()唤醒
同步：尝试获取同步锁，但是资源被其他线程占用时
