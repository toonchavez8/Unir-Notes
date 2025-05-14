# CSS Preprocessors

## Objectives

- Introduction to CSS preprocessors: Learn what CSS preprocessors are, understand their benefits, and how they enhance traditional CSS capabilities.
- Core features: Explore key features like variables, which allow for more maintainable code by avoiding repetition, and `mixins`, which enable reusable styles that can be included in multiple CSS rules.
- Advanced nesting: Understand advanced nesting techniques for writing cleaner and more structured stylesheets. Learn how nesting rules within each other corresponds to the HTML structure.

## Reading

### [What are CSS preprocessors](https://www.geeksforgeeks.org/what-is-a-css-preprocessors/)

CSS preprocessors are used to write styles in a special syntax that is then compiled insto started CSS. They extend standard CSS by including variables nesting, `mixins` and functions. 

#### Benefits of CSS Preprocessors

1. ****Code Reusability****: Preprocessors allow you to reuse code through `mixins` and functions, making stylesheets easier to maintain.
2. ****Enhanced Readability and Organization****: Nesting allows you to write styles in a way that mirrors the structure of your HTML, which improves readability.
3. ****Easier Maintenance****: Using variables for common values (e.g., colors, fonts) makes updating styles across a project simple.
4. ****Modular Code Structure****: You can split your stylesheets into smaller files and import them into a main stylesheet, promoting a modular approach.

#### Popular Preprocessors

#### Sass

[Sass](https://www.geeksforgeeks.org/sass) is one of the most widely used CSS preprocessors. It adds features such as variables, nesting, `mixins`, and functions, which help in writing clean and organized styles.

- ***Syntax: Sass has two syntaxes:*** the original ****.sass syntax****, which is indentation-based, and ****.sCSS (Sassy CSS)****, which uses a syntax similar to regular CSS.
- **Variables:*** Store reusable values.
- **Nesting:*** Nest CSS rules to mimic HTML structure.
- **Mixins and Functions***: Create reusable blocks of styles.
- **Control Directives:***: Use programming concepts like loops and conditionals.

#### Less

[LESS](https://www.geeksforgeeks.org/css-preprocessor-less) CSS is a backward-compatible language extension for CSS. Features include variables, nesting, and `mixins`. It is developed to be similar to Sass but with a simpler syntax.

- ****Variables****: Defined with the @ symbol.
- ****Nesting****: Similar to Sass, allowing styles to be nested.
- ****Mixins****: Include groups of CSS properties.
- ****Operations****: Perform calculations directly in your stylesheets.

#### Stylus

Stylus is a preprocessor that aims to be more flexible and feature-rich. Syntax is minimalistic and indentation-based. It also supports variables, nesting, and a wide range of functions.

- ****Flexible Syntax:**** Can be written with or without braces and semicolons.
- ****Powerful Functions:**** Supports complex functions for style manipulation.
- ****Conditionals and Loops:**** Allows for advanced programming logic.

#### PostCSS

Unlike Sass or LESS, [PostCSS](https://www.geeksforgeeks.org/difference-between-css-variables-and-preprocessor) is not a preprocessor but a tool for transforming CSS using plugins. It can be extended with various plugins for linting, autoprefixing, and more.Offers a modular and customizable approach to enhancing CSS.

- ****Modular Approach****: Use plugins for tasks like linting, autoprefixing, and minification.
- ****Customizable****: Create your own plugins for specific tasks.
- ****Widely Used****: Many modern build tools (e.g., Webpack) support PostCSS.

#### SCSS

[SCSS](https://www.geeksforgeeks.org/how-do-you-create-application-to-use-scss) is an extension of Sass that uses a CSS-like syntax. It maintains compatibility with CSS syntax, making it easier for CSS developers to transition to SCSS.

- ****Backwards Compatibility****: Supports all features of CSS.
- ****Advanced Features****: Offers variables, `mixins`, inheritance, and functions.
- ****Readable Syntax****: Familiar to CSS developers.

#### Comparison of Preprocesors

| Feature                  | Sass/SCSS   | LESS    | Stylus  | PostCSS           |
| ------------------------ | ----------- | ------- | ------- | ----------------- |
| **Variables***           | Yes         | Yes     | Yes     | Plugin-based      |
| **Nesting***             | Yes         | Yes     | Yes     | Plugin-based      |
| ***Mixins***             | Yes         | Yes     | Yes     | Plugin-based      |
| **Functions***           | Yes         | Yes     | Yes     | Plugin-based      |
| ***Syntax Flexibility*** | .scss/.sass | .less   | .styl   | N/A               |
| ***Extensibility***      | Limited     | Limited | Limited | Highly Extensible |

### [[001_Sass_Basics]]


## Watch Section

### Nesting

Rules inside of others rules is known as nesting

- Combine rules
- Can cause Extra CSS
- Nested css may cause extra bandwidth

### Partials

Snpippts of code that can easily be imported into other files are known as partials

- Genreally a partial will be named with underscore like `_partial.sCSS`
- To use it can import it as `@use "partial"`
- Scss will automaitly convert it and use it where you call it 
- We can Namespace our variables
	- Using as we can change the variable name like 
	- `@use "partial" as part`
	- To reference it we would use it as such
		- `color:part.$variable`

### Parent Selector

The parent selector lets you easily select the parent using the `&` 

It copies the parent and insert into a new style

We can use it create a suffix like below and it will create a new class called `btn-primary`

```sCSS
.btn{
	&-primary{}
}
```

We can also use it to target a parent present the code below will target a `.container .btn`

```sCSS
.btn{
	.container &{}
}
```

### Mixins

Sass lets us create mixins which are like functions within sass

- Create with `@Mixin`
- We can pass arguments or parameters
- We can set defaults
- We to use them we muse `@include`

example

```sCSS
@mixin btn($var:#defaultValue){
	border: $var
}

.container{
	@include btn(#newVal)
}
```

### Extend

We can use Extend to create classes with erilier rules

- Using `@extend` we create a sort of template or starting point for a new class