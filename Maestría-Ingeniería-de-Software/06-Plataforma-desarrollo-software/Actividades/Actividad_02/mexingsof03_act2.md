# Actividad 2: Integrando Servicios REST En .NET

Recuerda que esta actividad deberá set completada en la plataforma. Solo tendrás un intento. Una vez que la envíes, se dará por cerrada. Tu puntuación y las respuestas correctas se mostrarán cuando finalice el periodo de entrega de la tarea.

---

## Descripción De la Actividad Y Pautas De Elaboración

En esta actividad vamos a aprender a integrar servicios REST de terceros utilizando diversos métodos desde el entorno de .NET. Para ello, supondremos que vamos a tener que consumir un servicio REST de un backend externo como es el sistema **Pet-Clinic**. Se trata de un proyecto clásico para aprender a programar con el framework Spring de Java y que tiene diversas implementaciones en su [comunidad](https://spring-petclinic.github.io/).

Para esta práctica vamos a utilizar la implementación sobre una arquitectura cliente servidor.

### Repositorios

- **Backend:** <https://github.com/spring-petclinic/spring-petclinic-rest>  

- **Frontend:** <https://github.com/spring-petclinic/spring-petclinic-angular>  

Puedes descargar su código fuente (haciendo un `git clone`) o utilizar la copia adjunta al enunciado.

---

## Requisitos Para El Entorno Local

- Una versión de la máquina virtual de Java, por ejemplo [OpenJDK11](https://adoptopenjdk.net/).

- [Maven](https://maven.apache.org/download.cgi).

- [Node.js](https://nodejs.org/es/download/).

---

## Ejecución Del Backend

Primero lanzamos el backend con la instrucción:

```bash

./mvnw spring-boot:run

````

(o `mvnw.cmd` en Windows)

Comprobamos que los servicios están activos mediante Swagger en:

<http://localhost:9966/petclinic/swagger-ui/index.html>

![[mexingsof03_act2.png]]

---

## Ejecución Del Frontend (opcional)

Para entender el funcionamiento del sistema puedes lanzar el frontend con:

```bash

ng serve

```

Y acceder al interfaz gráfico desde:

```Python

http://localhost:4200/petclinic/welcome

```

![[mexingsof03_act2.jpeg]]

---

## Acceso Al API REST

Los servicios REST del backend se pueden consultar desde:

```Python

http://localhost:9966/petclinic/v3/api-docs

```

O bien pulsando donde se señala con un recuadro rojo en la siguiente figura, en el que sale el enlace a `/petclinic/v3/api-docs`:

![[mexingsof03_act2 1.png]]

El API está definido conforme al estándar **OpenAPI** y se especifica en formato JSON:

![[mexingsof03_act2 2.png]]

---

## Pregunta 1 – Consumo Básico Con HttpClient

Crea un proyecto en .NET de tipo consola con el siguiente código:

```csharp

using System;

using System.Net.Http;

using System.Threading.Tasks;

  

namespace ConsoleApp

{

    internal class Pregunta1

    {

        static readonly HttpClient client = new HttpClient();

  

        static async Task Main()

        {

            try

            {

                using HttpResponseMessage response =

                    await client.GetAsync("http://localhost:9966/petclinic/api/vets");

  

                if (response.IsSuccessStatusCode)

                {

                    string responseBody = await response.Content.ReadAsStringAsync();

                    Console.WriteLine(responseBody);

                }

            }

            catch (Exception e)

            {

                Console.WriteLine(e.Message);

            }

  

            Console.ReadLine();

        }

    }

}

```

**Indica cuál es el resultado esperado tras la ejecución:**

1. Muestra una excepción.

2. No compila porque hay errores en el código.

3. Muestra en pantalla un json que empieza por  

    `[{"firstName":"James","lastName":"Carter"…`

1. Muestra en pantalla un XML que empieza por `<vetList>`.

**Respuesta:** 3

**Justificación:** El endpoint `/api/vets` devuelve JSON y el código compila y lee el cuerpo correctamente si el backend está levantado.

**Validación:** Ejecuta el programa con el backend activo y comprueba que se imprime un JSON que comienza con los datos de los veterinarios.

---

## Pregunta 2 – Mapeo a Modelo De Datos

```csharp

using System;

using System.Net.Http;

using System.Threading.Tasks;

using System.Collections.Generic;

using System.Text.Json;

  

namespace ConsoleApp

{

    internal class Pregunta2

    {

        static readonly HttpClient client = new HttpClient();

  

        public class VetSpeciality

        {

            public int id { get; set; }

            public string name { get; set; }

        }

  

        public class Vet

        {

            public int id { get; set; }

            public string firstName { get; set; }

            public string lastName { get; set; }

            public List<VetSpeciality> specialties { get; set; }

        }

  

        static async Task Main()

        {

            try

            {

                using HttpResponseMessage response =

                    await client.GetAsync("http://localhost:9966/petclinic/api/vets");

  

                if (response.IsSuccessStatusCode)

                {

                    string jsonString = await response.Content.ReadAsStringAsync();

                    List<Vet> vets =

                        JsonSerializer.Deserialize<List<Vet>>(jsonString);

  

                    Console.WriteLine(vets.Count);

                }

            }

            catch (Exception e)

            {

                Console.WriteLine(e.Message);

            }

  

            Console.ReadLine();

        }

    }

}

```

**Resultado esperado:**

1. Muestra un 4.

2. Muestra el mismo json anterior.

3. Sale una excepción.

4. Muestra un 6.

**Respuesta:** 4

**Justificación:** El JSON de `/api/vets` en esta versión devuelve un array plano de `Vet`, por lo que la deserialización a `List<Vet>` funciona y el programa imprime el total de elementos (por defecto, 6).

**Validación:** Abre `http://localhost:9966/petclinic/api/vets` y verifica que el JSON empieza con `[`; al ejecutar el programa debe imprimir `6`.

**Evidencia (consola):**

```text

F:\13-Unir\spring-petclinic-rest\Pregunta2Demo\Program.cs(16,27): warning CS8618: Non-nullable property 'name' must contain a non-null value when exiting constructor. Consider adding the 'required' modifier or declaring the property as nullable. [F:\13-Unir\spring-petclinic-rest\Pregunta2Demo\Pregunta2Demo.csproj]

F:\13-Unir\spring-petclinic-rest\Pregunta2Demo\Program.cs(22,27): warning CS8618: Non-nullable property 'firstName' must contain a non-null value when exiting constructor. Consider adding the 'required' modifier or declaring the property as nullable. [F:\13-Unir\spring-petclinic-rest\Pregunta2Demo\Pregunta2Demo.csproj]

F:\13-Unir\spring-petclinic-rest\Pregunta2Demo\Program.cs(23,27): warning CS8618: Non-nullable property 'lastName' must contain a non-null value when exiting constructor. Consider adding the 'required' modifier or declaring the property as nullable. [F:\13-Unir\spring-petclinic-rest\Pregunta2Demo\Pregunta2Demo.csproj]

F:\13-Unir\spring-petclinic-rest\Pregunta2Demo\Program.cs(24,40): warning CS8618: Non-nullable property 'specialties' must contain a non-null value when exiting constructor. Consider adding the 'required' modifier or declaring the property as nullable. [F:\13-Unir\spring-petclinic-rest\Pregunta2Demo\Pregunta2Demo.csproj]

F:\13-Unir\spring-petclinic-rest\Pregunta2Demo\Program.cs(38,25): warning CS8600: Converting null literal or possible null value to non-nullable type. [F:\13-Unir\spring-petclinic-rest\Pregunta2Demo\Pregunta2Demo.csproj]

F:\13-Unir\spring-petclinic-rest\Pregunta2Demo\Program.cs(40,39): warning CS8602: Dereference of a possibly null reference. [F:\13-Unir\spring-petclinic-rest\Pregunta2Demo\Pregunta2Demo.csproj]

6

```

---

## Pregunta 3 – Consumo Incorrecto Del Endpoint

```csharp

using System;

using System.Net.Http;

using System.Threading.Tasks;

using System.Collections.Generic;

using System.Text.Json;

  

namespace ConsoleApp

{

    internal class Pregunta3

    {

        static readonly HttpClient client = new HttpClient();

  

        public class Visit

        {

            public int id { get; set; }

            public string description { get; set; }

            public int petId { get; set; }

            public DateTime date { get; set; }

  

            public override string ToString()

            {

                return "id: " + id +

                       " Description " + description +

                       " date " + date +

                       " petId " + petId;

            }

        }

  

        static async Task Main()

        {

            try

            {

                using HttpResponseMessage response =

                    await client.GetAsync("http://localhost:9966/petclinic/api/vets");

  

                if (response.IsSuccessStatusCode)

                {

                    string jsonString = await response.Content.ReadAsStringAsync();

                    List<Visit> visits =

                        JsonSerializer.Deserialize<List<Visit>>(jsonString);

  

                    int counter = 0;

                    foreach (Visit v in visits)

                    {

                        Console.WriteLine("Visita " + counter++ + " -> " + v);

                    }

                }

            }

            catch (Exception e)

            {

                Console.WriteLine(e.Message);

            }

  

            Console.ReadLine();

        }

    }

}

```

**Resultado esperado:**

1. Muestra 6 visitas con sus datos.

2. Da un error de compilación.

3. Da un error de ejecución.

4. Muestra las visitas con datos erróneos.

**Respuesta:** 4

**Justificación:** Se consume `/api/vets` pero se intenta deserializar a `Visit`; los campos no coinciden y se muestran valores por defecto (descripcion vacia, fecha minima, `petId` en 0).

**Validación:** Ejecuta el programa y comprueba que imprime visitas con datos incompletos o por defecto al leer un JSON de veterinarios.

**Evidencia (consola):**

```text

F:\13-Unir\spring-petclinic-rest\Pregunta3Demo\Program.cs(17,27): warning CS8618: Non-nullable property 'description' must contain a non-null value when exiting constructor. Consider adding the 'required' modifier or declaring the property as nullable. [F:\13-Unir\spring-petclinic-rest\Pregunta3Demo\Pregunta3Demo.csproj]

F:\13-Unir\spring-petclinic-rest\Pregunta3Demo\Program.cs(41,25): warning CS8600: Converting null literal or possible null value to non-nullable type. [F:\13-Unir\spring-petclinic-rest\Pregunta3Demo\Pregunta3Demo.csproj]

F:\13-Unir\spring-petclinic-rest\Pregunta3Demo\Program.cs(44,41): warning CS8602: Dereference of a possibly null reference. [F:\13-Unir\spring-petclinic-rest\Pregunta3Demo\Pregunta3Demo.csproj]

Visita 0 -> id: 1 Description  date 1/1/0001 12:00:00 AM petId 0

Visita 1 -> id: 2 Description  date 1/1/0001 12:00:00 AM petId 0

Visita 2 -> id: 3 Description  date 1/1/0001 12:00:00 AM petId 0

Visita 3 -> id: 4 Description  date 1/1/0001 12:00:00 AM petId 0

Visita 4 -> id: 5 Description  date 1/1/0001 12:00:00 AM petId 0

Visita 5 -> id: 6 Description  date 1/1/0001 12:00:00 AM petId 0

```

### Pregunta 4 **¿Qué Habría Que Cambiar Para Invocar Al Servicio correcto?**

1. `http://localhost:9966/petclinic/api/vets`

2. `http://localhost:9966/petclinic/api/visits`

3. `vets`

4. `visits`

**Respuesta:** 2

**Justificación:** El servicio de visitas está en `/api/visits`, no en `/api/vets`.

**Validación:** Verifica el endpoint en Swagger y prueba la URL en el navegador.

### Pregunta 5 **Resultado Esperado Tras El cambio:**

1. Muestra las cuatro visitas con datos correctos.

2. Muestra las seis visitas con datos correctos.

3. Muestra las cuatro visitas con datos nulos.

4. Da un error de ejecución.

**Respuesta:** 1

**Justificación:** El backend de Petclinic suele devolver 4 visitas iniciales en la base de datos en memoria.

**Validación:** Consulta `/api/visits` en Swagger o con el navegador y cuenta los elementos.

```text

Visita 0 -> id: 1 Description rabies shot date 1/1/2013 12:00:00 AM petId 7

Visita 1 -> id: 2 Description rabies shot date 1/2/2013 12:00:00 AM petId 8

Visita 2 -> id: 3 Description neutered date 1/3/2013 12:00:00 AM petId 8

Visita 3 -> id: 4 Description spayed date 1/4/2013 12:00:00 AM petId 7

```

---

## Pregunta 6 – Inserción Con POST

```java

using System;

  

using System.Net.Http;

  

using System.Net.Http.Headers;

  

using System.Net.Http.Json;

  

using System.Threading.Tasks;

  

namespace ConsoleApp

  

{

  

    internal class Pregunta6

  

    {

  

        static readonly HttpClient client = new HttpClient();

  

        public class Speciality

  

        {

  

            public int id {

                get;

                set;

            }

  

            public string name {

                get;

                set;

            }

  

            public override string ToString()

  

            {

  

                return "id: " + id + " name " + name;

  

            }

  

        }

  

        static async Task < Uri > CreateSpecialityAsync(Speciality speciality)

  

        {

  

            HttpResponseMessage response = await client.PostAsJsonAsync(

  

                "api/specialties", speciality);

  

            response.EnsureSuccessStatusCode();

  

            // return URI of the created resource.

  

            return response.Headers.Location;

  

        }

  

        static async Task Main()

  

        {

  

            try

  

            {

  

                client.BaseAddress = new Uri("http://localhost:9966/petclinic/");

  

                client.DefaultRequestHeaders.Accept.Clear();

  

                client.DefaultRequestHeaders.Accept.Add(

  

                    new MediaTypeWithQualityHeaderValue("application/json"));

  

                Speciality speciality = new Speciality()

  

                {

  

                    id = 100,

  

                        name = "MySpec100"

  

                };

  

                var url = await CreateSpecialityAsync(speciality);

  

                Console.WriteLine($ "Created at {url}");

  

            } catch (Exception e)

  

            {

  

                Console.WriteLine(e.Message);

  

                Console.WriteLine(e.ToString());

  

            }

  

            Console.ReadLine();

  

        }

  

    }

  

}

```

1. Crea una nueva especialidad con código 100 y mostrando un «Created at /api/specialties/100

2. Da un error de ejecución.

3. Dice que crea una nueva especialidad pero no muestra nada.

4. Nos muestra un «Created at /api/specialties/100», pero en realidad ha creado una nueva especialidad pero le ha asignado un código diferente.

**Respuesta:** 2

**Justificación:**El 500 viene del backend, no del cliente. Para esta pregunta, el flujo correcto debería devolver 201 y un Location, pero el servidor está fallando.

```text

Response status code does not indicate success: 500.

System.Net.Http.HttpRequestException: Response status code does not indicate success: 500.

   at System.Net.Http.HttpResponseMessage.EnsureSuccessStatusCode()

   at ConsoleApp.Pregunta6.CreateSpecialityAsync(Speciality speciality) in F:\13-Unir\spring-petclinic-rest\Pregunta6Demo\Program.cs:line 47

   at ConsoleApp.Pregunta6.Main() in F:\13-Unir\spring-petclinic-rest\Pregunta6Demo\Program.cs:line 81

   ```

  

---

  

## Pregunta 7 – Alta Y Consulta

  

Durante una ejecución muestra este mensaje:

  

```java

using System;

  

using System.Collections.Generic;

  

using System.Net.Http;

  

using System.Net.Http.Headers;

  

using System.Net.Http.Json;

  

using System.Text.Json;

  

using System.Threading.Tasks;

  

namespace ConsoleApp

  

{

  

    internal class Pregunta7

  

    {

  

        static readonly HttpClient client = new HttpClient();

  

        public class Speciality

  

        {

  

            public int id {

                get;

                set;

            }

  

            public string name {

                get;

                set;

            }

  

            public override string ToString()

  

            {

  

                return "id: " + id + " name " + name;

  

            }

  

        }

  

        static async Task < Speciality > CreateSpecialityAsync(Speciality speciality)

  

        {

  

            HttpResponseMessage response = await client.PostAsJsonAsync(

  

                "api/specialties", speciality);

  

            response.EnsureSuccessStatusCode();

  

            string jsonContent = response.Content.ReadAsStringAsync().Result;

  

            Speciality dev = JsonSerializer.Deserialize < Speciality > (jsonContent);

  

            return dev;

  

        }

  

        static async Task < List < Speciality >> GetSpecialitiesAsync()

  

        {

  

            HttpResponseMessage response = await client.GetAsync(

  

                "api/specialties");

  

            response.EnsureSuccessStatusCode();

  

            string jsonString = await response.Content.ReadAsStringAsync();

  

            List < Speciality > specialities = JsonSerializer.Deserialize < List < Speciality >> (jsonString);

  

            return specialities;

  

        }

  

        static async Task < Speciality > GetSpecialityAsync(int id)

  

        {

  

            HttpResponseMessage response = await client.GetAsync(

  

                "api/specialties" + "/" + id);

  

            response.EnsureSuccessStatusCode();

  

            string jsonString = await response.Content.ReadAsStringAsync();

  

            Speciality dev = JsonSerializer.Deserialize < Speciality > (jsonString);

  

            return dev;

  

        }

  

        static Speciality findByName(List < Speciality > specialityList, String name)

  

        {

  

            foreach(Speciality s in specialityList)

  

            {

  

                if (s.name.Equals(name))

  

                    return s;

  

            }

  

            return null;

  

        }

  

        static async Task Main()

  

        {

  

            try

  

            {

  

                client.BaseAddress = new Uri("http://localhost:9966/petclinic/");

  

                client.DefaultRequestHeaders.Accept.Clear();

  

                client.DefaultRequestHeaders.Accept.Add(

  

                    new MediaTypeWithQualityHeaderValue("application/json"));

  

                Speciality specialityToBeCreated = new Speciality()

  

                {

  

                    id = 123,

  

                        name = "MySpecialityDemo"

  

                };

  

                // Añadir

  

                Speciality specialityCreated = await CreateSpecialityAsync(specialityToBeCreated);

  

                Console.WriteLine("specialityCreated -> " + specialityCreated);

  

                // Buscar todos

  

                List < Speciality > specialityList = await GetSpecialitiesAsync();

  

                Console.WriteLine("specialityList size -> " + specialityList.Count);

  

                Speciality specialityFounded = findByName(specialityList, "MySpecialityDemo");

  

                Console.WriteLine("specialityFounded -> " + specialityFounded);

  

                // Buscar por id

  

                Speciality specialityFoundedIndividual = await GetSpecialityAsync(specialityFounded.id);

  

                Console.WriteLine("specialityFoundedIndividual -> " + specialityFoundedIndividual);

  

            } catch (Exception e)

  

            {

  

                Console.WriteLine(e.Message);

  

                Console.WriteLine(e.ToString());

  

            }

  

            Console.ReadLine();

  

        }

  

    }

  

}

```

![[mexingsof03_act2 3.png]]

**Indica qué es lo que hace el programa:**

1. Da de alta una especialidad con id 123 y descripción MySpecialityDemo. Busca las que hay registradas que son 25. Busca alguna que tenga esa descripción y coincide que es la 29 y la devuelve. Hay dos con el mismo nombre..

2. Da de alta una especialidad con id 123 y descripción MySpecialityDemo. Busca las que hay registradas que son 25. Busca alguna que tenga esa descripción y le ha dado el código 29 que es la que encuentra. Implica que el añadir aunque le pongamos el identificador y lo devuelva no es correcta la implementación del servidor.

3. Añade y busca una especialidad, pero esa traza no es possible.

4. Hay un error porque no se pueden tener 25 especialidades guardadas.

**Respuesta:** C

**Justificación:** El servidor ignore el ID enviado y asigna otro, por eso la especialidad creada aparece con un ID distinto (p. ej. 29).

**Validación:** Observa el ID en la respuesta de creación y compáralo con el ID solicitado.`

```text

Response status code does not indicate success: 500.

System.Net.Http.HttpRequestException: Response status code does not indicate success: 500.

   at System.Net.Http.HttpResponseMessage.EnsureSuccessStatusCode()

   at ConsoleApp.Pregunta7.CreateSpecialityAsync(Speciality speciality) in F:\13-Unir\spring-petclinic-rest\Pregunta7Demo\Program.cs:line 52

   at ConsoleApp.Pregunta7.Main() in F:\13-Unir\spring-petclinic-rest\Pregunta7Demo\Program.cs:line 144

```

---

## Pregunta 8 – Actualización Con PUT

```java

using System;

  

using System.Collections.Generic;

  

using System.Net.Http;

  

using System.Net.Http.Headers;

  

using System.Net.Http.Json;

  

using System.Text.Json;

  

using System.Threading.Tasks;

  

namespace ConsoleApp

  

{

  

    internal class Pregunta8

  

    {

  

        static readonly HttpClient client = new HttpClient();

  

        public class Speciality

  

        {

  

            public int id {

                get;

                set;

            }

  

            public string name {

                get;

                set;

            }

  

            public override string ToString()

  

            {

  

                return "id: " + id + " name " + name;

  

            }

  

        }

  

        static async Task < Speciality > CreateSpecialityAsync(Speciality speciality)

  

        {

  

            HttpResponseMessage response = await client.PostAsJsonAsync(

  

                "api/specialties", speciality);

  

            response.EnsureSuccessStatusCode();

  

            string jsonContent = response.Content.ReadAsStringAsync().Result;

  

            Speciality dev = JsonSerializer.Deserialize < Speciality > (jsonContent);

  

            return dev;

  

        }

  

        static async Task < List < Speciality >> GetSpecialitiesAsync()

  

        {

  

            HttpResponseMessage response = await client.GetAsync(

  

                "api/specialties");

  

            response.EnsureSuccessStatusCode();

  

            string jsonString = await response.Content.ReadAsStringAsync();

  

            List < Speciality > specialities = JsonSerializer.Deserialize < List < Speciality >> (jsonString);

  

            return specialities;

  

        }

  

        static async Task < Speciality > GetSpecialityAsync(int id)

  

        {

  

            HttpResponseMessage response = await client.GetAsync(

  

                "api/specialties" + "/" + id);

  

            response.EnsureSuccessStatusCode();

  

            string jsonString = await response.Content.ReadAsStringAsync();

  

            Speciality dev = JsonSerializer.Deserialize < Speciality > (jsonString);

  

            return dev;

  

        }

  

        static Speciality findByName(List < Speciality > specialityList, String name)

  

        {

  

            foreach(Speciality s in specialityList)

  

            {

  

                if (s.name.Equals(name))

  

                    return s;

  

            }

  

            return null;

  

        }

  

        static async Task < Speciality > UpdateSpecialityAsync(Speciality speciality)

  

        {

  

            HttpResponseMessage response = await client.PutAsJsonAsync(

  

                $ "api/specialties/{speciality.id}", speciality);

  

            response.EnsureSuccessStatusCode();

  

            string jsonString = await response.Content.ReadAsStringAsync();

  

            Speciality dev = JsonSerializer.Deserialize < Speciality > (jsonString);

  

            return dev;

  

        }

  

        static async Task Main()

  

        {

  

            try

  

            {

  

                client.BaseAddress = new Uri("http://localhost:9966/petclinic/");

  

                client.DefaultRequestHeaders.Accept.Clear();

  

                client.DefaultRequestHeaders.Accept.Add(

  

                    new MediaTypeWithQualityHeaderValue("application/json"));

  

                Speciality specialityToBeCreated = new Speciality()

  

                {

  

                    name = "MySpecialityDemo-Pregunta8"

  

                };

  

                // Añadir

  

                Speciality specialityCreated = await CreateSpecialityAsync(specialityToBeCreated);

  

                Console.WriteLine("specialityCreated -> " + specialityCreated);

  

                // Buscar todos

  

                List < Speciality > specialityList = await GetSpecialitiesAsync();

  

                Console.WriteLine("specialityList size -> " + specialityList.Count);

  

                Speciality specialityFounded = findByName(specialityList, "MySpecialityDemo-Pregunta8");

  

                Console.WriteLine("specialityFounded -> " + specialityFounded);

  

                // Buscar por id

  

                Speciality specialityFoundedIndividual = await GetSpecialityAsync(specialityFounded.id);

  

                Console.WriteLine("specialityFoundedIndividual -> " + specialityFoundedIndividual);

  

                // Actualizar

  

                specialityFoundedIndividual.name = "MySpecialityDemo-Changed";

  

                Speciality specialityChanged = await UpdateSpecialityAsync(specialityFoundedIndividual);

  

                Console.WriteLine("specialityChanged -> " + specialityChanged);

  

                // Buscar por id de nuevo

  

                specialityFoundedIndividual = await GetSpecialityAsync(specialityFounded.id);

  

                Console.WriteLine("specialityFoundedIndividual tras cambio -> " + specialityFoundedIndividual);

  

            } catch (Exception e)

  

            {

  

                Console.WriteLine(e.Message);

  

                Console.WriteLine(e.ToString());

  

            }

  

            Console.ReadLine();

  

        }

  

    }

  

}

```

**Indica qué es lo que hace el programa:**

1. Da de alta especialidad, la busca, la actualiza y la vuelve a buscar y en cada caso va mostrando los valores

2. Da de alta especialidad, la busca, la actualiza y la vuelve a buscar, pero al buscarla al final vemos que la ha borrado.

3. Da de alta especialidad, la busca, la actualiza y la vuelve a buscar, pero al buscarla al final vemos que la ha duplicado.

4. Hay un error en el servidor y, cuando intentamos actualizar, falla.

**Respuesta:** 4

**Justificación:** El flujo completo POST → GET → PUT → GET actualiza el recurso y muestra los valores antes y después.

**Validación:**

Response status code does not indicate success: 500.

System.Net.Http.HttpRequestException: Response status code does not indicate success: 500.

   at System.Net.Http.HttpResponseMessage.EnsureSuccessStatusCode()

   at ConsoleApp.Pregunta8.CreateSpecialityAsync(Speciality speciality) in F:\13-Unir\spring-petclinic-rest\Pregunta8Demo\Program.cs:line 52

   at ConsoleApp.Pregunta8.Main() in F:\13-Unir\spring-petclinic-rest\Pregunta8Demo\Program.cs:line 160

---

## Pregunta 9 – Borrado Con DELETE

```java

using System;

  

using System.Collections.Generic;

  

using System.Net;

  

using System.Net.Http;

  

using System.Net.Http.Headers;

  

using System.Net.Http.Json;

  

using System.Text.Json;

  

using System.Threading.Tasks;

  

namespace ConsoleApp

  

{

  

    internal class Pregunta9

  

    {

  

        static readonly HttpClient client = new HttpClient();

  

        public class Speciality

  

        {

  

            public int id {

                get;

                set;

            }

  

            public string name {

                get;

                set;

            }

  

            public override string ToString()

  

            {

  

                return "id: " + id + " name " + name;

  

            }

  

        }

  

        static async Task < Speciality > CreateSpecialityAsync(Speciality speciality)

  

        {

  

            HttpResponseMessage response = await client.PostAsJsonAsync(

  

                "api/specialties", speciality);

  

            response.EnsureSuccessStatusCode();

  

            string jsonContent = response.Content.ReadAsStringAsync().Result;

  

            Speciality dev = JsonSerializer.Deserialize < Speciality > (jsonContent);

  

            return dev;

  

        }

  

        static async Task < List < Speciality >> GetSpecialitiesAsync()

  

        {

  

            HttpResponseMessage response = await client.GetAsync(

  

                "api/specialties");

  

            response.EnsureSuccessStatusCode();

  

            string jsonString = await response.Content.ReadAsStringAsync();

  

            List < Speciality > specialities = JsonSerializer.Deserialize < List < Speciality >> (jsonString);

  

            return specialities;

  

        }

  

        static async Task < Speciality > GetSpecialityAsync(int id)

  

        {

  

            HttpResponseMessage response = await client.GetAsync(

  

                "api/specialties" + "/" + id);

  

            response.EnsureSuccessStatusCode();

  

            string jsonString = await response.Content.ReadAsStringAsync();

  

            Speciality dev = JsonSerializer.Deserialize < Speciality > (jsonString);

  

            return dev;

  

        }

  

        static Speciality findByName(List < Speciality > specialityList, String name)

  

        {

  

            foreach(Speciality s in specialityList)

  

            {

  

                if (s.name.Equals(name))

  

                    return s;

  

            }

  

            return null;

  

        }

  

        static async Task < String > UpdateSpecialityAsync(Speciality speciality)

  

        {

  

            HttpResponseMessage response = await client.PutAsJsonAsync(

  

                $ "api/specialties/{speciality.id}", speciality);

  

            response.EnsureSuccessStatusCode();

  

            string jsonString = await response.Content.ReadAsStringAsync();

  

            return jsonString;

  

        }

  

        static async Task < HttpStatusCode > DeleteSpecialityAsync(int id)

  

        {

  

            HttpResponseMessage response = await client.DeleteAsync(

  

                "api/specialties/" + id);

  

            return response.StatusCode;

  

        }

  

        static async Task Main()

  

        {

  

            try

  

            {

  

                client.BaseAddress = new Uri("http://localhost:9966/petclinic/");

  

                client.DefaultRequestHeaders.Accept.Clear();

  

                client.DefaultRequestHeaders.Accept.Add(

  

                    new MediaTypeWithQualityHeaderValue("application/json"));

  

                Speciality specialityToBeCreated = new Speciality()

  

                {

  

                    name = "MySpecialityDemo-Pregunta9"

  

                };

  

                // Añadir

  

                Speciality specialityCreated = await CreateSpecialityAsync(specialityToBeCreated);

  

                Console.WriteLine("specialityCreated -> " + specialityCreated);

  

                // Buscar todos

  

                List < Speciality > specialityList = await GetSpecialitiesAsync();

  

                Console.WriteLine("specialityList size -> " + specialityList.Count);

  

                Speciality specialityFounded = findByName(specialityList, "MySpecialityDemo-Pregunta9");

  

                Console.WriteLine("specialityFounded -> " + specialityFounded);

  

                // Buscar por id

  

                Speciality specialityFoundedIndividual = await GetSpecialityAsync(specialityFounded.id);

  

                Console.WriteLine("specialityFoundedIndividual -> " + specialityFoundedIndividual);

  

                // Actualizar

  

                specialityFoundedIndividual.name = "MySpecialityDemo-PRegunta9-Changed";

  

                String json = await UpdateSpecialityAsync(specialityFoundedIndividual);

  

                Console.WriteLine("specialityChanged -> " + json);

  

                // Buscar por id de nuevo

  

                specialityFoundedIndividual = await GetSpecialityAsync(specialityFounded.id);

  

                Console.WriteLine("specialityFoundedIndividual tras cambio -> " + specialityFoundedIndividual);

  

                // Borrar

  

                var statusCode = await DeleteSpecialityAsync(specialityFounded.id);

  

                Console.WriteLine($ "Deleted (HTTP Status = {(int)statusCode})");

  

            } catch (Exception e)

  

            {

  

                Console.WriteLine(e.Message);

  

                Console.WriteLine(e.ToString());

  

            }

  

            Console.ReadLine();

  

        }

  

    }

  

}

```

**Resultado esperado:**

1. Sigue dando una excepción al actualizar.

2. Aparentemente crea, busca, actualiza y borra, pero el borrado no se realiza bien.

3. Crea, busca, actualiza y borra una especialidad correctamente.

4. Da una nueva excepción al borrar.

**Respuesta:** 1

**Justificación:** El endpoint de borrado funciona y devuelve un estado HTTP de éxito (200/204).

**Validación:**

Response status code does not indicate success: 500.

System.Net.Http.HttpRequestException: Response status code does not indicate success: 500.

   at System.Net.Http.HttpResponseMessage.EnsureSuccessStatusCode()

   at ConsoleApp.Pregunta9.CreateSpecialityAsync(Speciality speciality) in F:\13-Unir\spring-petclinic-rest\Pregunta9Demo\Program.cs:line 54

   at ConsoleApp.Pregunta9.Main() in F:\13-Unir\spring-petclinic-rest\Pregunta9Demo\Program.cs:line 172

---

## Pregunta 10 – Autenticación Básica

Para el servicio REST de Pet-Clinic y edita el fichero application.properties que tienes en la ruta `pet-clinic\spring-petclinic-rest\src\main\resources.` Debes poner en la parte de abajo `petclinic.security.enable=true.`

Si lo prefieres, tienes un fichero `application.properties.conseguridad`que puedes renombrar a application.properties.

Vuelve a lanzar el servidor con `mvn spring-boot:run.`

Recuerda que usa una base de datos en memoria, por lo que todos los datos que tuvieras de pruebas anteriores se perderán.

Si intentas acceder al swagger te pedirá credenciales, por defecto puedes usar admin-admin para usuario y contraseña:

Credenciales por defecto:

- Usuario: `admin`

- Contraseña: `admin`

![[mexingsof03_act2 4.png]]

Intenta ejecutar este programa:

```java

using System;

  

using System.Collections.Generic;

  

using System.Net.Http;

  

using System.Net.Http.Headers;

  

using System.Text.Json;

  

using System.Threading.Tasks;

  

namespace ConsoleApp

  

{

  

    internal class Pregunta9

  

    {

  

        static readonly HttpClient client = new HttpClient();

  

        public class Speciality

  

        {

  

            public int id {

                get;

                set;

            }

  

            public string name {

                get;

                set;

            }

  

            public override string ToString()

  

            {

  

                return "id: " + id + " name " + name;

  

            }

  

        }

  

        static async Task < List < Speciality >> GetSpecialitiesAsync()

  

        {

  

            HttpResponseMessage response = await client.GetAsync(

  

                "api/specialties");

  

            Console.WriteLine("response -> " + response);

  

            response.EnsureSuccessStatusCode();

  

            string jsonString = await response.Content.ReadAsStringAsync();

  

            List < Speciality > specialities = JsonSerializer.Deserialize < List < Speciality >> (jsonString);

  

            return specialities;

  

        }

  

        static async Task Main()

  

        {

  

            try

  

            {

  

                client.BaseAddress = new Uri("http://localhost:9966/petclinic/");

  

                client.DefaultRequestHeaders.Accept.Clear();

  

                client.DefaultRequestHeaders.Accept.Add(

  

                    new MediaTypeWithQualityHeaderValue("application/json"));

  

                // Buscar todos

  

                List < Speciality > specialityList = await GetSpecialitiesAsync();

  

                if (specialityList != null)

  

                {

  

                    Console.WriteLine("specialityList size -> " + specialityList.Count);

  

                    foreach(Speciality s in specialityList)

  

                    Console.WriteLine("Speciality -> " + s);

  

                }

  

            } catch (Exception e)

  

            {

  

                Console.WriteLine(e.Message);

  

                Console.WriteLine(e.ToString());

  

            }

  

            Console.ReadLine();

  

        }

  

    }

  

}

```

Y verás que muestra un error de autenticación:

![[mexingsof03_act2 5.png]]

Si probamos desde un cliente como POSTMAN, añadiendo la autorización básica de usuario y contraseña veremos que ya funciona:

![[mexingsof03_act2 6.png]]

Modifica el programa para incluir la autenticación en la cabecera de las peticiones:

```java

static async Task Main()

  

{

  

    try

  

    {

  

        client.BaseAddress = new Uri("http://localhost:9966/petclinic/");

  

        client.DefaultRequestHeaders.Accept.Clear();

  

        client.DefaultRequestHeaders.Accept.Add(

  

            new MediaTypeWithQualityHeaderValue("application/json"));

  

        var clientId = "admin";

  

        var clientSecret = "admin";

  

        var authenticationString = $ "{clientId}:{clientSecret}";

  

        var base64EncodedAuthenticationString = Convert.ToBase64String(System.Text.ASCIIEncoding.UTF8.GetBytes(authenticationString));

  

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + base64EncodedAuthenticationString);

  

        // Buscar todos

  

        List < Speciality > specialityList = await GetSpecialitiesAsync();

  

        if (specialityList != null)

  

        {

  

            Console.WriteLine("specialityList size -> " + specialityList.Count);

  

            foreach(Speciality s in specialityList)

  

            Console.WriteLine("Speciality -> " + s);

  

        }

  

    } catch (Exception e)

  

    {

  

        Console.WriteLine(e.Message);

  

        Console.WriteLine(e.ToString());

  

    }

  

    Console.ReadLine();

  

}

  

}

```

**Resultado esperado:**

1. Sigue dando un error de autenticación.

2. Funciona correctamente y devuelve e imprime las tres especialidades nuevas.

3. Da un error de ejecución que no tiene nada que ver con autenticación.

4. Funciona correctamente aunque no imprime nada.

**Respuesta:** 2

**Justificación:** Con Basic Auth correcta, el servidor acepta la petición y devuelve la lista.

**Validación:** Ejecuta con seguridad activa y confirma que no aparece 401 y que se imprime el listado.