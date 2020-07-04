# rough verilog parser generation
A rough verilog parser generation and build by python

# background

In IC development, it is pretty bother to sort out every ports regs and wires for each module. The instantation work between the modules also annoying developers. Though this project, you can insert the correspinding tag to anto generate the verilog files.

I hope that this project can improve the sense of happiness of IC developers.

Support Verilog-2001

There is currently no R&D plan to support system verilog for this moment

More details...

# Depends
Base on Python3.8. Considering that most first-line engineers carry out development work on a server on an isolated network. This project try to use simple and easy-to-install standard libraries, and as little possible as rely on external tools

Current used libraies:

   * sys
   * getopt
   * sqlite3
   * copy
   * re
   * pprint

# Maintainers

Just me, lol

# License

GNU General Public License v3.0 
