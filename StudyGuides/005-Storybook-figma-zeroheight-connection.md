
First i began a default next js project at latest 

Installed tailwind 

Then i instaled the shadcn cli for faster component building with tailwind

Then i installed the storybook project near the end it stlightly failed due to mis configured post css

So i updated it to uise 

```js
export default {

  plugins: {

    "@tailwindcss/postcss": {},

  },

};
```
Instead of

```js
const config = {

  plugins: ["@tailwindcss/postcss"],

};

  

export default config;
```


Then i installed concurently to run both my npm run dev and my npm run storybook

`npm i -D concurrently`


So i an later run 

```json
  "scripts": {

    "dev": "concurrently \"next dev --turbopack\" \"npm run storybook\""
    }
```

Then i deleted everything inside the stories folder to begin

I installed shadcin button

`npx shadcn@latest add button`

Then i created a new `button.stories.tsx`

