# Alejandra Leyva Journalist Portfolio Site

**Type:** Client  
**Source:** FoodLovers – Alejandra Leyva  
**Repository:** [https://github.com/toonchavez8/alejandra-leyva-portfolio](https://github.com/toonchavez8/alejandra-leyva-portfolio)  
**Live Site:** [https://alejandra-leyva.com/](https://alejandra-leyva.com/)

---

## Overview

A portfolio website for photojournalist **Alejandra Leyva** designed to showcase her projects and published work. The site allows the client to create and manage new project pages through a CMS and supports bilingual content in both English (`eng`) and Spanish (`esp`).

---

## Objectives

- Design the portfolio using **Figma**
    
- Build a fully responsive site connected to a CMS
    
- Support local language switching (English / Spanish)

---

## Tech Stack

- Figma
    
- Next.js, Tailwind CSS
    
- Prismic IO (Headless CMS)
    
- Deployed via Vercel

---

## Features & Implementation

### Structure & Architecture

The portfolio is built as a **Next.js application integrated with Prismic CMS**, where routing and page rendering are driven by dynamic content models rather than hard-coded pages. Content is authored in the Prismic dashboard and fetched via API, then mapped to React components and page templates on the frontend.

This setup enables a flexible content architecture in which pages and sections can be reorganized directly from Prismic without requiring code changes. Dynamic routes (such as `[uid]/page.tsx`) are generated at build time or on demand based on Prismic document UIDs. The overall layout and routing logic live in the `app` directory, with a central layout file managing global structure and nested page files handling individual content views.

Architecturally, the project follows a **headless CMS pattern**, decoupling content management from presentation. This allows the client to control site content and structure independently while I focus on UI, routing, and performance. Next.js provides static generation and server-side rendering, which are well suited for a portfolio site, while Prismic’s Slice Machine and custom types enable modular, reusable content blocks.

This combination supports scalability and ease of maintenance, allowing new pages and sections to be added entirely through Prismic without modifying frontend routes—an essential requirement for the client.

---

### Interactivity

For interactivity, the site includes a **server-side API endpoint using Nodemailer** to handle contact form submissions. When a user submits an inquiry, an email is sent to the client using predefined mail options.

```ts
const mailOptions = {
	from: email,
	to: process.env.EMAIL_TO,
	subject: `Nuevo mensaje de ${name}`,
	text: `Message from ${name} (${email}):\n\n${message}`,
};

try {
	const info = await transporter.sendMail(mailOptions);
	return new Response(JSON.stringify({ success: true }), { status: 200 });
} catch (error: unknown) {
	if (error instanceof Error) {
		return new Response(
			JSON.stringify({ success: false, error: error.message }),
			{ status: 500 }
		);
	} else {
		return new Response(
			JSON.stringify({ success: false, error: "An unknown error occurred." }),
			{ status: 500 }
		);
	}
}
```

This works in tandem with the contact component, which **obfuscates the client’s email address** and only decrypts it when the user actively clicks. This prevents email scraping by bots and helps reduce spam, as requested by the client.

```ts
/**
 * Encrypt email address with a simple obfuscation method.
 */
const obfuscateEmail = (email: string): string => {
	return btoa(email); // Base64 encode the email
};

/**
 * Decrypt the obfuscated email address.
 */
const deobfuscateEmail = (encodedEmail: string): string => {
	return atob(encodedEmail); // Base64 decode the email
};

/**
 * Component for "Contact" Slices.
 */
const Contact = ({ slice }: ContactProps): JSX.Element => {
	const encryptedEmail = obfuscateEmail(slice.primary.email || "");

	const handleEmailClick = () => {
		const email = deobfuscateEmail(encryptedEmail);
		window.location.href = `mailto:${email}`;
	};
};
```

---

### Layout & Responsiveness

The layout is built using **Tailwind CSS with Flexbox and Grid**, following a mobile-first approach. Breakpoints are carefully applied to ensure consistent typography, spacing, and image presentation across devices. Image-heavy sections are optimized for responsiveness and usability, particularly for photography-focused content.

---

## Responsive Strategy

- **Mobile-first:** Yes
    
- **Breakpoints:** Mobile / Tablet / Desktop
    
- **Assets:** Uses `yet-another-react-lightbox` to support high-quality image galleries

---

## Challenges & Solutions

- **Challenge:** Implementing language context correctly across routes when using a headless CMS. Managing language overrides between browser settings, routing, and Prismic content required careful handling.
    
- **Solution:** Introduced a language provider that syncs browser language detection, session storage, and route handling. This ensured consistent language behavior across navigation and page reloads.

```ts
export const LanguageProvider = ({ children }: { children: ReactNode }) => {
	const [lang, setLangState] = useState("es-mx"); // Default language
	const router = useRouter();
	const pathname = usePathname();

	useEffect(() => {
		if (typeof window !== "undefined") {
			const savedLang = sessionStorage.getItem("lang");
			if (savedLang) {
				setLangState(savedLang);
			} else {
				const browserLang = navigator.language;
				const normalizedLang =
					browserLang.toLowerCase() === "en-us" ? "en-us" : "es-mx";
				setLangState(normalizedLang);
				sessionStorage.setItem("lang", normalizedLang);
			}
		}
	}, []);
};
```

---

## Key Learnings

1. Implementing bilingual (English / Spanish) content with dynamic routing using Prismic
    
2. Securing contact information by encrypting emails and decrypting only on user interaction, combined with server-side email handling via Nodemailer
    
3. Integrating a lightbox solution to support high-quality photography galleries

---

## Notes / Improvements

- Image preloading or caching could further improve performance and perceived load times, especially for gallery-heavy pages.# Alejandra Leyva Journalist Portfolio Site

**Type:** Client  
**Source:** FoodLovers – Alejandra Leyva  
**Repository:** [https://github.com/toonchavez8/alejandra-leyva-portfolio](https://github.com/toonchavez8/alejandra-leyva-portfolio)  
**Live Site:** [https://alejandra-leyva.com/](https://alejandra-leyva.com/)

---

## Overview

A portfolio website for photojournalist **Alejandra Leyva** designed to showcase her projects and published work. The site allows the client to create and manage new project pages through a CMS and supports bilingual content in both English (`eng`) and Spanish (`esp`).

---

## Objectives

- Design the portfolio using **Figma**
    
- Build a fully responsive site connected to a CMS
    
- Support local language switching (English / Spanish)

---

## Tech Stack

- Figma
    
- Next.js, Tailwind CSS
    
- Prismic IO (Headless CMS)
    
- Deployed via Vercel

---

## Features & Implementation

### Structure & Architecture

The portfolio is built as a **Next.js application integrated with Prismic CMS**, where routing and page rendering are driven by dynamic content models rather than hard-coded pages. Content is authored in the Prismic dashboard and fetched via API, then mapped to React components and page templates on the frontend.

This setup enables a flexible content architecture in which pages and sections can be reorganized directly from Prismic without requiring code changes. Dynamic routes (such as `[uid]/page.tsx`) are generated at build time or on demand based on Prismic document UIDs. The overall layout and routing logic live in the `app` directory, with a central layout file managing global structure and nested page files handling individual content views.

Architecturally, the project follows a **headless CMS pattern**, decoupling content management from presentation. This allows the client to control site content and structure independently while I focus on UI, routing, and performance. Next.js provides static generation and server-side rendering, which are well suited for a portfolio site, while Prismic’s Slice Machine and custom types enable modular, reusable content blocks.

This combination supports scalability and ease of maintenance, allowing new pages and sections to be added entirely through Prismic without modifying frontend routes—an essential requirement for the client.

---

### Interactivity

For interactivity, the site includes a **server-side API endpoint using Nodemailer** to handle contact form submissions. When a user submits an inquiry, an email is sent to the client using predefined mail options.

```ts
const mailOptions = {
	from: email,
	to: process.env.EMAIL_TO,
	subject: `Nuevo mensaje de ${name}`,
	text: `Message from ${name} (${email}):\n\n${message}`,
};

try {
	const info = await transporter.sendMail(mailOptions);
	return new Response(JSON.stringify({ success: true }), { status: 200 });
} catch (error: unknown) {
	if (error instanceof Error) {
		return new Response(
			JSON.stringify({ success: false, error: error.message }),
			{ status: 500 }
		);
	} else {
		return new Response(
			JSON.stringify({ success: false, error: "An unknown error occurred." }),
			{ status: 500 }
		);
	}
}
```

This works in tandem with the contact component, which **obfuscates the client’s email address** and only decrypts it when the user actively clicks. This prevents email scraping by bots and helps reduce spam, as requested by the client.

```ts
/**
 * Encrypt email address with a simple obfuscation method.
 */
const obfuscateEmail = (email: string): string => {
	return btoa(email); // Base64 encode the email
};

/**
 * Decrypt the obfuscated email address.
 */
const deobfuscateEmail = (encodedEmail: string): string => {
	return atob(encodedEmail); // Base64 decode the email
};

/**
 * Component for "Contact" Slices.
 */
const Contact = ({ slice }: ContactProps): JSX.Element => {
	const encryptedEmail = obfuscateEmail(slice.primary.email || "");

	const handleEmailClick = () => {
		const email = deobfuscateEmail(encryptedEmail);
		window.location.href = `mailto:${email}`;
	};
};
```

---

### Layout & Responsiveness

The layout is built using **Tailwind CSS with Flexbox and Grid**, following a mobile-first approach. Breakpoints are carefully applied to ensure consistent typography, spacing, and image presentation across devices. Image-heavy sections are optimized for responsiveness and usability, particularly for photography-focused content.

---

## Responsive Strategy

- **Mobile-first:** Yes
    
- **Breakpoints:** Mobile / Tablet / Desktop
    
- **Assets:** Uses `yet-another-react-lightbox` to support high-quality image galleries

---

## Challenges & Solutions

- **Challenge:** Implementing language context correctly across routes when using a headless CMS. Managing language overrides between browser settings, routing, and Prismic content required careful handling.
    
- **Solution:** Introduced a language provider that syncs browser language detection, session storage, and route handling. This ensured consistent language behavior across navigation and page reloads.

```ts
export const LanguageProvider = ({ children }: { children: ReactNode }) => {
	const [lang, setLangState] = useState("es-mx"); // Default language
	const router = useRouter();
	const pathname = usePathname();

	useEffect(() => {
		if (typeof window !== "undefined") {
			const savedLang = sessionStorage.getItem("lang");
			if (savedLang) {
				setLangState(savedLang);
			} else {
				const browserLang = navigator.language;
				const normalizedLang =
					browserLang.toLowerCase() === "en-us" ? "en-us" : "es-mx";
				setLangState(normalizedLang);
				sessionStorage.setItem("lang", normalizedLang);
			}
		}
	}, []);
};
```

---

## Key Learnings

1. Implementing bilingual (English / Spanish) content with dynamic routing using Prismic
    
2. Securing contact information by encrypting emails and decrypting only on user interaction, combined with server-side email handling via Nodemailer
    
3. Integrating a lightbox solution to support high-quality photography galleries

---

## Notes / Improvements

- Image preloading or caching could further improve performance and perceived load times, especially for gallery-heavy pages.