
## **HTTP Server Code Explanation**

### **1. Mock Data**

```js
const mockUsers = [
  { id: 1, name: "John Doe" },
  { id: 2, name: "Jane Smith" },
  { id: 3, name: "Alice Johnson" },
];
```

- Holds a sample list of users.
    
- Acts as a temporary database for demonstration purposes.
    

---

### **2. Server Port**

```js
const PORT = process.env.PORT;
```

- Reads the port number from environment variables.
    
- Server listens on this port to handle incoming requests.
    

---

### **3. Middleware Functions**

#### **Logger Middleware**

```js
const logger = (req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
};
```

- Logs incoming HTTP method (`GET`, `POST`, etc.) and URL path to the console.
    
- `next()` ensures the next function in the chain runs.
    

#### **JSON Header Middleware**

```js
const jsonHeaderMiddleware = (req, res, next) => {
  res.setHeader("Content-Type", "application/json");
  next();
};
```

- Sets the response `Content-Type` header to `application/json`.
    
- Ensures responses are sent as JSON when required.
    

---

### **4. Request Handlers**

#### **Get All Users**

```js
const getUsersHandler = (req, res) => {
  jsonHeaderMiddleware(req, res, () => {
    res.end(JSON.stringify(mockUsers));
  });
};
```

- Handles `GET /api/users`.
    
- Returns all users in JSON format.
    

#### **Get User by ID**

```js
const getUserByIdHandler = (req, res) => {
  const userId = req.url.split("/")[3];
  const user = mockUsers.find((user) => user.id === parseInt(userId));
  if (user) {
    jsonHeaderMiddleware(req, res, () => {
      res.end(JSON.stringify(user));
    });
  } else {
    res.writeHead(404, { "Content-Type": "text/html" });
    res.end("<h1>404 Not Found</h1><p>User not found.</p>");
  }
};
```

- Handles `GET /api/users/:id`.
    
- Finds user by `id` from URL.
    
- Returns user if found, otherwise responds with a `404` error page.
    

#### **Create User**

```js
const createUserHandler = (req, res) => {
  let body = "";
  req.on("data", (chunk) => {
    body += chunk.toString();
  });
  req.on("end", () => {
    const newUser = JSON.parse(body);
    mockUsers.push({ id: mockUsers.length + 1, ...newUser });
    res.statusCode = 201;
    jsonHeaderMiddleware(req, res, () => {
      res.end(JSON.stringify(newUser));
    });
  });
};
```

- Handles `POST /api/users`.
    
- Reads request body, parses it as JSON, and adds a new user to `mockUsers`.
    
- Responds with `201 Created` and the newly added user.
    

#### **Not Found Handler**

```js
const notFoundHandler = (req, res) => {
  res.statusCode = 404;
  res.setHeader("Content-Type", "text/html");
  res.end("<h1>404 Not Found</h1><p>The page you are looking for does not exist.</p>");
};
```

- Handles requests that do not match any route.
    
- Returns a simple HTML 404 error page.
    

---

### **5. Server Setup**

```js
const server = http.createServer((req, res) => {
  logger(req, res, () => {
    if (req.url === "/api/users" && req.method === "GET") {
      getUsersHandler(req, res);
    } else if (req.url.match(/\/api\/users\/(\d+)/) && req.method === "GET") {
      getUserByIdHandler(req, res);
    } else if (req.url === "/api/users" && req.method === "POST") {
      createUserHandler(req, res);
    } else {
      notFoundHandler(req, res);
    }
  });
});
```

- Creates HTTP server.
    
- Uses `logger` to log each request.
    
- Routes requests to correct handlers based on URL and HTTP method.
    
- Falls back to `notFoundHandler` for unknown routes.
    

---

### **6. Start Server**

```js
server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

- Starts listening for incoming requests.
    
- Logs a message with the server address.
    

---

Here is the updated note with an additional section for possible improvements based on the enhanced version of the code you shared:

---

## **Possible Improvements**

### **1. Default Port Value**

```js
const PORT = process.env.PORT || 3000;
```

- Provides a fallback port (`3000`) if `process.env.PORT` is not set.
    
- Makes the server easier to run locally without requiring environment variables.
    

---

### **2. Middleware System Enhancement**

```js
const middlewares = [logger];

function runMiddlewares(req, res, middlewares, done) {
	let idx = 0;
	function next() {
		if (idx < middlewares.length) {
			middlewares[idx++](req, res, next);
		} else {
			done();
		}
	}
	next();
}
```

- Allows multiple middleware functions to be executed in sequence.
    
- Improves scalability, making it easier to add authentication, rate limiting, or other middleware later.
    

---

### **3. Route Mapping**

```js
const routes = {
	"GET /api/users": getUsersHandler,
	"POST /api/users": createUserHandler,
};
```

- Replaces multiple `if-else` statements with a `routes` object.
    
- Provides a cleaner and more scalable way to define API routes.
    

---

### **4. Enhanced Error Handling for JSON Parsing**

```js
try {
	const newUser = JSON.parse(body);
	// ...
} catch (err) {
	console.error("Error parsing JSON:", err);
	res.writeHead(400, { "Content-Type": "application/json" });
	res.end(JSON.stringify({ error: "Invalid JSON", details: err.message }));
}
```

- Catches JSON parsing errors.
    
- Returns a clear `400 Bad Request` response if invalid JSON is sent.
    

---

### **5. Improved URL Handling**

```js
const parsedUrl = new URL(req.url, `http://${req.headers.host}`);
const pathname = parsedUrl.pathname;
```

- Uses `URL` object for cleaner and more reliable URL parsing.
    
- Makes extracting parameters (e.g., `userId`) easier and more consistent.
    

---

### **6. Cleaner Dynamic Route Matching**

```js
else if (method === "GET" && /^\/api\/users\/(\d+)$/.test(pathname)) {
	const userId = pathname.split("/")[3];
	getUserByIdHandler(req, res, userId);
}
```

- Uses regular expression to match dynamic routes like `/api/users/1`.
    
- Improves readability and prevents incorrect matches.
    

---

### **7. Modular and Scalable Design**

- Middleware, routes, and handlers are structured to make future expansion easier.
    
- Codebase can be easily extended with:
    
    - Additional endpoints (e.g., PUT, DELETE for users).
        
    - More middleware (e.g., authentication, CORS).
        
    - External database integration (instead of in-memory `mockUsers`).
        

---

