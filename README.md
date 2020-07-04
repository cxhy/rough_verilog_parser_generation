# rough verilog parser generation
一个粗糙的 verilog 解析，生成工具

# 背景
在 IC 开发中，一个比较麻烦的事情是就是生成每个模块的端口。以及端口之间的例化工作，通过这个项目，可以通过verilog内部插入对应的标签可以生成对应的 verilog 工程文件。

希望可以通过这个项目提高 IC 开发人员工作的辛福感

支持verilog 2001 版本的协议

暂时没有打算支持system verilog的语法特性(主要我是开发人员，不太懂测试那边的东西)

详细的使用说明待补充

# 依赖
计划基于 Python3.8 开发，考虑到大多数一线工程师在隔离网络的服务器上进行开发工作，所以尽量只使用简单易于安装的标准库，尽量不依赖外部的工具。当前计划用到的库有

   * sys
   * getopt
   * sqlite3
   * copy
   * re
   * pprint

# 贡献者

眼下只有我一个人，但是我只是一个普通的芯片工程师，对于 python 的使用还仅仅处于比较业余的水平。

# 开源协议

GNU General Public License v3.0 
