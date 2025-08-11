# Guion de Video - Aplicación de Gestión de Campañas D&D

_Duración objetivo: 6 minutos_

---

## 1. INTRODUCCIÓN (1 minuto)

**[Pantalla: Logo/Título de la aplicación]**

"Hola, en este video les presento mi aplicación de gestión de campañas para Dungeons & Dragons, desarrollada con React y TypeScript.

**¿Por qué esta aplicación?** Los Dungeon Masters necesitan una herramienta centralizada para gestionar todos los elementos de sus campañas: sesiones, NPCs, ubicaciones, tiendas e inventarios. Esta aplicación resuelve ese problema ofreciendo una interfaz intuitiva y completa.

**Tecnologías principales:**

- React con TypeScript para type safety
- React Router para navegación
- CSS con metodología BEM y variables personalizadas
- Hooks personalizados para gestión de estado"

---

## 2. COMPONENTES DE REACT (1.5 minutos)

**[Pantalla: Estructura de carpetas del proyecto]**

"La aplicación está organizada en varios componentes principales:

**Páginas principales:**

- `Campaigns` - Lista y gestión de campañas
- `Sessions` - Gestión de sesiones de juego con funcionalidad de edición inline
- `NPCs` - Catálogo de personajes no jugables
- `Shops` - Tiendas con inventario editable en tabla flex
- `Locations` - Ubicaciones del mundo de juego
- `Items` - Gestión de objetos y equipamiento

**Componentes reutilizables:**

- `ShopInventory` - Componente extraído para gestión de inventarios
- `ItemForm` - Formulario reutilizable para crear/editar items
- `ShopForm` - Formulario para tiendas

**Enrutador utilizado:** Usamos React Router v6 con un array de rutas configurado en `siteRoutes.ts` que maneja:

- Rutas principales como `/campaigns`, `/sessions`
- Rutas anidadas como `/campaigns/:id/sessions/:sessionId`
- Rutas de creación con patrón consistente `/entity/create/new`"

---

## 3. HOOKS UTILIZADOS (1.5 minutos)

**[Pantalla: Código de hooks personalizados]**

"**Hooks nativos de React utilizados:**

- `useState` - Gestión de estado local en todos los componentes
- `useEffect` - Efectos secundarios y carga de datos
- `useNavigate` y `useParams` - Navegación y parámetros de URL

**Hook personalizado principal: `useCampaigns`** Este es el corazón de la aplicación. Centraliza toda la lógica de negocio:

const { 

  campaigns, sessions, npcs, shops, locations, items,

  createCampaign, updateCampaign, deleteCampaign,

  createShop, updateShop, // ... y más funciones CRUD

} = useCampaigns();

- 
- 
- 
- 

**¿Por qué es necesario?**

- **Centralización**: Evita duplicación de lógica entre componentes
- **Consistencia**: Todas las operaciones CRUD siguen el mismo patrón
- **Mantenibilidad**: Cambios en la lógica de datos se hacen en un solo lugar
- **Performance**: Gestión eficiente del estado global

**Valor que aporta:** Permite que cualquier componente acceda y modifique datos sin prop drilling, manteniendo la consistencia en toda la aplicación."

---

## 4. VISTAS Y DEMOSTRACIÓN (2 minutos)

**[Pantalla: Terminal corriendo npm run dev]**

"**Arranque local:**

npm install

npm run dev

- 
- 
- 
- 

Ahora veamos las vistas principales:

**[Mostrar cada vista brevemente]**

**1. Dashboard de Campañas**

- Grid responsivo con cards
- Filtros por estado y búsqueda
- Estilos: BEM con variables CSS personalizadas, gradientes en botones

**2. Gestión de Sesiones**

- Tabla flexible convertida de HTML table a flex grid
- Edición inline activada por parámetro URL `?edit=true`
- CSS destacable: Transiciones suaves, estados de edición, modal de confirmación

**3. Inventario de Tiendas**

- Componente `ShopInventory` extraído para reutilización
- Tabla editable con inputs inline para precio, cantidad y disponibilidad
- Modal de selección de items con búsqueda en tiempo real
- Estilos: Flex grid que se convierte en cards en mobile

**4. Formularios (Items/Shops)**

- Componente `ItemForm` reutilizable para crear/editar
- Validación visual con estados de error
- Layout de dos columnas: formulario principal + sidebar con imagen
- CSS: Variables para colores, spacing consistente con `--primary-color`, `--surface-color`"

---

## 5. CARACTERÍSTICAS TÉCNICAS DESTACADAS (30 segundos)

**[Pantalla: Código CSS con variables]**

"**Metodología CSS:**

- BEM para nomenclatura consistente: `.shop-detail__inventory-row--editing`
- Variables CSS centralizadas en `_variables.css`
- Responsive design mobile-first
- Componentes autocontenidos con sus propios estilos

**Características de UX:**

- Navegación consistente con breadcrumbs
- Estados de carga con skeleton UI
- Confirmaciones para acciones destructivas
- Edición inline sin cambio de página"

---

## 6. CONCLUSIÓN (30 segundos)

**[Pantalla: Vista general de la aplicación]**

"Esta aplicación demuestra:

- Arquitectura escalable con componentes reutilizables
- Gestión eficiente del estado con hooks personalizados
- Diseño responsive con metodología BEM
- UX intuitiva para gestión completa de campañas D&D

El resultado es una herramienta completa que centraliza toda la información necesaria para Dungeon Masters, con una interfaz moderna y fácil de usar.

¡Gracias por su atención!"

---

## TIPS PARA LA GRABACIÓN:

1. **Preparar ventanas:** Tener abiertas las vistas principales
2. **Código limpio:** Mostrar solo archivos relevantes
3. **Navegación fluida:** Practicar los clics entre secciones
4. **Velocidad:** Hablar claro pero dinámico para cumplir los 6 minutos
5. **Highlights:** Enfatizar la edición inline, el modal de items, y los hooks personalizados