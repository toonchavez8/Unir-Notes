Actividad 3. Integración y despliegue de una aplicación web

Las tres actividades que se llevarán a cabo en la asignatura Desarrollo Web Integral tienen como objetivo:

- Desarrollar un front-end haciendo uso de HTML5, CSS3, JavaScript y React.
- Desarrollar un back-end haciendo uso de una arquitectura orientada a microservicios, donde cada microservicio expondrá una API REST haciendo uso de Java, y Spring.
- Integrar ambas partes y desplegar front-End y back-end tanto en local como de forma pública.
- Hacer uso de bases de datos relacionales y del motor de búsqueda Elasticsearch.

Ilustración 1 - Arquitectura de la aplicación a desarrollar en la asignatura. Fuente: Elaboración propia

Esta tercera actividad consiste en la integración del front-end y el back-end realizado en las actividades anteriores y su despliegue mediante contenedores Docker.

**Pautas de elaboración**

En las dos actividades anteriores hemos construido:

- El front-end de una aplicación web (hasta ahora, con datos de prueba o mock).
- El back-end encargado de dar servicio a ese front-end (con referencias a máquinas locales), que se expone a través del servidor perimetral Cloud Gateway.

En esta actividad se deberá realizar lo siguiente:

- **Integrar el front-end y el back-end_._** Para esto será necesario modificar los componentes de React que se encargaban de acceder a los datos de prueba para que ahora hagan peticiones HTTP al back-end (**siempre al servidor perimetral**). Con las siguientes consideraciones:
    - El microservicio buscador dejará de usar una base de datos relacional y **pasará a utilizar un clúster de Elasticsearch** cuyo modelo de datos será similar al que se tenía en el modelo relacional. Debes **analizar** qué campos de tu modelo de datos del microservicio buscador pueden ser text, keyword, search-as-you-type…
    - El front-end debe **beneficiarse de este cambio en la implementación del back-end** (debe permitir búsquedas que utilicen internamente campos search as you type de Elasticsearch o búsquedas full-text, así como **facets**).
- **Desplegar todos los componentes de la arquitectura en local mediante contenedores Docker, a excepción del front-end, que estará desplegado de forma local, como se ha venido haciendo.** Tenemos los siguientes componentes desarrollados:
    - Front-end: una aplicación desarrollada con JavaScript y React.
    - Back-end: servidor perimetral Cloud Gateway, servidor de registro Eureka, microservicio buscador y microservicio operador.
- **Para llegar a la máxima nota será necesario desplegar todos los componentes de la arquitectura en Internet de forma pública haciendo uso de Vercel y Railway o herramientas similares (AWS, Azure…).**

La entrega consistirá en **un único archivo ZIP** que contendrá:

- **Vídeo memoria** **obligatoria** en formato MP4 de la actividad.
- **Proyectos con el código del front-end, Eureka, Cloud Gateway y microservicios.** Un directorio por proyecto, **sin comprimir**. Se incluye todo el contenido del proyecto **sin la carpeta target y sin la carpeta node_modules.**
- En caso de ser necesario, archivos SQL con sentencias DDL y DML necesarias para disponer del mismo conjunto de datos que se ha usado durante el desarrollo.

**Extensión y formato de la vídeo memoria**

La vídeo memoria tendrá una duración aproximada de 15 minutos y deberá visitar los siguientes aspectos de tu actividad:

1. **Modificaciones realizadas en el front-end:** se describirán brevemente las modificaciones que han sido necesarias en el front-end para lograr la integración con el back-end.
2. **Modificaciones realizadas en el back-end:** se describirán brevemente las modificaciones que han sido necesarias en el back-end para lograr la integración con el front-end y las consideraciones que se hayan tenido en cuenta para migrar del modelo relacional a Elasticsearch.
3. **Despliegue local:** se mostrarán los Dockerfile de los diferentes componentes del back-end, así como las evidencias de que la aplicación se está ejecutando correctamente.
4. **Despliegue remoto:** se mostrarán los diferentes componentes del back-end y front-end desplegados de forma pública, así como las evidencias de que la aplicación se está ejecutando correctamente.
5. **Conclusiones:** añade cualquier comentario que desees, así como _feedback_.

Rúbrica
# Rúbrica de Evaluación

## Criterio 7 – Ortografía
- Penalización de **-0.25 puntos** por cada cinco faltas de acentuación.  
- Penalización de **-0.10 puntos** por cada falta de ortografía.  

---

