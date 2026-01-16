Actividad 2: Análisis estático de código de una aplicación

Recuerda que esta actividad deberá set completada en la plataforma. Solo tendrás un intento. Una vez que la envíes, se dará por cerrada. Tu puntuación y las respuestas correctas se mostrarán cuando finalice el periodo de entrega de la tarea.

**Objetivos**

- Analizar el código fuente de una aplicación para poder determinar el nivel de riesgo de las vulnerabilidades encontradas.
    
- Conocer el tipo de defectos de seguridad que se pueden cometer en lenguajes como C y Java.
    
- Prepararse para poder analizar el código en base al conocimiento de los defectos de programación que se pueden cometer.

**Descripción de la actividad y pautas de elaboración**

Esta actividad profundiza en el estudio de la práctica de seguridad del software más importante que implantar en un ciclo de vida de desarrollo seguro de un software (S‑SDLC): revisión estática de código.

**Planteamiento de preguntas**

---

# 1. Dado El Siguiente Código, ¿qué Vulnerabilidad Contiene?

```c
#define BUFSIZE 256

int main(int argc, char **argv) {

char *buf;

buf = (char *)malloc(sizeof(char)*BUFSIZE);

strcpy(buf, argv[1]);

}
```

1. Stack overflow.
    
> 1. **Heap overflow.**
> Un **heap overflow** ocurre cuando un programa escribe **más datos de los permitidos** en una región de memoria asignada dinámicamente (el _heap_), sobrescribiendo memoria adyacente.
    
1. Format string.
    
2. No existe vulnerabilidad.

---

# 2. Dado El Siguiente Código, ¿qué Vulnerabilidad Contiene?

```c
#include <stdio.h>

void printWrapper(char *string) {

printf(string);

}

int main(int argc, char **argv) {

char buf[5012];

memcpy(buf, argv[1], 5012);

printWrapper(argv[1]);

return (0);

}
```

1. Stack overflow.
    
2. Heap overflow.
    
> 1. **Format string.**
> El programa contiene una vulnerabilidad de _format string_ porque la función `printf` usa directamente una cadena controlada por el usuario como formato. Esto permite que un atacante utilice especificadores como `%x` o `%n` para leer o modificar memoria del programa.
    
1. No existe vulnerabilidad.

---

# 3. Dado El Siguiente Código, ¿qué Vulnerabilidad Contiene?

```c
char* ptr = (char*)malloc (SIZE);

if (err) {

abrt = 1;

free(ptr);

}

...

if (abrt) {

logError("operation aborted before commit", ptr);

}
```

> 1. **Use after free.**
> El código contiene una vulnerabilidad de _use after free_ porque el puntero `ptr` es utilizado después de que la memoria a la que apunta ha sido liberada con `free`, lo que puede causar comportamientos inesperados o fallos de seguridad.
    
1. Heap overflow.
    
2. Format string.
    
3. No existe vulnerabilidad.

---

# 4. Dado El Siguiente Código, ¿qué Vulnerabilidad Contiene?

```c
bar connection(){

foo = malloc(1024);

return foo;

}

endConnection(bar foo) {

free(foo);

}

int main() {

while(1) //thread 1

//On a connection

foo=connection(); //thread 2

//When the connection ends

endConnection(foo)

}
```

> 1. **Use after free.**
> El código contiene una vulnerabilidad de _use after free_ debido a la falta de sincronización entre hilos. La memoria asignada puede set liberada en un hilo mientras otro hilo aún la está utilizando, lo que provoca comportamientos indefinidos y riesgos de seguridad.
    
1. Heap overflow.
    
2. Format string.
    
3. Memory leak.

---

# 5. Dado El Siguiente Código, ¿qué Vulnerabilidad Contiene?

```c
srand(time());

int randNum = rand();
```

1. Use after free.
    
2. Heap overflow.
    
3. Format string.
    
> **4. Uso de un generador de números pseudoaleatorios (PRNG) criptográficamente débil.**
> El código utilize la función `rand()` inicializada con `time()` como semilla, lo que genera números pseudoaleatorios predecibles. Este generador no es criptográficamente seguro y no debe usarse en contextos de seguridad.

---

# 6. Dado El Siguiente Código, ¿qué Vulnerabilidad Contiene?

