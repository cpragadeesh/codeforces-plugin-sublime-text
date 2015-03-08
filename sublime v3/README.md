# codeforces-plugin-sublime-text

Note: Works only for C++ code.

What it does?
Compiles your C++ code, Build it, fetch test cases, run your code on it, Compares output.

What it does not do:
Magically identify your problem over the internet and judge it.

Requirements:
1. Requires G++ to be installed.
2. Sublime 

Installation:
1. Copy and paste the folder into sublime packages directory.

Usage:
1. Save your C++ code as 'problemID.cpp'; Where problemID is the Contest ID followed by the problem Code, Such as 520A, 520a, 136c...
2. Choose build system as 'Codeforces' from Tools>Build System>Codeforces.
3. Hit Tools>Build or Cmd/Ctrl + B on OS X/Linux Machines.
4. Check the console for verdict.

Note: Build make take a while(as long as 50 secs) depending upon your connection. 