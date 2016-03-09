# One: Threads #
## Which of the following items are typically considered to be unique to a process, but not unique to a thread? ##
  * CPU registers
  * page table pointer
  * stack pointer
  * open files
  * segment table
  * child processes
  * program counter

## Which of the following are true statements about user-level threads versus kernel-level threads? ##
  * Invoking any system call that might block poses an extra problem for user-level threads
  * User level threads are more vulnerable to priority inversion than kernel-level threads
  * There is less overall scheduling overhead in a user-level thread system
  * User level threads retain advantages on symmetric multiprocessors
  * Upcalls are necessary to implement user-level threads. (An upcall is a notification, provided by the kernel to the user-level thread run-time system, that a thread has blocked.)

# Two: CPU Efficiency #
Measurements of a certain system have shown that the average process runs for a time T before blocking on I/O. A process switch requires time S, which is effectively wasted (over-head). For round-robin scheduling with quantum Q, give a formula for the CPU efficiency for each of the following.
  * Q = infinity
  * Q > T
  * S < Q < T
  * Q = S
  * Q nearly 0

# Three: Semaphores #
Suppose we have two threads Ta and Tb that we would like to wait for each other at a certain point in their execution

### Thread Ta ###
```
statement a1
rendezvous_a()
statement a2
```
### Thread Tb ###
```
statement b1
rendezvous_b()
statement b2
```

Here, we want Ta not to execute a2 until Tb has executed b1 and we want Tb not to execute b2 until Ta has executed a1. That is, we want the threads to "rendezvous" by calling rendezvous\_a() and rendezvous\_b().

Give a semaphore-based solution for rendezvous\_a() and rendezvous\_b(). Declare any variables you might need, along with their initial values. Make sure that deadlock is not possible in your solution.

# Four: Deadlock #
Consider the following program with two concurrent processes foo and bar:

```
int x = 0, y = 0, z = 0;
sem lock1 = 1, lock2 = 1;

process foo {
  z = z + 2;
  P(lock1);
  x = x + 2;
  P(lock2);
  V(lock1);
  y = y + 2;
  V(lock2);
}

process bar {
  P(lock2);
  y = y + 1;
  P(lock1);
  x = x + 1;
  V(lock1);
  V(lock2);
  z = z + 1;
}
```

Here the variables lock1 and lock2 are semaphores and the P() and V() functions are the associated "down" and "up" operations, respectively.

  * How might this program deadlock? You should demonstrate that the conditions you list specifically meet all of the conditions required for deadlock to occur.
  * Can the program deadlock in more than one state?
  * What are the possible final values of x, y, and z in the deadlock state? If the program can deadlock in more than one state, please specify which state results in the final values you give.
  * What are the possible final values of x, y, and z if the program terminates?

# Five: Virtual Memory #
Consider a system that uses 32-bit address and 3-level page table. Among the 32-bit virtual addresses, 4 bits are used to index into the first-level page table, 8 bits for the second-level, and another 8 bits for the third-level.
  * What is the page size of this system?
  * If a page table entry is 2 bytes long, what is the size of the second-level page table?
  * Give reasons why the page size in a virtual memory system should neither be too large or too small.
  * What is a translation lookaside buffer (TLB) and what does it do?

# Six: Caches #
Consider a program that accesses pages in the following order:
```
1,3,4,1,2,6,1,1,3,2,4,5,4,2,3,2,4
```

Assuming no pages are in memory when the program starts, show how many page faults will occur when using the following replacement algorithms and number of frames.
  * LRU, one frame
  * FIFO, one frame
  * LRU, three frames
  * FIFO, three frames

# Seven: Where's the Bottleneck? #
While running a job, the CPU utilization ratio is 15%, the paging-disk utilization is 90%, and the network is used at 40% of its capacity. Please identify which of the following may improve the overall throughput of the program and explain why.
  * Install a faster CPU
  * Double the size of the memory
  * Double the network bandwidth
  * Double the size of the disk
  * Upgrade the paging algorithm to include pre-fetching
  * Increase the page size

# Eight: Filesystems #
Consider a "standard" UNIX filesystem (with i-nodes, indirect blocks, etc). Assume that the file block cache is initially empty, and that the i-node cache initially contains the current working directory. Assume "bar" exists in the current working directory.

Suppose a program executes the following sequence of instructions.
```
fd = Open("bar"); // open the file
Seek(fd,0); // seek to beginning of file
Write(fd, "A", 1); // write one byte
Close(fd); // close the file
```

Reading or writing one block or i-node requires 1 disk access.
  * What is the minimum number of disk accesses that this sequence of instructions could possibly require? If it is not possible to give an exact value, explain why and indicate what additional information is needed.
  * What is the maximum number of disk accesses that this sequence of instructions could possibly require? If it is not possible to give an exact value, explain why and indicate what additional information is needed.

# Nine: System  Calls #
To access an operating system service, a user process must make a system call. In a user program, the interface presented by a system call is a library procedure with the same name as the system call, eg, read(), which is prototyped as follows:
```
ssize_t read(int fd, void *buf, size_t count);
```

  * An operating system exists to provide a number of services and functions to users. What needs are met by having system calls?
  * What are the functional differences between a system call and a normal (non-system) function call? IE, what things must you do with a system call (and why) that you can't do with a normal function call?
  * What are the operational differences between a system call and a normal (non-system) function call? IE, what are some differences in how they are implemented?
  * What are the precise series of steps performed when a system call is invoked? If you like, you may illustrate your answer using the read() system call shown above (or you can use a system call of your choice).