## Rúbrica de criterios técnicos
| **Criterio**                                                                                      | **0 points**                                                                                                | **0.75 points**                                                                                            | **1.13 points**                                                                                             | **Máxima puntuación**                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Criterio 1 Modificación del microservicio buscador para utilizar Elasticsearch**                | Las modificaciones realizadas no son suficientes y el código no se ejecuta correctamente. <br> **0 points** | Las modificaciones realizadas funcionan pero el modelado de los datos no es correcto. <br> **0.75 points** | Las modificaciones realizadas funcionan y modelado de los datos es correcto. <br> **1.13 points**           | Las modificaciones realizadas funcionan y modelado de los datos es correcto. Además, se han tenido en cuenta consideraciones de seguridad para trabajar con las credenciales de acceso a Elasticsearch. <br> **1.5 points** |
| **Criterio 2 Uso de Elasticsearch para realizar sugerencias, correcciones o búsquedas full-text** | No se realizan sugerencias, correcciones ni búsquedas full-text. <br> **0 points**                          | Se realizan búsquedas full-text sobre muy pocos atributos. <br> **0.75 points**                            | Se realizan búsquedas full-text sobre todos los atributos sobre los que tiene sentido. <br> **1.13 points** | Se realizan búsquedas full-text sobre todos los atributos sobre los que tiene sentido, así como la posibilidad de implementar correcciones o sugerencias. <br> **1.5 points**                                               |
| **Criterio 3 Uso de Elasticsearch para implementar facets**                                       | No se utilizan facets. <br> **0 points**                                                                    | Se utilizan facets para un número limitado de atributos. <br> **0.75 points**                              | Se utilizan facets para todos los atributos que lo puedan necesitar. <br> **1.13 points**                   | Se utilizan facets para todos los atributos que lo puedan necesitar. Los rangos devueltos son adecuados y permiten un buen nivel de experiencia de búsqueda. <br> **1.5 points**                                            |
| **Criterio 4 Integración de front-end y back-end en local**                                       | No se realiza. <br> **0 points**                                                                            | Se realiza con fallos en menos de dos componentes. <br> **1.25 points**                                    | Se realiza sin fallos. <br> **1.88 points**                                                                 | Se realiza sin fallos y el CORS está configurado a nivel GW. <br> **2.5 points**                                                                                                                                            |
| **Criterio 5 Modificación del estilo con CSS**                                                    | No se realiza. <br> **0 points**                                                                            | Se realiza correctamente para front o back, pero no ambos. <br> **1 point**                                | Se realiza correctamente para front y back. <br> **1.5 points**                                             | Se realiza correctamente para front y back. El CORS está configurado a nivel GW y únicamente el GW es accesible públicamente. <br> **2 points**                                                                             |
| **Criterio 6 Vídeo memoria obligatoria**                                                          | No hay vídeo memoria. <br> **0 points**                                                                     | Vídeo memoria demasiado corto o que no cubre todos los aspectos. <br> **0.5 points**                       | Vídeo memoria que cubre todos los aspectos pero no entra en detalle en ellos. <br> **0.75 points**          | Duración adecuada y cobertura de todos los aspectos solicitados. <br> **1 point**                                                                                                                                           |





----

Issue 1 — Asegurar que el servicio Search use Elasticsearch con mapping correcto (search_as_you_type, text, keyword)

