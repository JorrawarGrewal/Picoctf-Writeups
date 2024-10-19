first, the program will compare ebp+0x8 (our argument) to 0x3a2 which will compare the value of our argument (0x6fa) to 0x3a2.

```assembly
<+3>:   cmp    DWORD PTR [ebp+0x8],0x3a2
```

The next instruction, jg means jump if greater. Since the value of 0x6fa is greater than 0x3a2 it will jump to the address listed which is <asm+37>

```assembly
<+10>:  jg     0x512 <asm1+37>
```

At this instruction <asm+37>, it will compare 0x6fa to 0x6fa. The next instruction jne (jump if not equal) will not jump since both values are equal. 
```assembly
<+37>:  cmp    DWORD PTR [ebp+0x8],0x6fa
<+44>:  jne    0x523 <asm1+54>
```


Next, the program moves our argument, 0x6fa, to the register eax.

```assembly
<+46>:  mov    eax,DWORD PTR [ebp+0x8]
```

The program then substracts 0x12 in hex from 0x6fa which will make eax equal to 6e8.

```assembly
<+49>:  sub    eax,0x12
```

Next, the program jumps and pops ebp to take a value off the stack, this should take 8 byytes off of the top of the stack. Then the instruction ret will return the first value on the stack which should be 0x6e8. (since it was located at ebp+0x8).
```assembly
<+57>:  add    eax,0x12
<+60>:  pop    ebp
<+61>:  ret
```

Finally, the value returned, 0x6e8 should be the flag for this challenge with no wrapper.
