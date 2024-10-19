First, I ran the program. I noticed that it required two files to run, one named flag.txt, and one named rev_this.txt which was given to us.

Next, I opened the program to ghidra to see what the code was doing. I noticed that it opened the flag file in reading mode ("r") and the rev_this file in appending mode "a". This meant that the file that was given to us was the output of this program and we would have to do the opposite of what the program does to get it to its original state.

The program first reads each byte of the flag file and stores it in a seperate variable, it reads 0x18 bytes of this file, so the file likely has 0x18 or 24 characters. The first for loop in the program loops 8 times and just appends each character of the flag file to the rev_this file. This makes sense as the first 8 characters, PicoCTF{ appear in both files the same.

The next for loop loops through the 8th to 24th character in the flag file. It checks if the index it is currently on equals one when performing a bitwiseAND operation (&). This essentially checks if the index is even or odd. If the number is even, the program appends an ascii value +0x5 greater than the corresponding index in the flag to rev_this. If it is odd, the program appends an ascii value -0x2 less to the corresponding index. 

To reverse this process, I created a python script that would start with the end product (rev_this) and do the opposite operations. For even indexes it would -0x5 from the ascii value and +0x2 for odd indexes. This returned the flag picoCTF{r3v3rs37ee84d27}.
