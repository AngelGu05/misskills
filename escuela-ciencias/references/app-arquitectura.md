# Arquitectura de la app de estudio

La app de ejemplo es `assets/ejemplo-transcripcion.html` (transcripción del ADN). Es **un solo archivo HTML** con CSS y JS en línea, sin librerías. Funciona igual como Artifact de claude.ai y como sitio estático en Vercel.

Para un tema nuevo, **copia el archivo y reemplaza solo los datos del tema**. El motor ya está probado: reproductor, panel, examen, práctica, lectura y rutas.

## Índice
1. Mapa del archivo
2. Qué reemplazar (datos del tema)
3. Cómo escribir la animación (`renderAt`)
4. Qué conservar (motor)
5. Reglas que evitan errores conocidos
6. Checklist de pruebas

## 1. Mapa del archivo

Busca estos comentarios en el archivo para ubicarte:

| Marcador | Contenido | ¿Cambia por tema? |
|---|---|---|
| `<style>` `:root{...}` | Tokens de color (tema oscuro único), fuentes | Ajusta los colores del dominio (`--dna`, `--rna`…) |
| `<!-- PROCESO -->` | Escenario SVG, barra de subtítulos, reproductor, panel | No |
| `<!-- LEER TODO -->` | Contenedor vacío; lo llena `renderLeer()` | No |
| `<!-- LO GENERAL -->` | Tarjetas HTML escritas a mano | **Sí**: todo el contenido |
| `<!-- EXAMEN -->`, `<!-- PRÁCTICA -->` | Contenedores | No |
| `/* definiciones: qué es + qué hace */` | `DEF` | **Sí** |
| `/* partes de la animación */` | `CH`, `TOTAL`, `QT`, `CHN`, `STEPS`, `CAPS` | **Sí** |
| `/* geometría ... */` y `/* escena en el tiempo T */` | Funciones de posición y `renderAt(T,o)` | **Sí**: el dibujo del tema |
| `/* reproductor */`, `/* panel */` | Play/pausa, línea de tiempo, partes, selección, modo "Ponme a prueba" | No |
| `/* banco de preguntas */` | `MC`, `FILL`, `CASOS`, `SCEN`, `AB_*`, `PAREO`, `ABS` | **Sí** |
| `/* EXAMEN */` | Motor configurable (presets, pareo, IA/autoevaluación) | No (solo el título "Prueba de Biología · …") |
| `/* PRÁCTICA */` | Rondas por tema, repaso de errores | `TOPICS` según las partes del tema |
| `/* fondo animado */` | Canvas con motivos | **Sí**: motivo del tema (moléculas, células, átomos…) |
| `/* LEER TODO */` | `SUM` (una línea por parte) y el render | **Sí**: `SUM` |
| `/* rutas */` | Pestañas por `#hash` | No |

## 2. Qué reemplazar

### `DEF`: un objeto por estructura clicable
```js
id:{n:'Nombre visible', c:'--token-color', src:'vpax',          // fuentes internas (v=video p=PPT a=apuntes e=examen x=externo); en la página pública pills() devuelve '' y no se muestran
    w:'Qué es (1–2 frases)',
    h:'Qué hace (función; nunca vacío)',
    r:{3:'Qué hace en la parte 3', 8:'…'},                   // opcional, por parte
    warn:'Error común o aviso (opcional)',
    names:['claves','aceptadas'], not:['frases que invalidan'], // para corregir el "nombre" en la III Parte
    fn:'Respuesta modelo corta de su función (para la tabla del examen)'}
```

### Partes y tiempos
- `CH=[[inicio,fin],...]` en segundos, una entrada por parte; `TOTAL` = fin de la última.
- `QT[i]`: un instante de la parte `i` en el que **se ven todos** sus participantes. Lo usan "Ponme a prueba", "Leer todo" y el examen.
- `CHN`: nombres cortos para los botones.
- `STEPS[i]={t,s,src,who:[ids],h:'<p>HTML</p>'}`: `h` contiene la explicación completa, el resumen por pasos en `<p class="ppt">En resumen, paso N de 5: …</p>` y los errores comunes en `<p class="note">`. Todo en tono neutral: sin "según el PPT", "tus apuntes" ni minutos del video.
- `CAPS=[[t,'subtítulo'],...]`: la narración que cambia durante la animación.
- `SUM`: un resumen de una línea por parte, para "Leer todo".

