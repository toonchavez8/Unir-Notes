# Data Types

In this lesson, we will explore how to specify the data type a Java program uses.

## Why do we need data types?[](https://www.educative.io/courses/java-masterclass-developers/data-types#Why-do-we-need-data-types)

Computers process various kinds of data. For example, an application might use numbers that contain a decimal point, integers, individual characters, and strings. The Java compiler needs to know what kind of data it is working with, and so the programmer needs to specify a **data type**. For example, we would use the data type

- `int` for integers
- `char` for characters
- `String` for strings

As we will see, Java’s data types are organized into two categories

- Primitive types
- Reference types

Because the [first program](https://www.educative.io/courses/java-masterclass-developers/a-simple-java-program#program-display-text) we showed you earlier is so simple, we will look at other Java examples as we discuss the topics in this lesson.

## Primitive types[#](https://www.educative.io/courses/java-masterclass-developers/data-types#Primitive-types)

Individual numbers, characters, and Boolean values (true or false) have **primitive data types** because they are not objects in Java. The names of these types are reserved words made up of lowercase letters. For example, integers can have the data type `int`. An integer has no decimal point. Real, or **floating-point**, numbers contain a decimal point and can have the data type `double`. Individual characters—letters, digits, and punctuation—have the data type `char`. Data of type `boolean` has only two values, `true` or `false`.

> 📝 **Note**
> 
> The data types of integers, real numbers, characters, and Booleans are said to be primitive. Data that has a primitive type has a single value.
> 
> The types `int`, `double`, `char`, and `boolean` are the primitive types that we typically will use in this course. But Java has several other primitive types for integers and real numbers. The choice affects the range of numbers available and the amount of computer memory needed to represent them. Thus, an integer can have one of the types `byte`, `short`, `int`, or `long`. A `byte` integer has the smallest range and uses the least memory. A `long` integer has the largest range and uses the most memory. Similarly, a real number can have one of the types `float` or `double`. A `double` number can contain more digits—and so is more precise—than a `float` number.
> 
> The figure given below lists the available primitive types and shows their sizes as well as the ranges of their values.

![[Pasted image 20250919165133.png]]

## Reference types[](https://www.educative.io/courses/java-masterclass-developers/data-types#Reference-types)

As we just saw, data with a primitive type has a single value. Other data types, known as **reference types**, are more complex. For example, an object may have one or more pieces of data, as well as methods that work with that data. An object’s data type is a **class type**, which is a kind of reference type. A string is an example of an object. Its data type is `String` that is the name of a class in the Java Class Library that is provided with Java. Java has other reference types that we will encounter later in this course. For the moment, you need not worry about reference types, as we will concentrate on primitive types.