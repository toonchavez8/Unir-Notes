# CSS Layout Basics

## Objectives

- Understanding normal flow: Grasp the concept of normal flow, the default layout mechanism where block elements stack vertically and inline elements align horizontally.
- Manipulating layout with display: Explore how the display property modifies an element's default display style, influencing layout behaviors and structure. Understand different display values such as `block`, `inline`, `inline-block`, `flex`, and `grid`.
- Floating elements: Learn about the `float` property, which allows elements to be pulled to the left or right, causing surrounding inline content to wrap around them. Study techniques for managing this property effectively, including clearing floats.
- Positioning elements: Dive into the position property to understand how elements can be explicitly positioned on the page using values like `static`, `relative`, `absolute`, and `fixed`.

## Read

### [CSS layout: introduction](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Introduction)

#### Learning Outcomes

- Recognize the methods used to implement modern page layouts.
- Understand that normal flow is the default way a browser lays out block and inline Contents
- Know that properties such as `display`, `float`, and `position` are intended to change how the browser lays out content. 

#### Normal Layout Flow

Elements on a webpage lay out in **normal flow** if you haven't applied any CSS to change the way they behave.You can change how elements behave either by adjusting their position in normal flow or by removing them from it altogether.

Starting with a solid, well-structured document that's readable in normal flow is the best way to begin any webpage. It ensures that your content is readable even if the user's using a very limited browser or a device such as a screen reader that reads out the content of the page

#### How Are Elements Laid out by Default

The process begins as the boxes of individual elements are laid out in such a way that any padding, border, or margin they happen to have is added to their content. This is what we call the **box model**.

By default, a [block-level element](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content) 's content fills the available inline space of the parent element containing it, growing along the block dimension to accommodate its content. The size of [inline-level elements](https://developer.mozilla.org/en-US/docs/Glossary/Inline-level_content) is just the size of their content. You can set [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/width) or [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/height) on some elements that have a default [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/display) property value of `inline`, like [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img), but the `display` value will still remain `inline`.

If you want to control the `display` property of an inline-level element in this manner, use CSS to set it to behave like a block-level element (e.g., with `display: block;` or `display: inline-block;`, which mixes characteristics from both).

