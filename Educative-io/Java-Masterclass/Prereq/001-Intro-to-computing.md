# Introduction to Computing

In this lesson, we will learn the basic architecture of a computer that we will need in our study of Java.

## What is a Computer?

Before we can really talk about Java, we need to introduce some terminology. Sometimes when people speak of computers, they really mean a **computing system**: the computer itself, or **hardware**, and the programs, or **software**, necessary to perform desired tasks. Discussing each aspect separately is somewhat difficult, as they are so interrelated. A computer can do nothing useful without a program, and a program by itself is like an ignored list of directions.

Even so, we begin with a description of the computer as a machine. The hardware of a computing system includes not only the computer but also peripheral components such as:

- Printers
- Displays, and
- Scanners

We will treat these peripherals as a part of the computer.

## What Can a Computer Do?

Computers can perform astounding tasks, or so it seems. Actually, any major task is the result of many simple, basic operations. Just how rudimentary these operations are may surprise you! For example, a computer can:

- Get data from the outside world via a keyboard, a mouse, a disc, a scanner, the Internet, and so on.
- Save data, either temporarily or more permanently.
- Retrieve data that has been saved.
- Add, subtract, multiply, or divide two numbers.
- Compare two values to see whether one is less than, greater than, or equal to another.
- Manipulate data by either breaking it into pieces, joining it to other data, or moving it around.
- Display numbers, words, and other marks on a screen or on paper in various colors.

By performing these simple operations with great speed and accuracy, a computer can achieve impressive results.

## The Components of a Typical Computer

A typical computer has these major components, as the figure given below illustrates:

- Memory
- Input and output system
- Central processing unit

The connections between the various components are collectively called a **bus**.

![[Pasted image 20250715104128.png]]

The components of a typical computer

### Memory

A computer has two kinds of memory, primary and secondary. It can access its primary memory faster than its secondary memory. However, primary memory is usually more expensive than secondary memory, and so computers have less of it.

- **Primary memory**—also known as **random access memory** (**RAM**) or **internal memory**—is where a computer stores both its instructions and the data on which the instructions operate.
    
    - Primary memory is **volatile**, and whatever is stored therein is lost when electrical power is turned off.
- **Secondary memory**, or **secondary storage**, is **nonvolatile**: It does not lose its data without electricity.
    
    - Secondary memory can be on external electromechanical devices, such as hard disks, which are a part of the computer’s input/output system.
    - Secondary memory can also be internal **solid-state storage**. Possibilities include nonvolatile **flash memory** and random access memory with a battery to maintain its contents.

### The Input and Output System

A computer can communicate with us—under the control of a program— via its **input and output system**. This system includes various **input devices**—such as a keyboard and mouse—and **output devices**, such as a display and a printer. Various disk drives can be both input devices and output devices, as can network cards and modems that enable computers to communicate with one another via the Internet. Input and output devices connect to the bus via **adapters** that make the devices appear similar to the CPU by accommodating their differing characteristics.

### The Central Processing Unit

The **central processing unit**, or **CPU**, decodes and executes the instructions of a program stored in memory. These instructions direct the CPU to perform arithmetic, make comparisons, and perform other similar tasks. The CPU can move data from one memory location to another. It can direct data from memory to an output device and from an input device to memory. In these ways, the CPU manipulates data in memory according to the instructions in a program. In a sense, the CPU is the heart—or brain—of the machine.

Ordinarily, the CPU executes instructions sequentially in the order in which they appear in memory. Certain instructions, however, can direct the CPU to alter the order of execution by repeating or skipping other instructions. We will learn how to design the logic of a program, and in doing so to determine the conditions that will affect the order in which the CPU will execute instructions.

Although input and output devices do not communicate directly with the computer’s primary memory, they ultimately transfer data either to it or from it, as the figure given below illustrates, as a result of an instruction executed within the CPU.

![[Pasted image 20250715111247.png]]

Data is transferred from an input device to a computer’s memory, or from a computer’s memory to an output device

If we type data at a keyboard for a program to read, the data is placed into memory. This data is the program’s **input**. If a program displays data for us, the data first must be in memory. Anything that a program displays is called its **output**.

### More about Primary Memory

For our purposes, some knowledge of a computer’s primary memory will be helpful. This memory is a collection of locations called **bytes**. Each byte:

- Contains a value known as its **contents**
- Has a fixed numeric name called an **address** that is fixed by the designer of the computer.

We cannot change the address of a particular byte, but we can change its contents. Thus, our program can refer to a specific byte by its address and then look at or change its contents.

We can make an analogy between bytes and mailboxes in a post office: Each box number (the address) is fixed, but the contents of the box can change. However, unlike a mailbox, a byte can contain only a single piece of data at a time; placing new data into a byte destroys the old data.

Both the contents and address of a byte are represented by a sequence of binary values. Each value is produced by a physical component that can be in one of two states, such as on or off, magnetized or not magnetized, and so on. Such components are usually easier and cheaper to make than those having more than two states each. We typically denote the two states using the binary digits 0 and 1. Binary digits are commonly called **bits**.

A byte contains eight bits. For example, we might represent the contents of a particular byte as the binary numeral 10011100. This sequence of bits represents a **binary number**. Groups of consecutive bytes can represent longer binary numerals. Such groups can be two, four, eight, or more bytes long.

