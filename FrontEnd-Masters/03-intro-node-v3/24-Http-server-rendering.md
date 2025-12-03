# **Study Notes: Building an HTTP Server That Renders Dynamic HTML**

---

# 1. **Overview: Server-Side Rendering with Node.js**

The goal is to build a simple server that:

- Reads an HTML template file.
    
- Injects (interpolates) dynamic data into that template.
    
- Sends the final HTML to the browser.
    
- Opens the browser automatically.
    
- Uses foundational Node.js modules instead of frameworks (e.g., Express).

This demonstrates **server-side rendering (SSR)** without external libraries.

---

# 2. **Creating The Server**

## 2.1 Purpose of `createServer`

`createServer` is a function that:

- Receives a list of notes from the caller.
    
- Returns an HTTP server created via `http.createServer()`.
    
- Handles requests asynchronously because it must read files.

### Key Concepts

|Concept|Definition|
|---|---|
|**HTTP server**|A process that listens for requests and returns responses.|
|**Request/Response objects**|Interfaces used to read incoming data and send outgoing content.|
|**Async handler**|Required because file reads are asynchronous.|

---

# 3. **Loading And Preparing the HTML Template**

## 3.1 Getting the Template Path

A `URL` object is used to locate the HTML file relative to the module:

```js
const HTML_PATH = new URL("./template.html", import.meta.url);
```

### Important Note for Windows

`pathname` can break paths on Windows.  
Use the `URL` object directly instead of `.pathname`.

---

## 3.2 Reading the Template

```js
const template = await fs.readFile(HTML_PATH, "utf-8");
```

- Reading with `"utf-8"` ensures the result is a string.
    
- Without encoding, Node returns a buffer.

---

## 3.3 Interpolating the Template

Interpolation replaces placeholders (like `{{ notes }}`) with actual content.

```js
const html = interpolate(template, {
  notes: formatNotes(notes)
});
```

### Mermaid: Template Rendering Pipeline

```mermaid
flowchart LR
  A[Load Notes JSON] --> B[Format Notes as HTML]
  B --> C[Load Template.html]
  C --> D["Interpolate {{notes}} Placeholder"]
  D --> E[Send Final HTML to Browser]
```

---

# 4. **Sending The Response**

## 4.1 Setting Headers (writeHead)

```js
res.writeHead(200, { "Content-Type": "text/html" });
```

- **Status 200** → request succeeded.
    
- **Content-Type: text/html** → ensures browser parses HTML.

## 4.2 Sending the Final HTML

```js
res.end(html);
```

`res.end()` terminates the response and transmits the content.

---

# 5. **Starting The Server**

## 5.1 Creating a Start Function

A wrapper function encapsulates server initialization:

```js
function start(notes, port) {
  const server = createServer(notes);
  server.listen(port);
  open(address);
}
```

### Responsibilities of `start()`

|Step|Description|
|---|---|
|Create server|`createServer(notes)`|
|Listen to port|Keep server available on given port|
|Display address|For debugging|
|Open browser|Automatically load website|

---

## 5.2 Exporting the Start Function

```js
export { start };
```

- Only exported functions can be used or tested in other files.
    
- Non-exported functions become module-private.

---

# 6. **Wiring Up the CLI Command**

The CLI command named `web`:

- Accepts a `port` positional argument (default 5000).
    
- Fetches all notes via `getAllNotes()`.
    
- Starts the server and passes both values.

```js
const notes = await getAllNotes();
start(notes, argv.port);
```

---

# 7. **Testing The Server**

## 7.1 Case: Empty Notes

If there are no notes, the template renders but shows nothing.

## 7.2 Adding Notes

Use the CLI:

```Python
notes new "clean my room"
```

After adding notes, restarting the server renders them correctly.

---

# 8. **Understanding The Result: Server-Side Rendering**

This process results in:

- Rendering dynamic HTML **on the server**.
    
- Sending the finished HTML to the browser.
    
- Similar principle used by server-rendered React (SSR).

## Key Idea

**Express and other frameworks still use `http` under the hood.**  
Understanding basic HTTP is foundational to using any Node.js web framework.

---

# 9. **Comparison: Raw HTTP Vs Express**

|Aspect|Raw HTTP Module|Express.js|
|---|---|---|
|Boilerplate|High|Low|
|Routing|Manual|Built-in|
|Middleware|Manual|Built-in|
|Ease of use|Low|High|
|Realistic usage|Rare|Very common|

Express is preferred in real projects, but understanding the `http` module builds strong fundamentals.

---

# **Summary Of Key Points**

- The server loads an HTML template and injects dynamic HTML using interpolation.
    
- `createServer()` wraps `http.createServer()` and handles asynchronous operations.
    
- Headers must be set correctly (`Content-Type: text/html`).
    
- The `start()` function starts the server, opens the browser, and logs the address.
    
- CLI integration fetches notes and starts the server on the selected port.
    
- Rendering approach is equivalent to basic server-side rendering patterns.
    
- Knowledge of the raw Node.js HTTP module provides foundational understanding before moving into frameworks like Express.

---

These notes capture the structure, logic, and broader context of building a simple Node.js HTTP server that performs server-side rendering of dynamic content.