### Banco de preguntas
- `MC`: `{id,tp,st,q,o:[4],a,ex}`. `tp` es el tema de práctica y `st` la parte de la animación a la que enlaza (o `null`).
- `FILL`: `{id,tp,st,q,parts:[{p:'a. subpregunta',k:['claves'],not:[...],show:'respuesta'}],ex}`. En las claves, `'=x'` exige coincidencia exacta; las demás aceptan la respuesta si contiene la clave (sin tildes ni mayúsculas).
- `PAREO`: `[['Término','Descripción corta'],...]`. Las descripciones no deben servir para dos términos a la vez.
- `CASOS`: `{q,m}`, un caso de la vida real y su respuesta modelo.
- `SCEN`: `{t, ids:[5 ids]}`, el momento de la animación que se numera en el examen. Cada id debe tener una llamada `L()` visible en ese `t`.
- `ABS`: `{q,m,svg:()=>html}`, una comparación de dos imágenes (puede usar `renderAt` en dos tiempos).

## 3. Cómo escribir la animación

`renderAt(T,{labels,nums,interactive})` devuelve **una cadena SVG** (viewBox 1000×500) para el instante `T`. El reproductor la vuelve a generar en cada cuadro. Generarla toma unos 0,3 ms, así que no hace falta mantener el DOM entre cuadros.

Ayudantes dentro de `renderAt`:
- `H(id, svg)` envuelve una forma como **clicable**: `.hit`, `data-id`, foco con teclado.
- `L(id,x,y,texto,anchor,lx,ly,cls,op)` dibuja una **etiqueta** con línea guía. En modo examen (`nums`) dibuja el **número** en su lugar.
- `A(...)` es una anotación que no se puede tocar. `inset(...)` es un recuadro explicativo.
- `prog(T,a,b)` es una interpolación suavizada entre los tiempos a y b; `lin` es lineal; `pw(T,[[t,v],...])` es por tramos.

Patrones para que se vea **natural**:
- Las proteínas **llegan volando** desde fuera con `prog`, y después oscilan un poco con `Math.sin(T*2)*0.8`.
- Las formas cambian por **interpolación de puntos** (polilíneas con la misma cantidad de puntos), por ejemplo el ADN que se dobla. No cambies de dibujo de golpe.
- Las partículas (sustratos) entran en ciclo hacia la enzima, con fases distintas.
- Las etiquetas **siguen** a su objeto y aparecen o desaparecen con opacidad.
- Al cambiar de escena (por ejemplo, del núcleo al citoplasma) haz un **fundido cruzado** de 1–2 s.

## 4. Qué conservar sin tocar
- Las selecciones usan `pointerdown`, no `click`, porque el SVG se regenera en cada cuadro y un `click` podría perderse. Al seleccionar se pausa la animación.
- "Pausar al final de cada parte" (`byParts`) está activado por defecto.
- El examen recalcula el total con las partes elegidas. Las preguntas abiertas se corrigen con `claude.use('sample')` si existe; si no, se autoevalúan con la respuesta modelo.
- `localStorage` siempre va dentro de try/catch. Cambia el prefijo de las claves (`tx-missed`, `tx-excfg`) por uno del tema.
- El botón de imprimir en "Leer todo" solo aparece fuera de claude.ai, porque ahí `window.print` no funciona.

## 5. Reglas que evitan errores conocidos
- **Los totales deben sumar.** Si un preset imita el examen de la profesora, el total anunciado tiene que coincidir con la suma de sus partes.
- Las celdas y tarjetas con SVG anchos dentro de un grid necesitan `min-width:0` en el padre, o se rompe el ancho en el celular.
- Una clase de botón no puede llamarse igual que una de las pastillas de fuente (`.x` era "Externo" y desarmó el botón de cerrar).
- En la búsqueda de "Leer todo", los enlaces internos usan `data-jump` con `preventDefault`. Si cambian el `#hash`, el router los confunde con una pestaña.

## 6. Checklist de pruebas
1. `node --check` del último `<script>` (extráelo con una regex).
2. Playwright: capturas en `T` = cada `QT[i]` y una cuadrícula para revisarlas juntas, sin etiquetas encimadas ni elementos fuera del cuadro.
3. Clic en una estructura → la tarjeta muestra "Qué es / Qué hace / En esta parte".
4. Play durante 1,5 s → `T` avanza; al final de la parte se pausa sola.
5. Cada preset del examen: el total impreso coincide con `EX.total`. Un pareo contestado bien da el puntaje máximo.
6. "Leer todo": buscar una palabra → hay coincidencias y se ocultan las partes que no la tienen. "Ver esta parte" → pestaña Proceso con la animación en esa parte.
7. Celular a 390 px: `document.documentElement.scrollWidth === 390` en todas las pestañas.