#### How Many Bits in a given Number of Bytes?

The address of a byte is typically 16, 32, or even 64 bits long. Having more bits enables an address to be longer, and thus the computer’s memory can be larger because it can have more bytes. Addresses begin at zero and are assigned to the bytes consecutively, as shown in the figure given below.

![[Pasted image 20250715111459.png]]

> [!NOTE]
> 📝 **Note: The decimal equivalent of a binary integer**
> 
> Each bit in a binary numeral has a value that is determined by its position within the numeral. This value is analogous to the value of a digit within a decimal numeral. For example, the decimal numeral `4321` represents four thousand, three hundred, and twenty-one: The `4` represents `4000`, the `3` represents `300`, the `2` represents `20`, and the `1` represents `1`. The sum of `4000`, `300`, `20`, and `1` is `4321`.
> 
> Another way to write 4321 is:  
> $4 \times 1000 + 3 \times 100 + 2 \times 10 + 1$  
> But by convention, we reverse the order of the terms and write the sum this way:  
> $1 + 2 \times 10 + 3 \times 100 + 4 \times 1000$
> 
> which is:  
> $1 \times 10^0 + 2 \times 10^1 + 3 \times 10^2 + 4 \times 10^3$
> 
> Analogously, the binary numeral `10111` represents the decimal computation:  
> $1 \times 2^0 + 1 \times 2^1 + 1 \times 2^2 + 0 \times 2^3 + 1 \times 2^4$
> 
> which is:  
> $1 \times 1 + 1 \times 2 + 1 \times 4 + 0 \times 8 + 1 \times 16$
> 
> or `23` in decimal. While decimal numerals use a **base** `10` notation, binary numerals use a base `2` notation.
> 
> Although the eight bits in a byte permit a rather small range of values, we can group consecutive bytes to represent larger quantities. For numeric values, Java uses groupings of two, four, and eight bytes.

## Instructions

A computer’s primary memory contains not only data but also the instructions that enable the computer to perform its task. These instructions reside in consecutive bytes of memory and are in a numeric form called **machine instructions**. In general, each kind of computer has its own unique instruction set or **machine language**, that is defined by its designers. Whether we write a program in Java or another programming language, the computer ultimately understands only a machine-language version of the program, as we will see.

> [!NOTE]
> 📝 **Aside: Some history of the stored program concept**
> 
> The IBM Automatic Sequence Controlled Calculator, also called the Harvard Mark I, was the first automatic digital computer. Completed in 1944, it was the result of a collaboration between Howard Aiken of Harvard University and IBM. The Mark I followed instructions that were punched onto a paper tape; a program was not stored internally within the machine. Calculations were carried out electromagnetically using relays, which are mechanical switches activated by electromagnets.
> 
> At about the same time that Aiken was building his computer, John Atanasoff of Iowa State University designed and built the first electronic digital computer. Using Atanasoff’s ideas, J. Presper Eckert and John Mauchly of the University of Pennsylvania completed the ENIAC in 1946. The ENIAC was the first large general-purpose electronic computer. Although these machines did not depend upon mechanical devices to perform their calculations, they were programmed by plugging wires into special boards and by setting thousands of switches.
> 
> While work on the ENIAC progressed, Mauchly and Eckert, along with John von Neumann of Princeton University, proposed the **stored program concept**, whereby a computer’s memory would contain both the program and the data to be manipulated. This concept—also known as the **von Neumann architecture**—was a significant advance in the development of computers and remains fundamental to all present-day computers.

In the late 1940s, programmers actually wrote programs only in machine language. This process was both tedious and error-prone and produced programs that were difficult for humans to read and understand. The mid-1950s saw the development of **high-level languages** that focused on problem-solving and not on a particular machine language. Today’s programming languages are still called high-level languages, even though they are more powerful than the languages of more than half a century ago. Rather than writing the numeric instructions of a machine language, programmers can write symbolic statements in a high-level language. These statements have more immediate meaning to humans and thus are easier to write, read, and understand. Moreover, one statement in a high-level language generally represents several machine-language instructions.

A program written in a high-level language—called a **source program**—must be translated into the machine language of a specific computer before it can execute, or **run**. Another program performs this translation:

- A **compiler** is one such program; it translates an entire high-level language program into machine language. We then run the resulting machine language in a separate step.
- An **interpreter**, on the other hand, translates a statement written in a high-level language into machine language and then immediately executes it, alternating between translation and execution.

As we will see, Java programs are typically compiled.

> [!note] 
> The statements in a program are sometimes called **code**, regardless of the programming language. **Coding**, then, is a synonym for programming.

Have you ever used a computer to play a video game or write an essay? For each of these endeavors, you actually used an **application program**, or simply an **application**. You are about to use Java to write your own applications. To be able to use any application, your computer needs an operating system. An **operating system** is a set of programs that provides services that enable you to use a computer. For all practical purposes, an operating system is an essential part of a computing system. Current systems—such as Windows, macOS, UNIX, and Linux—provide an environment in which you can work. For example, operating systems enable you to:

- Save files
- Organize files into folders or directories
- Use applications
- Connect to the Internet

We will assume that you have some basic knowledge of the operating system that is available to you.