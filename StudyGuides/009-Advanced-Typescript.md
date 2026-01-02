TypeScript can sometimes feel like bunch of nonsense. But once you internalize a few key patterns, the type system starts to feel like a powerful tool instead of an obstacle.

Here are a few tricks that I’ve personally found valuable, especially if you’re working on a large codebase or building libraries.

---

# 1. Optional Keys Vs Optional Values

There’s a big difference between marking a property as optional and allowing `undefined` as a value. These look similar:

```TypeScript
type OptionalKey = {
  foo?: string;
}

type OptionalValue = {
  foo: string | undefined;
}
```

But they behave differently:

- `foo?: string` means the key `foo` might not be present at all.
- `foo: string | undefined` means `foo` is always present, but its value might be `undefined`.

Why this matters? The difference between them affects the way you use it:

- How you check if a property exists
- Function argument inference
- Serializing/deserializing data from external sources

## Example

```TypeScript
function logFoo(obj: OptionalKey) {
  if ('foo' in obj) {
    console.log(obj.foo?.toUpperCase());
  }
}

function logBar(obj: OptionalValue) {
  console.log(obj.foo?.toUpperCase()); // May log undefined
}
```

As a rule of thumb, use `foo?: Type` (Optional Key) when the property might not be present, and `foo: Type | undefined` (Optional Value) when the key is always expected.

---

# 2. Pick and Omit for Object Key Manipulation

When you need to reshape object types by including or excluding specific keys, `Pick` and `Omit` are your go-to tools.

This type utilities are part of the language and are always available for your use, they are particularly useful when you need to derive types.

> Don't forget, Pick and Omit works over Object shapes

## Pick

```TypeScript
type User = {
  id: number;
  name: string;
  email: string;
};

type PublicUser = Pick<User, 'id' | 'name'>;
// { id: number; name: string }
```

`Pick` is useful when exposing a public-facing API without leaking sensitive fields, it lets you choose what properties will be included

## Omit

```TypeScript
type PrivateUser = Omit<User, 'email'>;
// { id: number; name: string }
```

Use `Omit` when you want to reuse a base type but remove some fields for specific scenarios, like forms or UI display logic.

These utilities keep your types DRY and consistent. Instead of redefining structures, you can derive them from existing ones, reducing duplication and potential errors.

---

# 3. Extract and Exclude for Union Filtering

Unlike `Pick` and `Omit`, which work on object keys, `Extract` and `Exclude` operate on union types, they are pretty similar in how the work.

## Extract

```TypeScript
type Status = 'draft' | 'published' | 'archived';

type ArchivedOnly = Extract<Status, 'archived'>;
// 'archived'
```

Use `Extract` when you want to narrow down a union to only include specific members.

## Exclude

```TypeScript
type VisibleStatus = Exclude<Status, 'archived'>;
// 'draft' | 'published'
```

Use `Exclude` when you want to remove one or more members from a union.

These are essential tools when refining API responses, filtering variants, or creating conditional logic that needs to type-check specific string literal options.

---

# 4. Loose Autocomplete

This is a different kind of trick, this one affects how your editor understand your types.

Sometimes you want to offer a set of suggestions to the user without forcing them to pick from a fixed list.

## The Trick

```TypeScript
type Variant = 'success' | 'warning' | 'info'

function setVariant(variant: Variant | (string & {})) {
  // ...
}
```

Now TypeScript will offer autocompletion for the variants defined in the `Variant` union, but will also allow allow any other string.

`string & {}` is essentially still a string, but TypeScript treats it as a branded version, preserving autocomplete while keeping it assignable to `string`.

> [Here](https://egghead.io/blog/using-branded-types-in-typescript) you can found another article related to [Branded Types](https://egghead.io/blog/using-branded-types-in-typescript)

## Use Cases

- Props with suggested values
- Config objects
- Third-party data with flexible inputs

---

# 5. Mapped Types for Smart Rewrites

Mapped types let you create new types from existing ones by transforming each property. This concept is a cornerstone of TypeScript’s type system and is covered more deeply in my article: [Learn the Key Concepts of TypeScript’s Powerful Generic and Mapped Types](https://egghead.io/blog/learn-the-key-concepts-of-typescript-s-powerful-generic-and-mapped-types).

You can consider Mapped types as some kind of function that transform a type in another by using all of the utilities and features of Typescript, like the above utilities and tricks, but also string literals, and more.

## Example: Feature Flags

```TypeScript
type Config = {
  debug: string;
  logging: string;
};

type FeatureFlags = {
  [K in keyof Config]: boolean;
};
// This will create the following type
// { debug: boolean; logging: boolean }
```

## General Utility Type

```TypeScript
type Booleanize<T> = {
  [K in keyof T]: boolean;
};
```

Mapped types are perfect for:

- Adapting backend responses
- Creating flexible utility types
- Rewriting shapes while preserving keys
- Enforcing contracts between layers

They’re also essential in combination with generics to create reusable type logic across your app or library.

> Found more about Generics in the following article [An Introduction to Typescript Generics](https://egghead.io/blog/an-introduction-to-typescript-generics)

---

# 6. The IIMT Pattern (Infer Inside Mapped Type)

This pattern unlocks the power of `infer` within mapped types, allowing you to extract and reuse internal type information from complex structures.

It dynamically inspects each property of a type (by using `infer`), and if that property matches a specific shape (e.g., a function), it extracts part of it.

This means you can build new types that are entirely based on the structure of other types without manually copying anything.

## The Pattern

```TypeScript
type API = {
  getUser: () => Promise<{ name: string }>;
  logout: () => void;
};

type ReturnTypes<T> = {
  [K in keyof T]: T[K] extends (...args: any) => infer R ? R : never;
};

// Result:
// {
//   getUser: Promise<{ name: string }>;
//   logout: void;
// }
```

Here, ReturnTypes iterates over each key in the API object and uses conditional types to check if the value is a function. If it is, it uses infer R to grab the return type of that function.

## How it Works

- `keyof T` iterates over each key of the input type.
- `T[K]` accesses the value type at each key.
- `T[K] extends (…args: any) => infer R` checks if that value is a function. (consider this as a conditional block)
- `infer R` captures the return type of the function.
- If the value is not a function, the fallback is never.

This pattern is composable—you can use it to build return type maps, argument type maps, or anything else you need.

```TypeScript
type ArgumentTypes<T> = {
  [K in keyof T]: T[K] extends (...args: infer A) => any ? A : never;
};
```

This will give you a type with the argument list of each function in a mapped type.

You can use this in different situations like:

- Generating automatic schemas
- Building strongly-typed service clients
- Rewriting function maps
- Validating types without duplicating logic

If you’re building libraries or dynamic APIs, this pattern is a must-have in your TypeScript toolbox.

Once it clicks, it opens the door to expressive, scalable, and maintainable type logic.