- Observación: Existe ElasticsearchConfig.java y entidades — la integración está iniciada.
- Conclusión: Parcial — no garantiza mapping correcto para search_as_you_type/keyword/text.
- Dónde corregir: [Items.java](vscode-file://vscode-app/c:/Users/FoodLovers/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) y [ElasticsearchConfig.java](vscode-file://vscode-app/c:/Users/FoodLovers/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)
- Pasos:
    1. Anotar campos de la entidad con los tipos @Field apropiados (Text, Keyword, Search_As_You_Type).
    2. Asegurar que el índice se cree con el mapping en ElasticsearchConfig al arrancar.
- Ejemplo mínimo para añadir en ElasticsearchConfig (crear índice si no existe):

```Java
// ...existing code...
// add an index creation method (pseudo)
public void ensureIndex(RestHighLevelClient client) throws IOException {
    String index = "items";
    GetIndexRequest get = new GetIndexRequest(index);
    if (!client.indices().exists(get, RequestOptions.DEFAULT)) {
        CreateIndexRequest req = new CreateIndexRequest(index);
        req.settings(Settings.builder()
            .put("index.number_of_shards", 1)
            .put("index.number_of_replicas", 0)
        );
        String mapping = """
        {
          "properties": {
            "id": { "type": "keyword" },
            "name": { "type": "search_as_you_type" },
            "description": { "type": "text" },
            "category": { "type": "keyword" },
            "brand": { "type": "keyword" },
            "price": { "type": "double" }
          }
        }
        """;
        req.mapping(mapping, XContentType.JSON);
        client.indices().create(req, RequestOptions.DEFAULT);
    }
}
// ...existing code...
```

Issue 2 — Implementar endpoints de búsqueda full-text, sugerencias (autocomplete) y fuzzy/correcciones

- Observación: SearchAPI e InnerSearch existen pero se desconoce si soportan multi_match, completion y fuzzy.
- Conclusión: Parcial/No completo para la nota máxima.
- Dónde corregir: [SearchAPI.java](vscode-file://vscode-app/c:/Users/FoodLovers/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) y search/service/InnerSearch.java
- Pasos:
    1. Añadir endpoint /search?q= que realice multi_match sobre campos text con fuzziness.
    2. Añadir endpoint /suggest?q= que use el campo search_as_you_type con prefix.
- Ejemplo mínimo de endpoints en el controlador:

```Java
// ...existing code...
@GetMapping("/search")
public ResponseEntity<?> search(@RequestParam String q, @RequestParam(defaultValue="0") int page) {
    // call service.searchFullText(q, page)
    // return results
}

@GetMapping("/suggest")
public ResponseEntity<?> suggest(@RequestParam String q) {
    // call service.suggest(q) -> use prefix/search_as_you_type
    // return suggestions
}
// ...existing code...
```

Issue 3 — Implementar facets (aggregaciones) y rangos de precio

- Observación: No se ven endpoints explícitos de agregaciones en el árbol.
- Conclusión: No cumple para nota máxima.
- Dónde corregir: search/service/InnerSearch.java y SearchAPI.java
- Pasos:
    1. Añadir endpoint /facets que devuelva buckets de agregaciones para categoría, marca y rangos numéricos de precio.
    2. Usar terms aggs para campos categóricos y range aggs para precio.
- Ejemplo mínimo de agregaciones:

```java
// ...existing code...
SearchSourceBuilder source = new SearchSourceBuilder();
source.aggregation(AggregationBuilders.terms("by_category").field("category.keyword"));
source.aggregation(AggregationBuilders.terms("by_brand").field("brand.keyword"));
source.aggregation(AggregationBuilders.range("price_ranges").field("price")
    .addUnboundedTo("cheap", 50)
    .addRange("mid", 50, 200)
    .addUnboundedFrom("expensive", 200));
```

Issue 4 — Front-end debe usar únicamente el Gateway y aprovechar características de ES

- Observación: El front-end tiene services.js, componente Facets y mocks/data.json; no está claro si llama al Gateway.
- Conclusión: Parcial — probablemente está usando mocks; hay que asegurar que todas las llamadas vayan al Gateway y consuman /search, /suggest, /facets.
- Dónde corregir: [services.js](vscode-file://vscode-app/c:/Users/FoodLovers/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) (o api/index.js) y componentes que usan mocks.
- Pasos:
    1. Reemplazar llamadas a mocks por fetch al URL base del Gateway (usar variable de entorno VITE_API_URL).
    2. Actualizar UI de búsqueda para llamar a /search, /suggest, /facets a través del Gateway.
- Cambio mínimo en services.js:

```js
// ...existing code...
const BASE = import.meta.env.VITE_API_URL || 'http://localhost:8080';
export async function search(q) {
  return fetch(`${BASE}/search-service/search?q=${encodeURIComponent(q)}`).then(r=>r.json());
}
export async function suggest(q) {
  return fetch(`${BASE}/search-service/suggest?q=${encodeURIComponent(q)}`).then(r=>r.json());
}
export async function facets() {
  return fetch(`${BASE}/search-service/facets`).then(r=>r.json());
}
// ...existing code...
```

Eres Un genio de codigo, pero me queires educar y ayudar a crear issues en github, te voy a psar un issue que tengo definido mejoramelo y punta hacia donde tengo detalles y lo que pasos que me recomiedas tomar y que criteros de acceptadcion de beriad e tomar para que complete el issue y los tipos de purebas y vagamente como serian esas pruebas

Issue 5 — Configurar CORS solo en Cloud Gateway y restringir acceso directo a microservicios

- Observación: cloud-gateway existe y contiene docker-compose; requiere configuración explícita de CORS.
- Conclusión: No verificado — probablemente necesita configuración.
- Dónde corregir: [application.yml](vscode-file://vscode-app/c:/Users/FoodLovers/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)
- Pasos:
    1. Añadir configuración de CORS en el gateway permitiendo únicamente el origen del front-end.
    2. Asegurarse de que los microservicios no permitan CORS abierto.
- Fragmento mínimo para application.yml:

```yml
# ...existing code...
spring:
  cloud:
    gateway:
      globalcors:
        corsConfigurations:
          '[/**]':
            allowedOrigins: "http://localhost:5173" # origen del front-end
            allowedMethods:
              - GET
              - POST
              - PUT
              - DELETE
            allowedHeaders: "*"
# ...existing code...
```

Issue 6 — Docker: composer stack local con Elasticsearch, Eureka, Search, Operator, Gateway

- Observación: Hay Dockerfiles; cloud-gateway tiene docker-compose.*, pero no hay un compose raíz que incluya Elasticsearch y todos los servicios.
- Conclusión: No cumple para despliegue local reproducible.
- Dónde corregir: Crear docker-compose.dev.yml en raíz o actualizar [docker-compose.dev.yml](vscode-file://vscode-app/c:/Users/FoodLovers/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) para incluir todos los servicios.
- Pasos:
    1. Añadir docker-compose que levante: elasticsearch, eureka, operator, search, cloud-gateway (solo gateway publicado) y una red.
    2. Exponer únicamente el puerto del gateway públicamente.
- Ejemplo mínimo de docker-compose:  `--watch`

```Dockerfile
version: '3.8'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.9.0
    environment:
      - discovery.type=single-node
      - ELASTIC_PASSWORD=${ES_PASSWORD}
    ports:
      - "9200:9200"
    volumes:
      - esdata:/usr/share/elasticsearch/data
  eureka:
    build: ./eureka
    environment:
      - SPRING_PROFILES_ACTIVE=dev
    networks:
      - backend
  search:
    build: ./search
    environment:
      - ES_HOST=http://elasticsearch:9200
      - ES_USER=elastic
      - ES_PASSWORD=${ES_PASSWORD}
    networks:
      - backend
  operator:
    build: ./operator
    networks:
      - backend
  cloud-gateway:
    build: ./cloud-gateway
    ports:
      - "8080:8080" # only gateway exposed
    networks:
      - backend
volumes:
  esdata:
networks:
  backend:
    driver: bridge
```

Issue 7 — Archivos de entorno y seguridad de credenciales

- Observación: Hay .env y test.env; es necesario .env.template y no subir secretos.
- Conclusión: Parcial — requiere ajustes para nota máxima.
- Dónde corregir: Raíz de cada servicio (search/, operator/, cloud-gateway/, eureka/, inventario-front/)
- Pasos:
    1. Añadir .env.template con nombres de variables pero sin valores.
    2. Eliminar secretos del repo y añadir .env a .gitignore.
- Ejemplo .env.template para search:

```bash
ES_HOST=http://localhost:9200
ES_USER=elastic
ES_PASSWORD=changeme
SPRING_PROFILES_ACTIVE=dev
SERVER_PORT=9001
```

Issue 8 — UX de facets y que el front aproveche las características de ES

- Observación: Existe componente Facets; necesita conexión con facets del back-end y sugerencias.
- Conclusión: Parcial — el front debe consumir /facets y /suggest para beneficiarse.
- Dónde corregir: [Facets.jsx](vscode-file://vscode-app/c:/Users/FoodLovers/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) y endpoints de search.
- Pasos:
    1. Conectar el componente Facets para llamar a facets() y actualizar filtros.
    2. Conectar input de búsqueda a suggest() para autocompletado.

Issue 9 — Verificación de Eureka / service discovery

- Observación: El módulo eureka existe y probablemente registre servicios.
- Conclusión: Probablemente OK pero se debe confirmar en tiempo de ejecución.
- Dónde corregir: Revisar application.yml de cada servicio para eureka.client.serviceUrl.defaultZone y spring.application.name.
- Pasos rápidos:
    - Levantar stack y comprobar UI de Eureka en su puerto; verificar servicios registrados.

Issue 10 — Documentación y trazabilidad para corrección/grading

- Observación: README parciales.
- Conclusión: No completo para nota máxima.
- Dónde corregir: Añadir README en raíz con pasos para ejecutar localmente (docker-compose), cómo configurar .env y lista de endpoints (search, suggest, facets).
- Comandos mínimos a documentar:
    - Definir ES_PASSWORD en .env
    - docker compose -f docker-compose.dev.yml up --build
    - npm install && npm run dev (front-end)

Resumen de comprobación (puedes copiarlo como checklist):

- [ ]  Añadir/verificar mappings con search_as_you_type y tipos keyword/text.
- [ ]  Añadir endpoints de búsqueda: full-text (multi_match + fuzziness), suggest (search_as_you_type).
- [ ]  Añadir endpoint de facets (terms y rangos).
- [ ]  Actualizar front-end para usar el Gateway y consumir los nuevos endpoints; eliminar mocks.
- [ ]  Configurar CORS únicamente en cloud-gateway.
- [ ]  Crear docker-compose.dev.yml que levante ES + todos los servicios; exponer solo el gateway.
- [ ]  Añadir .env.template en cada servicio y eliminar secretos.
- [ ]  Asegurar registro en Eureka para todos los servicios.
- [ ]  Añadir README con pasos para ejecutar y desplegar.

Puedo generar cambios concretos (mappings en Items.java y ElasticsearchConfig, controladores de búsqueda, docker-compose y .env.template). Indica cuál quieres que genere primero y lo scaffoldeo.


```bash

```


