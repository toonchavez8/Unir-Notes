# Technical Interview Study Guide: Node.js, Figma & Design Systems

## Node.js Fundamentals

Node.js is a **JavaScript runtime** built on Chrome’s V8 engine, designed for fast I/O and real-time applications. It uses a **single-threaded event loop** model to handle many concurrent tasks. In this model, Node offloads blocking I/O (file, network, database) to the OS and continues running other code; when I/O is done, callbacks/events are queued on the loop[digitalocean.com](https://www.digitalocean.com/community/tutorials/node-js-architecture-single-threaded-event-loop#:~:text=Node%20JS%20Platform%20does%20not,this%20model%20internals%2C%20first%20go)[geeksforgeeks.org](https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/#:~:text=NodeJS%20is%20single,each%20one%20to%20finish%20sequentially). This non-blocking, event-driven architecture allows a single Node process to serve many users efficiently. For example, if a request requires a database read, Node delegates that operation and continues processing other requests until the read returns, then handles the callback[digitalocean.com](https://www.digitalocean.com/community/tutorials/node-js-architecture-single-threaded-event-loop#:~:text=Node%20JS%20Platform%20does%20not,this%20model%20internals%2C%20first%20go)[geeksforgeeks.org](https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/#:~:text=NodeJS%20is%20single,each%20one%20to%20finish%20sequentially).

- **Non-blocking Event Loop:** Node’s core is the single-threaded **event loop**. It checks an “event queue” and processes callbacks as they arrive[digitalocean.com](https://www.digitalocean.com/community/tutorials/node-js-architecture-single-threaded-event-loop#:~:text=Node%20JS%20Platform%20does%20not,this%20model%20internals%2C%20first%20go). If a task is CPU-heavy or blocking, Node can offload it to a worker thread (or better, avoid it) so the loop can keep running[digitalocean.com](https://www.digitalocean.com/community/tutorials/node-js-architecture-single-threaded-event-loop#:~:text=,some%20Blocking%20IO%20Operations%20like)[geeksforgeeks.org](https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/#:~:text=NodeJS%20is%20single,each%20one%20to%20finish%20sequentially). This design lets Node handle thousands of concurrent connections with few resources.
    
- **Modules & NPM:** Node uses **CommonJS modules**: you `require('fs')` or `require('http')` to import functionality[geeksforgeeks.org](https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/#:~:text=In%20a%20NodeJS%20Application%2C%20a,http%2C%20fs%2C%20os%2C%20path%2C%20etc). The Node Package Manager (NPM) tracks dependencies via a `package.json` file and offers commands (`npm install`, `npm update`) to add or update libraries[geeksforgeeks.org](https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/#:~:text=NPM%20stands%20for%20the%20Node,key%20points%20about%20the%20NPM).
    
- **Asynchronous vs Synchronous:** Node favors **asynchronous** code. A synchronous function blocks until it finishes; in contrast, an asynchronous function initiates its work and lets the program continue running (often using callbacks, Promises, or `async/await` to handle the result)[geeksforgeeks.org](https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/#:~:text=Synchronous%20Functions%20Asynchronous%20Functions%20Blocks,Typically%20returns%20a%20promise%20or). Understanding Promises and the `async/await` syntax is crucial, since they help write non-blocking code that looks sequential.
    
- **Common API:** Familiarize with Node’s core modules (e.g. `fs`, `http`, `path`, `events`) and popular libraries. For example, the `http` module can create web servers; `fs` reads/writes files; `path` handles file paths. Express.js (a framework) is often used, so know middleware and routing basics.
    
- **Performance Notes:** Node is very fast for I/O-bound tasks and real-time apps, and it allows using the same language on server and client[geeksforgeeks.org](https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/#:~:text=Here%20are%20some%20reasons%20why,NodeJS%20is%20preferred). However, CPU-intensive tasks (image processing, heavy math) can block the loop. Node’s single-thread model can also limit raw compute throughput. As one GFG guide notes, Node’s **single-threaded nature** means it can’t fully utilize multi-core CPUs without clustering, and its API changes rapidly[geeksforgeeks.org](https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/#:~:text=%2A%20Single,introduce%20instability%20and%20compatibility%20issues).
    

## Figma & UI/UX Basics

**Figma** is a collaborative **web-based design tool** for UI and UX. It focuses on interface design and prototyping with real-time collaboration[en.wikipedia.org](https://en.wikipedia.org/wiki/Figma#:~:text=Figma%20is%20a%20collaborative%20,on%20mobile%20and%20tablet%20devices). Multiple designers (and engineers) can work on the same file simultaneously. In Figma you work in **Design mode** (drawing shapes, frames, and components), **Prototype mode** (creating interactive flows between screens), or **Dev mode** (inspecting elements for code snippets, assets, variables and dimensions)[en.wikipedia.org](https://en.wikipedia.org/wiki/Figma#:~:text=). This makes handoffs to developers smoother.

Key Figma concepts include:

- **Frames and Layouts:** Frames (like artboards) define the boundaries of designs and can use **Auto Layout** for responsive behavior. Auto Layout creates dynamic, flexible layouts that automatically adjust spacing and size as you add or change content[algocademy.com](https://algocademy.com/blog/top-figma-interview-questions-ace-your-design-tool-interview/#:~:text=Answer%3A%20Auto%20Layout%20in%20Figma,aspects%20of%20Auto%20Layout%20include). For example, placing buttons in an Auto Layout frame can ensure equal padding and can adapt if the button text changes.
    
- **Components & Instances:** Components are reusable elements (like buttons, cards, forms). You create a master component and then use its _instances_ in your design. Editing the master updates all instances automatically, ensuring consistency[algocademy.com](https://algocademy.com/blog/top-figma-interview-questions-ace-your-design-tool-interview/#:~:text=Q4%3A%20What%20are%20Components%20in,Figma). This lets you update a color or layout in one place, and have it ripple through the design.
    
- **Styles:** Figma lets you define **Styles** for colors, text, grids, effects, etc. A style is a named design token – for example a “Primary Color” style or a heading text style. When you apply these styles to objects, any later change to the style updates all linked objects[algocademy.com](https://algocademy.com/blog/top-figma-interview-questions-ace-your-design-tool-interview/#:~:text=Q8%3A%20What%20are%20Styles%20in,how%20do%20you%20create%20them). This is key for maintaining visual consistency (brand colors, typography) across large designs.
    
- **Variants:** Figma’s Variants group related component states together (e.g. button “size” or “state” variations) under one component, simplifying organization. A variant is a custom property (like “Primary/Secondary” or “Enabled/Hovered”) that lets you switch instances among multiple designs easily[algocademy.com](https://algocademy.com/blog/top-figma-interview-questions-ace-your-design-tool-interview/#:~:text=Answer%3A%20Variants%20in%20Figma%20allow,To%20create%20variants).
    
- **Teams and Libraries:** Teams can publish **Team Libraries** of components and styles so every project can reuse the same design system. For example, you might publish your component library so developers and designers can pull in up-to-date buttons, icons, etc. (Figma’s Design System support makes this straightforward[algocademy.com](https://algocademy.com/blog/top-figma-interview-questions-ace-your-design-tool-interview/#:~:text=Answer%3A%20A%20Design%20System%20in,a%20Design%20System%20in%20Figma)).
    

## Figma API and Automation

Figma also provides a **REST API** for developers. This API lets you access design file data programmatically (e.g. to export assets, read node properties, or automate workflows)[rollout.com](https://rollout.com/integration-guides/figma/api-essentials#:~:text=What%20type%20of%20API%20does,Figma%20provide). It uses standard HTTP methods (GET, POST, etc.) with JSON responses[rollout.com](https://rollout.com/integration-guides/figma/api-essentials#:~:text=What%20type%20of%20API%20does,Figma%20provide). To use it, you generate a personal access token in Figma and include it in API requests. Common uses include syncing design tokens to code, exporting icons/assets in bulk, or integrating Figma with project tools. Notably, Figma’s API supports **webhooks**: you can subscribe to events (like file or comment updates) so your server is notified in real-time when a designer publishes changes[rollout.com](https://rollout.com/integration-guides/figma/api-essentials#:~:text=Does%20the%20Figma%20API%20have,webhooks). In short, learning the Figma API means you can bridge design and development (for example, automatically pulling color values from Figma into your app)[rollout.com](https://rollout.com/integration-guides/figma/api-essentials#:~:text=What%20type%20of%20API%20does,Figma%20provide)[algocademy.com](https://algocademy.com/blog/top-figma-interview-questions-ace-your-design-tool-interview/#:~:text=Q11%3A%20How%20do%20you%20use,API%20for%20automation%20and%20integration).

## Storybook & Component Development

**Storybook** is a popular tool for UI component development and testing. It provides an isolated “workshop” where you can build, view, and interact with UI components outside of your main app[storybook.js.org](https://storybook.js.org/#:~:text=Storybook%20is%20a%20frontend%20workshop,It%27s%20open%20source%20and%20free). Thousands of teams use Storybook to develop component libraries: you spin up a local Storybook server and it renders your components (React, Vue, Angular, etc.) in different states. This makes it easy to visualize edge cases (disabled buttons, error states, form variations) without having to run the full application. As Storybook’s docs say: _“Storybook is a frontend workshop for building UI components and pages in isolation”_[storybook.js.org](https://storybook.js.org/#:~:text=Storybook%20is%20a%20frontend%20workshop,It%27s%20open%20source%20and%20free). By writing “stories” (scenarios) for each component, teams get interactive documentation and a testing sandbox. In interviews, know that Storybook is often mentioned in the context of design systems: it helps bridge designers and developers by showing exactly what each component does in code.

### **General Purpose**

This process integrates **Figma designs directly into Storybook** so developers can:

- Visually compare UI components to their design specs.
    
- Ensure pixel-perfect implementation without switching between tools.
    
- Improve collaboration between designers and developers by centralizing both code and design references.
    
- Optionally inspect spacing, colors, and tokens through Figma’s API (using figspec).
    

---

### **Interview-Style Answer**

> **“Integrating Figma with Storybook allows developers to embed live design references directly inside the component development environment. This helps ensure components match design specifications, speeds up reviews, and reduces context switching between design and code. It also improves collaboration across teams by making design assets and component states visible in one place. Additionally, with the Figma API (figspec), we can inspect spacing, colors, and styles directly in Storybook, supporting design consistency and faster QA.”**
# 1) Install the add-on

From your project root:

```bash
# npm
npm i -D storybook-addon-designs

# or: yarn add -D storybook-addon-designs
# or: pnpm add -D storybook-addon-designs
```

Stop Storybook if it’s running before you install.

---

# 2) Register the add-on in Storybook

In **.storybook/main.ts** (or **main.js**), add it to `addons`:

```ts
// .storybook/main.ts
import type { StorybookConfig } from '@storybook/react'; // adjust for your framework

const config: StorybookConfig = {
  // ...
  addons: [
    '@storybook/addon-essentials',
    'storybook-addon-designs', // 👈 add this
  ],
};

export default config;
```

---

# 3) Enable the “Design” panel globally (decorator)

Add the provided decorator so every story can show a design without repeating setup.

```ts
// .storybook/preview.ts (or preview.js)
import { withDesign } from 'storybook-addon-designs';

// Add it globally:
export const decorators = [withDesign];
```

This creates a **Design** tab/panel in Storybook’s addons area.

---

# 4) Link a Figma design to a story (basic “embed” view)

Copy a Figma link:

1. In Figma, select the frame/component (e.g., a Badge variant).
    
2. Right-click → **Copy link** (or use the share bar’s “Copy link”).
    

Attach it in your story’s `parameters`:

```ts
// Badge.stories.tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Badge } from './Badge';

const meta: Meta<typeof Badge> = {
  title: 'Components/Badge',
  component: Badge,

  // 👇 Applies to all stories in this file
  parameters: {
    design: {
      type: 'figma', // supports: 'figma' | 'image' | 'link' | 'iframe'
      url: 'https://www.figma.com/file/ABC...#node-id=123:456',
    },
  },
};

export default meta;
type Story = StoryObj<typeof Badge>;

export const Default: Story = { args: { /* ... */ } };
```

- Open Storybook → select your story → **Design** panel will show the embedded Figma artboard.
    
- You can also set `design` at the **story** level to point each variant at its specific Figma node:
    

```ts
export const Success: Story = {
  args: { variant: 'success' },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/ABC...#node-id=789:1011',
    },
  },
};
```

> Tip: Some teams prefer linking the whole sticker sheet at the meta level (quick visual comparison). Others link exact variants per story for pixel-perfect mapping. Do whichever matches your workflow.

---

# 5) Other supported design sources (optional)

Instead of Figma, you can embed:

```ts
parameters: {
  design: { type: 'image',  url: '/designs/badge.png'   } // static image
  // or
  design: { type: 'link',   url: 'https://design.docs' }   // plain link
  // or
  design: { type: 'iframe', url: 'https://your-site'   }   // live site / videos
}
```

---

# 6) Turn on **Figma “spec” view** (inspection overlays)

If you want measurements and tokens (spacing, sizes, CSS snippets) right inside Storybook, switch the design type to **figspec**. This uses the Figma API and requires a personal access token.

## 6.1 Create a Figma personal access token

- In Figma: **Settings → Account → Personal Access Tokens** → generate a token.
    
- Keep it secret.
    

## 6.2 Provide the token to Storybook

Create **.env** in your project root (or add to your env manager) and set:

```
STORYBOOK_FIGMA_ACCESS_TOKEN=YOUR_TOKEN_HERE
```

> Don’t commit your `.env` to version control.

**Restart Storybook** so it picks up the env var.

## 6.3 Use `figspec` in your story parameters

```ts
parameters: {
  design: {
    type: 'figspec',
    url: 'https://www.figma.com/file/ABC...#node-id=123:456',
  },
}
```

Now the Design panel shows inspection overlays: you can zoom and read spacing, sizes, and copy CSS-like values.

---

# 7) Compare design vs. implementation with Storybook tools

- Use Storybook’s toolbar (e.g., the **Measure** tool in `@storybook/addon-essentials`) to check paddings/margins on your rendered component and compare with the Figma panel.
    
- If you maintain light/dark variants, switch your component’s controls/theme and compare each against the respective Figma variant by changing the linked node or using per-story `parameters`.
    

---

# 8) Common tips & gotchas

- **Access**: The Figma link must be accessible to whoever opens Storybook (org/project permissions apply). If the panel is blank, check Figma permissions and that you’re logged in.
    
- **Exact node links**: Linking to a specific **node-id** (copy link while the exact layer is selected) makes the panel jump to the right variant.
    
- **Project-wide default**: Putting `design` in the file’s `meta.parameters` makes it default for all stories in the file; override at story level when needed.
    
- **Restart on env changes**: Any change to `.env` (token setup) requires a Storybook restart.
    
- **Security**: Don’t publish Storybook with a tokened figspec setup to public CI previews unless you’re okay with that exposure. Prefer environment scoping or internal previews.
    

---

## TL;DR Workflow

1. Install `storybook-addon-designs`.
    
2. Register it in `.storybook/main.(ts|js)`.
    
3. Add `withDesign` decorator in `.storybook/preview.(ts|js)`.
    
4. In each story (or at meta level), set:
    
    ```ts
    parameters: { design: { type: 'figma', url: 'FIGMA_LINK' } }
    ```
    
5. (Optional) For inspection overlays:
    
    - Create `STORYBOOK_FIGMA_ACCESS_TOKEN` in `.env`.
        
    - Restart Storybook.
        
    - Switch `type` to `'figspec'`.
        

That’s everything the video demonstrates—basic Figma embedding, global enablement, per-story overrides, and the optional “spec” mode with a token—plus a few tips to make it smooth in real projects.
## Design Systems & Atomic Design

A **design system** is a comprehensive, unified set of design standards, components, and guidelines that keep a product’s interface consistent[figma.com](https://www.figma.com/blog/design-systems-101-what-is-a-design-system/#:~:text=What%20exactly%20is%20a%20design,system). As Figma’s blog explains: _“At its core, a design system is a set of building blocks and standards that help keep the look and feel of products … consistent,”_ serving as a blueprint and shared language for teams[figma.com](https://www.figma.com/blog/design-systems-101-what-is-a-design-system/#:~:text=What%20exactly%20is%20a%20design,system). This typically includes:

- **Foundational Elements:** Colors, typography, spacing tokens, icons and imagery guidelines. These are the raw design tokens that define your brand palette and styles.
    
- **Component Library:** Reusable UI elements (buttons, inputs, cards, navigation bars, etc.) often implemented in code (React components, CSS classes, etc.) and documented. The library may include variants for different states or sizes.
    
- **Pattern/Template Library:** Higher-level patterns (login flows, data tables, page layouts) that show how components combine to solve UX problems.
    
- **Guidelines & Documentation:** Rules on when and how to use components, accessibility guidelines, code snippets, and design rationale.
    

Design systems differ from simple style guides. They not only cover visuals but also include technical and usability standards. In Figma’s words, _“design systems are more holistic, including coding standards and usability, while a style guide is a subset focusing on visual elements”_[figma.com](https://www.figma.com/blog/design-systems-101-what-is-a-design-system/#:~:text=,and%20style%20guides). A well-built system lets designers focus on creativity (solving new UX problems) instead of recreating common elements, and it lets developers implement interfaces more predictably.

One popular methodology is **Atomic Design** (by Brad Frost). It breaks UI design into a hierarchy: _atoms_ (basic elements like buttons or labels), _molecules_ (groups of atoms functioning together, like a search form), _organisms_ (complex UI sections composed of molecules, like a header), and so on[figma.com](https://www.figma.com/blog/design-systems-101-what-is-a-design-system/#:~:text=The%20introduction%20of%20Brad%20Frost%E2%80%99s,shared%20vocabulary%20for%20design%20and). This approach provides a shared vocabulary and structure: for example, a developer can hear “atoms and molecules” and immediately know it refers to that hierarchy of component granularity[figma.com](https://www.figma.com/blog/design-systems-101-what-is-a-design-system/#:~:text=The%20introduction%20of%20Brad%20Frost%E2%80%99s,shared%20vocabulary%20for%20design%20and).

To implement a design system in practice (especially using Figma and code):

- Define **styles/tokens** first (colors, text styles, spacing).
    
- Create **components** in Figma for each UI element, using Variants for different states (e.g. enabled/disabled buttons)[algocademy.com](https://algocademy.com/blog/top-figma-interview-questions-ace-your-design-tool-interview/#:~:text=Answer%3A%20A%20Design%20System%20in,a%20Design%20System%20in%20Figma).
    
- Organize components into logical categories and pages.
    
- Document usage guidelines and rules (either in Figma or in a separate style guide site).
    
- Publish the system (e.g. as a Figma Team Library and as a code package) for others to use. As one guide puts it, a Figma design system requires “defin[ing] color, text, and effect styles; creating components; using variants; documenting guidelines; and publishing to your team library”[algocademy.com](https://algocademy.com/blog/top-figma-interview-questions-ace-your-design-tool-interview/#:~:text=Answer%3A%20A%20Design%20System%20in,a%20Design%20System%20in%20Figma). Regular maintenance is also key: a design system evolves as the product grows.
    

## Behavioral Interview Strategies

In behavioral interviews, focus on _how_ you handled real situations. Employers often use the **STAR method** (Situation, Task, Action, Result) to structure answers[capd.mit.edu](https://capd.mit.edu/resources/the-star-method-for-behavioral-interviews/#:~:text=S,by%20breaking%20down%20the%20formula). For each question, clearly describe the **Situation** and context, your specific **Task** or goal, the **Action** you personally took, and the outcome or **Result**. For example, instead of saying _“We improved the design”_, you’d say _“I led a redesign of the landing page (Situation/Task). I researched user needs, updated the component library for consistency, and coordinated with developers to implement the changes (Action). This resulted in a 20% increase in user engagement (Result).”_ Interviews look for clarity and ownership: use “I” statements to highlight your contributions[capd.mit.edu](https://capd.mit.edu/resources/the-star-method-for-behavioral-interviews/#:~:text=you,outcomes%20of%20the%20team%20efforts).

Common behavioral themes include teamwork (working on a cross-functional team), leadership (taking initiative), challenges (overcoming obstacles or tight deadlines), conflict resolution, and learning from mistakes. Practice describing 3–5 concise stories from past projects, each illustrating skills relevant to the role (communication, problem-solving, adaptability, etc.). By preparing STAR-formatted stories and practicing them aloud, you can answer questions like _“Tell me about a time you….”_ with confidence and structure[capd.mit.edu](https://capd.mit.edu/resources/the-star-method-for-behavioral-interviews/#:~:text=S,by%20breaking%20down%20the%20formula)[capd.mit.edu](https://capd.mit.edu/resources/the-star-method-for-behavioral-interviews/#:~:text=you,outcomes%20of%20the%20team%20efforts).

## System Design Approach

System-design interviews test your architectural thinking. When presented with a design problem (e.g. **“Design a URL shortener”** or **“Design a chat system”**), use a structured approach:

- **Clarify requirements:** Ask what features are needed, what the scale is (users per second, data size), and constraints (e.g. latency, consistency needs)[github.com](https://github.com/donnemartin/system-design-primer#:~:text=Step%201%3A%20Outline%20use%20cases%2C,constraints%2C%20and%20assumptions). Determine who will use the system and what the core use cases are.
    
- **High-level design:** Sketch a block diagram of major components (clients, web servers, application servers, databases, caches, load balancers)[github.com](https://github.com/donnemartin/system-design-primer#:~:text=Outline%20a%20high%20level%20design,with%20all%20important%20components). Explain your choices: for example, you might use a relational database for transactional data or a NoSQL store for highly-scalable reads.
    
- **Core component design:** Drill into key parts. For a URL shortener, that would include how to generate unique hashes, database schema, and how to resolve a short link back to the original URL[github.com](https://github.com/donnemartin/system-design-primer#:~:text=Outline%20a%20high%20level%20design,with%20all%20important%20components). Talk through data models and APIs (e.g. a “shorten URL” API vs a “redirect” handler).
    
- **Scalability & Trade-offs:** Identify bottlenecks and scalability techniques[github.com](https://github.com/donnemartin/system-design-primer#:~:text=Step%204%3A%20Scale%20the%20design). Discuss caching, load balancing, database sharding or replication, rate limiting, etc. For example, you might add a Redis cache in front of the database to speed up lookups. Mention trade-offs (e.g. consistency vs availability). Address how the design would handle growth, and justify your decisions.
    

Throughout, communicate clearly (draw on a whiteboard if available) and explain trade-offs. Citing one resource on system design: _“Gather requirements…ask questions to clarify use cases… outline a high level design with all important components… then identify and address bottlenecks”_[github.com](https://github.com/donnemartin/system-design-primer#:~:text=Step%201%3A%20Outline%20use%20cases%2C,constraints%2C%20and%20assumptions)[github.com](https://github.com/donnemartin/system-design-primer#:~:text=Step%204%3A%20Scale%20the%20design). Practice a few common scenarios (news feed, chat server, social media timeline) so you’re comfortable sketching quick diagrams and reasoning through them.

## Coding Interview Techniques (Whiteboard)

For algorithm/coding interviews, a clear step-by-step approach is key. Most experts recommend:

1. **Clarify the problem.** Before coding, restate the problem in your own words and ask clarifying questions about edge cases or constraints. (E.g., _“Can inputs be null?”_, _“Is the data size small enough to use simple methods?”_). Always confirm you understand the inputs and expected outputs[techinterviewhandbook.org](https://www.techinterviewhandbook.org/coding-interview-techniques/#:~:text=How%20to%20find%20solutions%20to,coding%20interview%20problems).
    
2. **Plan an approach.** Think out loud about possible solutions and their trade-offs. A good practice is to **visualize** or **draw diagrams**: sketch input data structures (arrays, linked lists, trees) on the whiteboard and walk through how you’d manipulate them[techinterviewhandbook.org](https://www.techinterviewhandbook.org/coding-interview-techniques/#:~:text=1,drawing%20it%20out). For example, draw a small example and manually work through the steps of your idea.
    
3. **Work out examples by hand.** Picking a simple test case and stepping through it manually often reveals a correct algorithm or necessary adjustments[techinterviewhandbook.org](https://www.techinterviewhandbook.org/coding-interview-techniques/#:~:text=2,solve%20the%20problem%20by%20hand). This also demonstrates your reasoning to the interviewer.
    
4. **Write pseudocode or modular steps.** Break the problem into smaller parts or functions. Outline the high-level algorithm before writing actual code. For instance, _“First I will compute a frequency map of all items, then iterate and build groups…”_[techinterviewhandbook.org](https://www.techinterviewhandbook.org/coding-interview-techniques/#:~:text=4,into%20smaller%20independent%20parts). This shows you have a plan.
    
5. **Code carefully.** Translate your plan into code, speaking through each line. Use meaningful variable names and consider edge cases (empty input, large values, etc.). If you get stuck while coding, narrate your thoughts or switch back to pseudocode – communication is as important as getting the perfect answer.
    
6. **Test your solution.** After coding, run through a couple of test cases (including edge cases) to verify correctness. If a mistake appears, fix it on the board and explain the fix.
    

As one guide emphasizes: _“candidates should start by asking clarifying questions and discussing a few possible approaches with their interviewers”_[techinterviewhandbook.org](https://www.techinterviewhandbook.org/coding-interview-techniques/#:~:text=How%20to%20find%20solutions%20to,coding%20interview%20problems). Visual aids help too: _“draw diagrams… to see the pattern”_ when dealing with matrices or trees[techinterviewhandbook.org](https://www.techinterviewhandbook.org/coding-interview-techniques/#:~:text=1,drawing%20it%20out). Remember, interviewers look for problem-solving process, not just the final code.

## Suggested 2-Week Study Plan

To maximize the 2-week timeframe, divide your study:

- **Week 1:** Focus on core technical concepts and coding practice.
    
    - **Day 1-2:** Review Node.js theory (event loop, async I/O, modules, NPM) using documentation or tutorials[digitalocean.com](https://www.digitalocean.com/community/tutorials/node-js-architecture-single-threaded-event-loop#:~:text=Node%20JS%20Platform%20does%20not,this%20model%20internals%2C%20first%20go)[geeksforgeeks.org](https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/#:~:text=NodeJS%20is%20single,each%20one%20to%20finish%20sequentially). Write and run small Node scripts (e.g. simple HTTP server, file reads with callbacks).
        
    - **Day 3-4:** Deepen JavaScript/Node knowledge (Promised-based async, streams, error handling). Solve a few Node-flavored problems (e.g. streaming JSON, building a REST endpoint).
        
    - **Day 5-6:** Study Figma and design basics. Follow a Figma tutorial to practice components, auto-layout, and styles[algocademy.com](https://algocademy.com/blog/top-figma-interview-questions-ace-your-design-tool-interview/#:~:text=Q4%3A%20What%20are%20Components%20in,Figma)[algocademy.com](https://algocademy.com/blog/top-figma-interview-questions-ace-your-design-tool-interview/#:~:text=Q8%3A%20What%20are%20Styles%20in,how%20do%20you%20create%20them). If possible, open Figma and create a simple design with a few components.
        
    - **Day 7:** Review behavioral interview basics. Prepare 4–5 STAR stories from past projects (using Situation-Task-Action-Result)[capd.mit.edu](https://capd.mit.edu/resources/the-star-method-for-behavioral-interviews/#:~:text=S,by%20breaking%20down%20the%20formula) and rehearse them aloud.
        
- **Week 2:** Shift to interview simulation and advanced topics.
    
    - **Day 8-9:** Cover design systems theory (read about atomic design and study [8] or [15] on what a design system is)[figma.com](https://www.figma.com/blog/design-systems-101-what-is-a-design-system/#:~:text=The%20introduction%20of%20Brad%20Frost%E2%80%99s,shared%20vocabulary%20for%20design%20and)[figma.com](https://www.figma.com/blog/design-systems-101-what-is-a-design-system/#:~:text=,and%20style%20guides). In Figma, try building a mini design system: define a few color/text styles and create reusable components.
        
    - **Day 10:** Practice system design problems. Choose 1–2 prompts (e.g. design a simple chat app or e-commerce checkout) and sketch a solution end-to-end (requirements, architecture diagram, components, scaling)[github.com](https://github.com/donnemartin/system-design-primer#:~:text=Step%201%3A%20Outline%20use%20cases%2C,constraints%2C%20and%20assumptions)[github.com](https://github.com/donnemartin/system-design-primer#:~:text=Step%204%3A%20Scale%20the%20design).
        
    - **Day 11-12:** Continue whiteboard coding practice. Time yourself solving 2–3 algorithm problems (use an online judge or just paper) and follow the clarifying/plan/code steps[techinterviewhandbook.org](https://www.techinterviewhandbook.org/coding-interview-techniques/#:~:text=How%20to%20find%20solutions%20to,coding%20interview%20problems)[techinterviewhandbook.org](https://www.techinterviewhandbook.org/coding-interview-techniques/#:~:text=1,drawing%20it%20out). Focus on explaining your thought process clearly.
        
    - **Day 13:** Review Figma API basics if relevant (look at [22] Figma API docs), or try a mini-plugin if time allows. Also skim common Node.js interview questions and ensure you know the answers.
        
    - **Day 14:** Mock interview day – ask a friend or record yourself. Do one behavioral question, one design sketch, and one coding problem under timed conditions. Identify weak spots and lightly review them before the real interview. Relax and get rest before interview day.
        

This plan balances theory (concepts and docs) with practice (hands-on exercises and mock problems). Adjust as needed to your strengths and weaknesses, but ensure you touch all areas: Node fundamentals, design tool concepts, system thinking, and clear communication. Good luck!

----

## Algorithms

## **Array Algorithm**
#### Maximum Subarray Sum - Kadane's Algorithm

Given an integer array ****arr[]****, find the ****subarray**** (containing at least one element) which has the ****maximum possible sum****, and return that sum.  
****Note:**** A ****subarray**** is a continuous part of an array.

> [!NOTE]
> ****Input:**** arr[] = [2, 3, -8, 7, -1, 2, 3]  
> ****Output:**** 11  
> ****Explanation:**** The subarray [7, -1, 2, 3] has the largest sum 11.
> 
> ****Input:**** arr[] = [-2, -4]  
> ****Output:**** -2  
> ****Explanation:**** The subarray [-2] has the largest sum -2.
> 
> ****Input:**** arr[] = [5, 4, 1, 7, 8]  
> ****Output:**** 25  
> ****Explanation:**** The subarray [5, 4, 1, 7, 8] has the largest sum 25.


##### Naive Approach By iterating over all subarrays - O(n^2) Time and O(1) Space

The idea is to run two nested loops to iterate over all possible subarrays and find the maximum sum. The outer loop will mark the starting point of a subarray and inner loop will mark the ending point of the subarray.


```js
function maxSubarraySum(arr) {
    let res = arr[0];
  
    // Outer loop for starting point of subarray
    for (let i = 0; i < arr.length; i++) {
        let currSum = 0;
      
        // Inner loop for ending point of subarray
        for (let j = i; j < arr.length; j++) {
            currSum = currSum + arr[j];
          
            // Update res if currSum is greater than res
            res = Math.max(res, currSum);
        }
    }
    return res;
}

const arr = [2, 3, -8, 7, -1, 2, 3];
console.log(maxSubarraySum(arr));
```

```python
def maxSubarraySum(arr):
    res = arr[0]
  
    # Outer loop for starting point of subarray
    for i in range(len(arr)):
        currSum = 0
      
        # Inner loop for ending point of subarray
        for j in range(i, len(arr)):
            currSum = currSum + arr[j]
            # Update res if currSum is greater than res
            res = max(res, currSum)
          
    return res

if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(maxSubarraySum(arr))
```


>   
> The idea of [****Kadane's algorithm****](https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1) is to traverse over the array from left to right and for each element, find the maximum sum among ****all subarrays ending at that element****. The result will be the maximum of all these values.

To calculate the maximum sum of subarray ending at current element, say ****maxEnding****, we can use the maximum sum ending at the previous element.


##### [Expected Approach] Using Kadane's Algorithm - O(n) Time and O(1) Space

So for any element, we have two choices:

> ****Choice 1:**** Extend the maximum sum subarray ending at the previous element by adding the current element to it. If the maximum subarray sum ending at the previous index is ****positive****, then it is always better to extend the subarray.
> 
> ****Choice 2:**** Start a new subarray starting from the current element. If the maximum subarray sum ending at the previous index is ****negative****, it is always better to start a new subarray from the current element.

This means that ****maxEnding at index i = max(maxEnding at index (i - 1) + arr[i], arr[i])**** and the ****maximum**** value of maxEnding at any index will be our answer.

```js

function maxSubarraySum(arr) {
    
    // Stores the result (maximum sum found so far)    
    let res = arr[0];
    
    // Maximum sum of subarray ending at current position
    let maxEnding = arr[0];

    for (let i = 1; i < arr.length; i++) {
        
        // Either extend the previous subarray or start 
        // new from current element
        maxEnding = Math.max(maxEnding + arr[i], arr[i]);
        
        // Update result if the new subarray sum is larger
        res = Math.max(res, maxEnding);
    }
    return res;
}

// Driver Code
const arr = [2, 3, -8, 7, -1, 2, 3];
console.log(maxSubarraySum(arr));
```

```python

def maxSubarraySum(arr):
    
    # Stores the result (maximum sum found so far)
    res = arr[0]
    
    # Maximum sum of subarray ending at current position
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        
        # Either extend the previous subarray or start 
        # new from current element
        maxEnding = max(maxEnding + arr[i], arr[i])
        
        # Update result if the new subarray sum is larger
        res = max(res, maxEnding)
    
    return res

if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(maxSubarraySum(arr))
```

### Find the missing Numbers
Given an array ****arr[]**** of size ****n-1**** with ****distinct**** integers in the range of ****[1, n].**** This array represents a permutation of the integers from 1 to n with one element missing. Find the missing element in the array.

****Examples:**** 

>****Input:**** `arr[] = [8, 2, 4, 5, 3, 7, 1]  `
****Output:**** `6  `
****Explanation:**** All the numbers from 1 to 8 are present except 6.
****Input:**** `arr[] = [1, 2, 3, 5]  `
****Output:**** `4  `
****Explanation:**** Here the size of the array is `4`, so the range will be` [1, 5]`. The missing number between `1` to `5` is `4`


#### [Naive Approach] Linear Search for Missing Number - O(n^2) Time and O(1) Space

This approach iterates through each number from 1 to `n` (where `n` is the size of the array + 1) and checks if the number is present in the array. For each number, it uses a nested loop to search the array. If a number is not found, it is returned as the missing number.

```js

function missingNum(arr) {
    const n = arr.length + 1;

    // Iterate from 1 to n and check
    // if the current number is present
    for (let i = 1; i <= n; i++) {
        let found = false;
        for (let j = 0; j < n - 1; j++) {
            if (arr[j] === i) {
                found = true;
                break;
            }
        }

        // If the current number is not present
        if (!found)
            return i;
    }
    return -1;
}

// drvier code 
const arr = [8, 2, 4, 5, 3, 7, 1];
console.log(missingNum(arr));
```

```python
def missingNum(arr):
    n = len(arr) + 1

    # Iterate from 1 to n and check
    # if the current number is present
    for i in range(1, n + 1):
        found = False
        for j in range(n - 1):
            if arr[j] == i:
                found = True
                break

        # If the current number is not present
        if not found:
            return i
    return -1

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr))
```

#### ****[Better Approach] Using Hashing - O(n) Time and O(n) Space****

This approach uses a hash array (or frequency array) to track the presence of each number from 1 to `n` in the input array. It first initializes a hash array to store the frequency of each element. Then, it iterates through the hash array to find the number that is missing (i.e., the one with a frequency of 0).

```js
function missingNum(arr) {
    let n = arr.length + 1;

    // Create hash array of size n+1
    let hash = new Array(n + 1).fill(0);

    // Store frequencies of elements
    for (let i = 0; i < n - 1; i++) {
        hash[arr[i]]++;
    }

    // Find the missing number
    for (let i = 1; i <= n; i++) {
        if (hash[i] === 0) {
            return i;
        }
    }
    return -1;
}

// driver code
const arr = [8, 2, 4, 5, 3, 7, 1];
const res = missingNum(arr);
console.log(res);
```

```python
def missingNum(arr):
    n = len(arr) + 1

    # Create hash array of size n+1
    hash = [0] * (n + 1)

    # Store frequencies of elements
    for i in range(n - 1):
        hash[arr[i]] += 1

    # Find the missing number
    for i in range(1, n + 1):
        if hash[i] == 0:
            return i
    return -1

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    res = missingNum(arr)
    print(res)
```