```java
private void buildList ( int untrustedListSize ){

if ( 0 > untrustedListSize ){

die("Negative value supplied for list size, die evil hacker!");

}

Widget[] list = new Widget [ untrustedListSize ];

list[0] = new Widget();

}
```

> 1. **Validación incorrecta del índice del array.**
> El código presenta una validación incorrecta del índice del array, ya que solo verifica que el tamaño no sea negativo, pero permite el valor cero, lo que provoca un acceso fuera de los límites del array al intentar acceder al índice 0.
    
1. _Uso de claves criptográficas codificadas._
    
2. _Format string._
    
3. _Uso de un generador de números pseudoaleatorios (PRNG) criptográficamente débil__._**

---

# 7. Dado El Siguiente Código, ¿qué Vulnerabilidad Contiene?

```c
struct hostent *clienthp;

char hostname[MAX_LEN];

// create server socket, bind to server address and listen on socket

...

// accept client connections and process requests

int count = 0;

for (count = 0; count < MAX_CONNECTIONS; count++) {

int clientlen = sizeof(struct sockaddr_in);

int clientsocket = accept(serversocket, (struct sockaddr *)&clientaddr, &clientlen);

if (clientsocket >= 0) {

clienthp = gethostbyaddr((char*) &clientaddr.sin_addr.s_addr, sizeof(clientaddr.sin_addr.s_addr), AF_INET);

strcpy(hostname, clienthp->h_name);

logOutput("Accepted client connection from host ", hostname);

// process client request

...

close(clientsocket);

}

}

close(serversocket);
```

1. Use after free.
    
2. Integer overflow.
    
3. Format string.
    
> **4**. **Buffer Overflow.**
> El código contiene una vulnerabilidad de _buffer overflow_ porque utilize `strcpy` para copiar un nombre de host de longitud no controlada dentro de un buffer de tamaño fijo, lo que puede provocar escritura fuera de los límites de memoria.

---

# 8. Dado El Siguiente Código, ¿qué Vulnerabilidad Contiene?

```c
int a = 5, b = 6;

size_t len = a - b;

char buf[len]; // Just blows up the stack

}
```

1. Use after free.
    
> **2**. **Integer overflow.**
> El código contiene una vulnerabilidad de _integer overflow_ debido a la resta de dos enteros que produce un valor negativo que luego es convertido a `size_t`, provocando un valor extremadamente grande y un fallo al intentar reservar memoria en el stack.
    
1. Format string.
    
2. Buffer Overflow**.**

---

# 9. Dado El Siguiente Código, ¿qué Vulnerabilidad Contiene?

```c
void host_lookup(char *user_supplied_addr){

struct hostent *hp;

in_addr_t *addr;

char hostname[64];

in_addr_t inet_addr(const char *cp);

/*routine that ensures user_supplied_addr is in the right format for conversion */

validate_addr_form(user_supplied_addr);

addr = inet_addr(user_supplied_addr);

hp = gethostbyaddr( addr, sizeof(struct in_addr), AF_INET);

strcpy(hostname, hp->h_name);

}
```

1. Use after free.
    
2. Integer overflow.
    
3. Format string.
    
> **4**. **NULL Pointer Dereference.**
> El código presenta una vulnerabilidad de _NULL pointer dereference_ porque no se valida el valor de retorno de `gethostbyaddr`. Si la función falla y devuelve NULL, el acceso a `hp->h_name` provoca una caída del programa.

---

# 10. Dado El Siguiente Código, ¿qué Vulnerabilidad Contiene?

```perl
my $dataPath = "/users/cwe/profiles";

my $username = param("user");

my $profilePath = $dataPath . "/" . $username;

open(my $fh, "<", $profilePath) || ExitError("profile read error: $profilePath");

print "<ul>\n";

while (<$fh>) {

print "<li>$_</li>\n";

}

print "</ul>\n";
```

1. Use after free.
    
> **2**. **Manipulación de rutas.**
> El código contiene una vulnerabilidad de manipulación de rutas porque concatena directamente una entrada controlada por el usuario para construir una ruta de archivo, permitiendo el acceso a archivos fuera del directorio previsto.
    
1. Format string.
    
2. Buffer Overflow**.**