The normal layout flow (mentioned in the layout introduction article) is the system by which elements are placed inside the browser's viewport. By default, block-level elements are laid out in the _block flow direction_, which is based on the parent's [writing mode](https://developer.mozilla.org/en-US/docs/Web/CSS/writing-mode) (_initial_: horizontal-tb). Each element will appear on a new line below the last one, with each one separated by whatever margin that's been specified. In English, for example, (or any other horizontal, top to bottom writing mode) block-level elements are laid out vertically.

Inline elements behave differently. They don't appear on new lines; instead, they all sit on the same line along with any adjacent (or wrapped) text content as long as there is space for them to do so inside the width of the parent block level element. If there isn't space, then the overflowing content will move down to a new line

If two vertically adjacent elements both have a margin set on them and their margins touch, the larger of the two margins remains and the smaller one disappears. This is known as [**margin collapsing**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_box_model/Mastering_margin_collapsing). Collapsing margins is only relevant in the **vertical direction**.

##### Normal Flow Example

Let's look at a simple example that explains all of this:

```html
<h1>Basic document flow</h1>

<p>
  I am a basic block level element. My adjacent block level elements sit on new
  lines below me.
</p>

<p>
  By default we span 100% of the width of our parent element, and we are as tall
  as our child content. Our total width and height is our content + padding +
  border width/height.
</p>

<p>
  We are separated by our margins. Because of margin collapsing, we are
  separated by the size of one of our margins, not both.
</p>

<p>
  Inline elements <span>like this one</span> and <span>this one</span> sit on
  the same line along with adjacent text nodes, if there is space on the same
  line. Overflowing inline elements will
  <span>wrap onto a new line if possible (like this one containing text)</span>,
  or just go on to a new line if not, much like this image will do:
  <img
    src="https://mdn.github.io/shared-assets/images/examples/long.jpg"
    alt="snippet of cloth" />
</p>

```

![[Pasted image 20250519202933.png]]

Note how the HTML is displayed in the exact order in which it appears in the source code, with block elements stacked on top of one another

For many of the elements on your page, the normal flow will create exactly the layout you need. However, for more complex layouts you will need to alter this default behavior using some of the tools available to you in CSS. Starting with a well-structured HTML document is very important because you can then work with the way things are laid out by default rather than fighting against it.

#### Overriding Normal Flow

The methods that can override normal flow and change how elements are laid out in CSS, which we will cover in detail in this module, are:

The [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/display) property

Standard values such as `block`, `inline` or `inline-block` can change how elements behave in normal flow, for example, by making a block-level element behave like an inline-level element (we covered these back in the [Box model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model#block_and_inline_boxes) lesson).

[Floats](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Introduction#floats)

Applying a [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/float) value such as `left` can cause block-level elements to wrap along one side of an element, like the way images sometimes have text floating around them in magazine layouts.

[Positioning](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Introduction#positioning)

The [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/position) property allows you to precisely control the placement of boxes inside other boxes. `static` positioning is the default in normal flow, but you can cause elements to be laid out differently using other values, for example, fixing them to the top of the browser viewport using `position: fixed`.

[Specific layout systems accessed through `display`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Introduction#specific_layout_systems_accessed_through_display)

We also have entire layout methods that are enabled via specific `display` values. The most important ones for you to know about are [CSS grid](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Grids) and [Flexbox](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox), which both alter how child elements are laid out inside their parents.

[Responsive design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Introduction#responsive_design)

Responsive design refers to creating layouts that adapt to different devices the web page is rendered on (for example, desktops and mobile phones). Responsive design doesn't provide any specific layout tools of its own; its most significant component is the [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media) at-rule, which allows you to apply different layouts depending on device attributes such as screen width or resolution.

#### Other Layouts

There are other layout techniques that are less commonly used, which we won't cover in this module:

[Table layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_table)

Features designed for styling parts of an HTML table can be used on non-table elements using `display: table` and associated properties.

[Multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_multicol_layout)

The multi-column layout properties can cause the content of a block to lay out in columns, as you might see in a newspaper.

### [Block and inline layout in normal flow](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flow_layout/Block_and_inline_layout_in_normal_flow)

Normal Flow is defined in the [CSS 2.1 specification](https://www.w3.org/TR/CSS2/visuren.html#normal-flow), which explains that any boxes in normal flow will be part of a _formatting context_. They can be either block or inline, but not both at once. We describe block-level boxes as participating in a _block formatting context_, and inline-level boxes as participating in an _inline formatting context_.

The behavior of elements which have a block or inline formatting context is also defined in this specification. For elements with a block formatting context, the spec says:

> "In a block formatting context, boxes are laid out one after the other, vertically, beginning at the top of a containing block. The vertical distance between two sibling boxes is determined by the 'margin' properties. Vertical margins between adjacent block-level boxes in a block formatting context collapse. In a block formatting context, each box's left outer edge touches the left edge of the containing block (for right-to-left formatting, right edges touch)." - 9.4.1

For elements with an inline formatting context:

> "In an inline formatting context, boxes are laid out horizontally, one after the other, beginning at the top of a containing block. Horizontal margins, borders, and padding are respected between these boxes. The boxes may be aligned vertically in different ways: their bottoms or tops may be aligned, or the baselines of text within them may be aligned. The rectangular area that contains the boxes that form a line is called a line box." - 9.4.2

#### Elements Participating in a Block Formatting Context

Block elements in a horizontal writing mode such as English, lay out vertically, one below the other.

![[Pasted image 20250519210205.png]]

In a vertical writing mode then would lay out horizontally.

![[Pasted image 20250519210144.png]]

As defined in the specification, the margins between two block boxes are what creates separation between the elements. We can see this with the layout of two paragraphs, to which I have added a border. The default browser stylesheet adds spacing between the paragraphs by way of adding a margin to the top and bottom.

```HTML
<div class="box">
  <p>
    One November night in the year 1782, so the story runs, two brothers sat
    over their winter fire in the little French town of Annonay, watching the
    grey smoke-wreaths from the hearth curl up the wide chimney. Their names
    were Stephen and Joseph Montgolfier, they were papermakers by trade, and
    were noted as possessing thoughtful minds and a deep interest in all
    scientific knowledge and new discovery.
  </p>
  <p>
    Before that night—a memorable night, as it was to prove—hundreds of millions
    of people had watched the rising smoke-wreaths of their fires without
    drawing any special inspiration from the fact.
  </p>
</div>

```

![[Pasted image 20250519210259.png]]

By default block elements will consume all of the space in the inline direction, so our paragraphs spread out and get as big as they can inside their containing block. If we give them a width, they will continue to lay out one below the other - even if there would be space for them to be side by side. Each will start against the start edge of the containing block, so the place at which sentences would begin in that writing mode.

#### Margin Collapsing

The spec explains that margins between block elements _collapse_. This means that if you have an element with a top margin immediately after an element with a bottom margin, rather than the total space being the sum of these two margins, the margin collapses, and so will essentially become as large as the larger of the two margins.

In the example below, the paragraphs have a top margin of `20px` and a bottom margin of `40px`. The size of the margin between the paragraphs is `40px` as the smaller top margin on the second paragraph has collapsed with the larger bottom margin of the first.

```cSS
p {
  border: 2px solid green;
  margin: 20px 0 40px 0;
}

```

![[Pasted image 20250519210421.png]]

> [!note] **Note:** If you are not sure whether margins are collapsing, check the Box Model values in your browser DevTools. This will give you the actual size of the margin which can help you to identify what is happening.

#### Elements Participating in an Inline Formatting Context

Inline elements display one after the other in the direction that sentences run in that particular writing mode. While we don't tend to think of inline elements as having a box, as with everything in CSS they do. These inline boxes are arranged one after the other. If there is not enough space in the containing block for all of the boxes a box can break onto a new line. The lines created are known as line boxes.

In the following example, we have three inline boxes created by a paragraph with a [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong) element inside it.

```HTML
<p>
  Before that night—<strong>a memorable night</strong>, as it was to
  prove—hundreds of millions of people had watched the rising smoke-wreaths of
  their fires without drawing any special inspiration from the fact.
</p>

```

![[Pasted image 20250519210658.png]]

The boxes around the words before the `<strong>` element and after the `</strong>` element are referred to as anonymous boxes, boxes introduced to ensure that everything is wrapped in a box, but ones that we cannot target directly.

The line box size in the block direction (so the height when working in English) is defined by the tallest box inside it. In the next example, the `<strong>` element is 300%; since that content spans two lines, it now defines the height of the line boxes of those two lines.

```cSS
strong {
  font-size: 300%;
}

```

![[Pasted image 20250519210754.png]]

#### The Display Property and Flow Layout

The [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/display) property defines how a box and any boxes inside it behave. In the CSS Display Model Level 3, we can learn more about how the `display` property changes the behavior of boxes and the boxes they generate.

The display type of an element defines the outer display type; this dictates how the box displays alongside other elements in the same formatting context. It also defines the inner display type, which dictates how boxes inside this element behave. We can see this very clearly when considering a flex layout. In the example below I have a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div), which I have given `display: flex`. The flex container behaves like a block element: it displays on a new line and takes up all of the space it can in the inline direction. This is the outer display type of `block`.

The flex items however are participating in a flex formatting context, because their parent is the element with `display: flex`, which has an inner display type of `flex`, establishing the flex formatting context for the direct children.

```HTML
<div class="container">
  <div>Flex Item</div>
  <div>Flex Item</div>
  <div>
    <div>Children</div>
    <div>are in</div>
    <div>normal flow</div>
  </div>
</div>

```

```cSS
.container {
  display: flex;
}

.container > * {
  border: 1px solid green;
}

```

![[Pasted image 20250519210945.png]]

Therefore you can think of every box in CSS working in this way. The box itself has an outer display type, so it knows how to behave alongside other boxes. It then has an inner display type which changes the way its children behave. Those children then have an outer and inner display type too. The flex items in the previous example become flex level boxes, so their outer display type is dictated by way of them being part of the flex formatting context. They have an inner display type of _flow_ however, meaning that their children participate in normal flow. Items nested inside our flex item lay themselves out as block and inline elements unless something changes their display type.

This concept of the outer and inner display type is important as this tells us that a container using a layout method such as flexbox (`display: flex`) and grid layout (`display: grid`) is still participating in block and inline layout, due to the outer display type of those methods being `block`.

#### Changing the Formatting Context an Element Participates in

Browsers display items in block or inline formatting contexts based on what normally makes sense for that element. For example, a [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong) element is used to strongly emphasize a span of content and is displayed in bold in browsers by default. It would not generally make sense for that `<strong>` element to be displayed as a block-level element, breaking onto a new line. If you did want all `<strong>` elements to display as block boxes, you could do so by setting `strong { display: block; }`. The ability to style content with CSS means you can always use the most appropriate semantic HTML elements to mark up your content and then change how they are displayed with CSS.

```cSS
strong {
  display: block;
}

```

![[Pasted image 20250519211043.png]]

### [Floats](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Floats)

#### The Background of Floats

The float property was introduced to allow web developers to implement layouts involving an image floating inside a column of text, with the text wrapping around the left or right of it. The kind of thing you might get in a newspaper layout.

Floats have commonly been used to create entire website layouts featuring multiple columns of information floated so they sit alongside one another (the default behavior would be for the columns to sit below one another in the same order as they appear in the source). There are newer, better layout techniques available. 

> [!caution] Using floats in this way should be regarded as a legacy technique

#### A Float Example

```HTML
<h1>Float example</h1>

<div class="box">Float</div>

<p>
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus aliquam
  dolor, eu lacinia lorem placerat vulputate. Duis felis orci, pulvinar id metus
  ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies tellus
  laoreet sit amet.
</p>

<p>
  Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet
  orci vel, viverra egestas ligula. Curabitur vehicula tellus neque, ac ornare
  ex malesuada et. In vitae convallis lacus. Aliquam erat volutpat. Suspendisse
  ac imperdiet turpis. Aenean finibus sollicitudin eros pharetra congue. Duis
  ornare egestas augue ut luctus. Proin blandit quam nec lacus varius commodo et
  a urna. Ut id ornare felis, eget fermentum sapien.
</p>

<p>
  Nam vulputate diam nec tempor bibendum. Donec luctus augue eget malesuada
  ultrices. Phasellus turpis est, posuere sit amet dapibus ut, facilisis sed
  est. Nam id risus quis ante semper consectetur eget aliquam lorem. Vivamus
  tristique elit dolor, sed pretium metus suscipit vel. Mauris ultricies lectus
  sed lobortis finibus. Vivamus eu urna eget velit cursus viverra quis
  vestibulum sem. Aliquam tincidunt eget purus in interdum. Cum sociis natoque
  penatibus et magnis dis parturient montes, nascetur ridiculus mus.
</p>

```

```cSS
body {
  width: 90%;
  max-width: 900px;
  margin: 0 auto;
  font:
    0.9em/1.2 Arial,
    Helvetica,
    sans-serif;
}

.box {
  width: 150px;
  height: 100px;
  border-radius: 5px;
  background-color: rgb(207 232 220);
  padding: 1em;
}

```

#### Floating the Box

To float the box, add the [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/float) and [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-right) properties to the `.box` rule:

```cSS
.box {
  float: left;
  margin-right: 15px;
  width: 150px;
  height: 100px;
  border-radius: 5px;
  background-color: rgb(207 232 220);
  padding: 1em;
}

```

Now if you save and refresh you'll see something like the following:

![[Pasted image 20250519211539.png]]

Let's think about how the float works. The element with the float set on it (the [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div) element in this case) is taken out of the normal layout flow of the document and stuck to the left-hand side of its parent container ([`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body), in this case).

 Any content that would come below the floated element in the normal layout flow will now wrap around it instead, filling up the space to the right-hand side of it as far up as the top of the floated element. There, it will stop.

Floating the content to the right has exactly the same effect, but in reverse: the floated element will stick to the right, and the content will wrap around it to the left. Try changing the float value to `right` and replace [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-right) with [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-left) in the last ruleset to see what the result is.

##### Visualizing the Float

While we can add a margin to the float to push the text away, we can't add a margin to the text to move it away from the float. This is because a floated element is taken out of normal flow and the boxes of the following items actually run behind the float. You can see this by making some changes to your example.

Add a class of `special` to the first paragraph of text, the one immediately following the floated box, then in your CSS add the following rules. These will give our following paragraph a background col

```cSS
.special {
  background-color: rgb(148 255 172);
  padding: 10px;
  color: purple;
}

```

To make the effect easier to see, change the `margin-right` on your float to `margin` so you get space all around the float. You'll be able to see the background on the paragraph running right underneath the floated box, as in the example below.

![[Pasted image 20250519211708.png]]

We've seen that a float is removed from normal flow and that other elements will display beside it. If we want to stop the following element from moving up, we need to _clear_ it; this is achieved with the [`clear`](https://developer.mozilla.org/en-US/docs/Web/CSS/clear) property.

```cSS
.cleared {
  clear: left;
}

```

![[Pasted image 20250519211737.png]]

You should see that the second paragraph now clears the floated element and no longer comes up alongside it. The `clear` property accepts the following values:

- `left`: Clear items floated to the left.
- `right`: Clear items floated to the right.
- `both`: Clear any floated items, left or right.

### [Positioning](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning)

Positioning allows you to take elements out of normal document flow and make them behave differently, for example, sitting on top of one another or always remaining in the same place inside the browser viewport. This article explains the different [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/position) values and how to use them.

#### Introducing Positioning

Positioning allows us to produce interesting results by overriding normal document flow. What if you want to slightly alter the position of some boxes from their default flow position to give a slightly quirky, distressed feel? Positioning is your tool. Or what if you want to create a UI element that floats over the top of other parts of the page and/or always sits in the same place inside the browser window no matter how much the page is scrolled? Positioning makes such layout work possible.

There are a number of different types of positioning that you can put into effect on HTML elements. To make a specific type of positioning active on an element, we use the [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/position) property.

#### Static Positioning

Static positioning is the default that every element gets. It just means "put the element into its default position in the normal flow — nothing special to see here."

To see this (and get your example set up for future sections) first add a `class` of `positioned` to the second [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p) in the HTML:

```html
<p class="positioned">…</p>
```

Now add the following rule to the bottom of your CSS:

```css
.positioned {
  position: static;
  background: yellow;
}
```

If you save and refresh, you'll see no difference at all, except for the updated background color of the 2nd paragraph. This is fine — as we said before, static positioning is the default behavior!

#### Relative Positioning

Relative positioning is the first position type we'll take a look at. This is very similar to static positioning, except that once the positioned element has taken its place in the normal flow, you can then modify its final position, including making it overlap other elements on the page. Go ahead and update the `position` declaration in your code:

### [Introducing top, bottom, left, and right](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning#introducing_top_bottom_left_and_right)

[`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/top), [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/bottom), [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/left), and [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/right) are used alongside [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/position) to specify exactly where to move the positioned element to. To try this out, add the following declarations to the `.positioned` rule in your CSS:

```Python
top: 30px;
left: 30px;
```

> [!note] **Note:** The values of these properties can take any [units](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units) you'd reasonably expect: pixels, mm, rems, %, etc.

#### Absolute Positioning

Absolute positioning brings very different results.

##### [Setting position: absolute](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning#setting_position_absolute)

Let's try changing the position declaration in your code as follows:

```css
position: absolute;
```

First of all, note that the gap where the positioned element should be in the document flow is no longer there — the first and third elements have closed together like it no longer exists! Well, in a way, this is true. An absolutely positioned element no longer exists in the normal document flow. Instead, it sits on its own layer separate from everything else. This is very useful: it means that we can create isolated UI features that don't interfere with the layout of other elements on the page. For example, popup information boxes, control menus, rollover panels, UI features that can be dragged and dropped anywhere on the page, and so on.

##### [Positioning contexts](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning#positioning_contexts)

Which element is the "containing element" of an absolutely positioned element? This is very much dependent on the `position` property value of the ancestors of the positioned element.

If no ancestor elements have their position property explicitly defined, then by default all ancestor elements will have a static position. The result of this is the absolutely positioned element will be contained in the **initial containing block**. The initial containing block has the dimensions of the viewport and is also the block that contains the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html) element. In other words, the absolutely positioned element will be displayed outside of the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html) element and be positioned relative to the initial viewport.

The positioned element is nested inside the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body) in the HTML source, but in the final layout it's 30px away from the top and the left edges of the page. We can change the **positioning context**, that is, which element the absolutely positioned element is positioned relative to. This is done by setting positioning on one of the element's ancestors: to one of the elements it's nested inside of (you can't position it relative to an element it's not nested inside of). To see this, add the following declaration to your `body` rule:

##### [Introducing z-index](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning#introducing_z-index)

All this absolute positioning is good fun, but there's another feature we haven't considered yet. When elements start to overlap, what determines which elements appear over others and which elements appear under others? In the example we've seen so far, we only have one positioned element in the positioning context, and it appears on the top since positioned elements win over non-positioned elements. What about when we have more than one?

Try adding the following to your CSS to make the first paragraph absolutely positioned too:

At this point you'll see the first paragraph colored lime, moved out of the document flow, and positioned a bit above from where it originally was. It's also stacked below the original `.positioned` paragraph where the two overlap. This is because the `.positioned` paragraph is the second paragraph in the source order, and positioned elements later in the source order win over positioned elements earlier in the source order.

Can you change the stacking order? Yes, you can, by using the [`z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index) property. "z-index" is a reference to the z-axis. You may recall from previous points in the course where we discussed web pages using horizontal (x-axis) and vertical (y-axis) coordinates to work out positioning for things like background images and drop shadow offsets. For languages that run left to right, (0,0) is at the top left of the page (or element), and the x- and y-axes run across to the right and down the page.

Web pages also have a z-axis: an imaginary line that runs from the surface of your screen towards your face (or whatever else you like to have in front of the screen). [`z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index) values affect where positioned elements sit on that axis; positive values move them higher up the stack, negative values move them lower down the stack. By default, positioned elements all have a `z-index` of `auto`, which is effectively 0.

To change the stacking order, try adding the following declaration to your `p:nth-of-type(1)` rule:

```css
Z-index: 1;
```

> [!note] Note that `z-index` only accepts unitless index values; you can't specify that you want one element to be 23 pixels up the Z-axis — it doesn't work like that. Higher values will go above lower values and it's up to you what values you use. Using values of 2 or 3 would give the same effect as values of 300 or 40000.

#### [Fixed positioning](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning#fixed_positioning)

Let's now look at fixed positioning. This works in exactly the same way as absolute positioning, with one key difference: whereas absolute positioning fixes an element in place relative to its nearest positioned ancestor (the initial containing block if there isn't one), **fixed positioning** fixes an element in place relative to the visible portion of the viewport. This means that you can create useful UI items that are fixed in place, like persistent navigation menus that are always visible no matter how much the page scrolls.

Let's put together a simple example to show what we mean. First of all, delete the existing `p:nth-of-type(1)` and `.positioned` rules from your CSS.

Now update the `body` rule to remove the `position: relative;` declaration and add a fixed height, like so:

```css
body {
  width: 500px;
  height: 1400px;
  margin: 0 auto;
}
```

Now we're going to give the `<h1>` element ` position: fixed; ` and have it sit at the top of the viewport. Add the following rule to your CSS:

```css
h1 {
  position: fixed;
  top: 0;
  width: 500px;
  margin-top: 0;
  background: white;
  padding: 10px;
}
```

The `top: 0;` is required to make it stick to the top of the screen. We give the heading the same width as the content column and then a white background and some padding and margin so the content won't be visible underneath it.

If you save and refresh, you'll see a fun little effect of the heading staying fixed — the content appears to scroll up and disappear underneath it. But notice how some of the content is initially clipped under the heading. This is because the positioned heading no longer appears in the document flow, so the rest of the content moves up to the top. We could improve this by moving the paragraphs all down a bit. We can do this by setting some top margin on the first paragraph. Add this now:

```css
p:nth-of-type(1) {
  margin-top: 60px;
}
```

##### [Sticky positioning](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning#sticky_positioning)

There is another position value available called `position: sticky`, which is somewhat newer than the others. This is basically a hybrid between relative and fixed position. It allows a positioned element to act like it's relatively positioned until it's scrolled to a certain threshold (e.g., 10px from the top of the viewport), after which it becomes fixed.

### [Basic example](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning#basic_example)

Sticky positioning can be used, for example, to cause a navigation bar to scroll with the page until a certain point and then stick to the top of the page.

cssCopy to Clipboardplay

```css
.positioned {
  position: sticky;
  top: 30px;
  left: 30px;
}
```

### [Scrolling index](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning#scrolling_index)

An interesting and common use of `position: sticky` is to create a scrolling index page where different headings stick to the top of the page as they reach it. The markup for such an example might look like so

The CSS might look as follows. In normal flow the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt) elements will scroll with the content. When we add `position: sticky` to the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt) element, along with a [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/top) value of 0, supporting browsers will stick the headings to the top of the viewport as they reach that position. Each subsequent header will then replace the previous one as it scrolls up to that position

```css
Dt {
  Background-color: black;
  Color: white;
  Padding: 10 px;
  Position: sticky;
  Top: 0;
  Left: 0;
  Margin: 1 em 0;
}
```