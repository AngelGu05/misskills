---
name: escuela-ciencias
description: Convierte un tema de ciencias de la escuela (biología, química, física) en material de estudio completo, en español. Analiza un video de YouTube solo con lo que dice, lo completa con el PPT de clase y fotos de apuntes, corrige los errores de los apuntes y construye una app web de estudio con una animación interactiva del proceso, una vista de lectura completa, un examen configurable con el formato de la profesora y práctica por temas. Después la publica en claude.ai, GitHub y Vercel. Úsala siempre que el usuario quiera entender o estudiar un tema de ciencias a partir de un video, un PPT, apuntes o exámenes viejos; cuando pida "explícame este video", "complétame los apuntes", "hazme una app o página para estudiar", "hazme un examen como el de mi profesora" o "quiero ver el proceso animado"; o cuando mencione una prueba, un bimestral o un tema de clase como transcripción, mitosis, fotosíntesis, respiración celular, membrana o enlaces químicos, aunque no diga "skill de escuela ciencias".
---

# Skill de escuela: ciencias

Convierte el material de clase de un estudiante (video, PPT, apuntes, exámenes viejos) en:

1. una **explicación detallada y fiel** a las fuentes;
2. **apuntes completos y corregidos**;
3. una **app de estudio** (animación interactiva, lectura completa, examen tipo profesora y práctica);
4. una **publicación** en claude.ai, GitHub y Vercel.

El usuario es un estudiante de secundaria que escribe en español informal. Respóndele en español claro, sin jerga técnica. Si aparece un término como "commit" o "deploy", explícalo en una frase.

## Principios (por qué importan)

- **Fidelidad a las fuentes (en el chat).** El estudiante necesita saber qué viene de su clase, porque eso es lo que le van a preguntar. Mientras no lo autorice, usa solo lo que dicen sus materiales. En tus respuestas del chat (explicación del video, apuntes completos, correcciones), etiqueta el origen de cada dato: 🎥 Video · 📊 PPT · ✍️ Apuntes · 📝 Examen · 🔶 Externo.
- **La app es pública y profesional.** La página la ven otras personas, no solo el estudiante. En la app **no** pongas referencias personales ni de origen: nada de "en tus apuntes…", "según el PPT", "en el minuto 3:44 del video", "el video no se escucha", "en un examen anterior se marcó…", "tu profesora", "dato externo" ni etiquetas de fuente (Video, PPT, Apuntes, Examen, Externo). Escribe el contenido como un texto de estudio neutral: "El ARN se forma de 5′ a 3′", "En resumen, paso 3 de 5", "En algunos libros también se le llama…". Los consejos de examen sí van, pero en general ("en un examen, escribe ambas direcciones"), sin anécdotas. Los nombres que usa la clase se ponen directamente como nombre oficial, sin decir de dónde salen.
- **No omitir nada.** El usuario lo pidió de forma explícita: todo lo que dicen sus materiales debe aparecer en algún lado (cifras, nombres, ejemplos, pasos del PPT, notas al margen). Antes de dar algo por terminado, revisa fuente por fuente que nada se quedó fuera.
- **Cada componente explica "qué es" y "qué hace".** Una definición sin función no le sirvió al usuario y lo dijo. Agrega también "qué hace en esta parte" cuando el componente actúa distinto según la etapa.
- **No inventar para tapar huecos.** Si a la transcripción le falta un tramo, dilo, con los minutos. Pide que el usuario lo escuche, o completa con información externa marcada. Si una herramienta no puede acceder a algo (YouTube, Vercel), dilo y da los pasos para que lo haga el usuario.
- **Antes de corregir un apunte, revisa todas las fuentes.** Si el PPT dice lo mismo que el apunte, el apunte está bien según su clase aunque un libro lo matice. En ese caso explica el matiz, no lo marques como error.
- **Corregir con tacto.** Los apuntes suelen tener errores (por ejemplo, "el ARN se forma de 3′ a 5′" o "factores de conversión" en lugar de "factores de transcripción basales"). Señálalos en una tabla: lo que dice → lo correcto → fuente.
- **Verificar lo que se construye.** Revisa que los puntajes del examen sumen el total anunciado (ya hubo un error así: decía 115 y sumaba 100). Prueba la app en el navegador antes de entregarla.

## Flujo de trabajo

No preguntes lo que ya puedes deducir. Haz preguntas concretas solo en las decisiones que de verdad le tocan al usuario, y si no contesta, sigue con valores razonables y dile cuáles usaste.

### Fase 1: Analizar el video

1. Pide el enlace. Intenta sacar los subtítulos con `scripts/youtube_transcript.sh <url>` (usa yt-dlp).
2. Si YouTube está bloqueado por la red del entorno, dilo y ofrece dos opciones: (a) que el usuario pegue el texto de **"Mostrar transcripción"** de YouTube, o (b) que permita `www.youtube.com` en la configuración de red del entorno.
3. Con la transcripción:
   - Busca **huecos**: saltos entre marcas de tiempo de más de unos 8 s que cortan una frase. Repórtalos con minutos exactos y con lo que probablemente falta. Si el usuario vuelve a pegar el mismo texto, explícale que hay que **escuchar** ese tramo en el video, porque la transcripción no lo tiene.
   - Corrige los errores del subtitulado automático ("tat boox" → caja TATA, "esposoma" → espliceosoma) y lístalos al final.
4. Entrega una explicación **por secciones con marcas de tiempo**, solo con lo que dice el video, y termina con un resumen del recorrido completo.
5. Si el usuario pide completar los huecos, hazlo con un bloque marcado 🔶 Externo.

Detalles en `references/fuentes.md`.

### Fase 2: Completar con PPT y apuntes

1. Extrae el PPT con `python3 scripts/extract_pptx.py archivo.pptx salida/`. Saca el texto, las **tablas**, las notas y las imágenes de cada diapositiva. No te quedes solo con los cuadros de texto: una tabla que no se leyó llevó a "corregir" un apunte que estaba bien. **Mira las imágenes**: a menudo traen información clave, como tipos de ARN o un diagrama de bacterias. Descomprime los ZIP de fotos en una carpeta propia y lee cada foto.
2. Entrega primero una tabla **"Correcciones a tus apuntes"**. Después, los **apuntes completos** organizados por tema, con etiquetas de origen por línea o por bloque.
3. Avisa de **mezclas de contexto**. Por ejemplo, un diagrama del PPT que es de procariotas (factor σ, terminador) mientras el video explica eucariotas.
4. Si en los apuntes hay términos que no aparecen en ninguna fuente, dilo y sugiere confirmarlos con la profesora.

### Fase 3: Construir la app de estudio

Antes de construir, propone la estructura y pregunta lo esencial: qué contenido entra, cómo quiere el examen, cómo se corrigen las preguntas abiertas y en qué dispositivo la usará. Si el usuario manda **exámenes viejos**, úsalos como **referencia de formato** (tipos de parte, puntajes, estilo de preguntas). Si son del mismo tema, úsalos también como **fuente de contenido** (preguntas, datos nuevos, y qué se marcó mal). Comenta en el chat lo que se marcó mal; en la app conviértelo en un consejo general, sin contar la anécdota. Fíjate de quién es el examen: si tiene el nombre de otra persona, no le digas al usuario "contestaste" o "te marcaron", y nunca pongas nombres de personas en la app. En la app, nombra los formatos "Examen 1", "Examen 2"…, nunca "como la profesora", "bimestral" ni "parcial del año pasado". Analiza también en qué falló el estudiante (por ejemplo, preguntas de aplicar vs. de memoria) para reforzar eso.

Parte de la app de ejemplo `assets/ejemplo-transcripcion.html`. Su motor es reutilizable y solo cambian los datos del tema. Lee `references/app-arquitectura.md` para saber qué reemplazar y qué conservar. La app tiene estas secciones:

| Pestaña | Qué tiene |
|---|---|
| **Proceso** | Animación **continua** del proceso dividida en partes, como si se viera en persona: play/pausa, línea de tiempo, saltar entre partes, "pausar al final de cada parte", velocidad, subtítulos que narran y atajos de teclado. Cada estructura es **clicable** y muestra qué es, qué hace y qué hace en esta parte. Incluye el modo **"Ponme a prueba"** (señalar estructuras sin etiquetas). |
| **Leer todo** | Toda la información en una página: resumen de una línea por parte, cada parte con una imagen fija, explicación y componentes desplegados, glosario A–Z, buscador, índice fijo, botón "Ver esta parte en la animación" e impresión a PDF (solo fuera de claude.ai). |
| **Lo general** | Tarjetas con lo transversal: definición, tipos, características, comparaciones (por ejemplo eucariota vs. procariota) y "errores comunes y aclaraciones". |
| **Examen** | **Configurable**: Examen 1, Examen 2… (uno por cada formato real que mande el usuario), solo selección única, solo completar, solo pareo, combinar algunos o combinar todos; largo corto, normal o largo. El total se calcula según lo elegido. Correcciones con explicación y enlace a la parte de la animación. |
| **Práctica** | 8 preguntas por tema con respuesta al momento y "Repasar mis errores" (guardado en el navegador). |

Diseño que el usuario pidió y aprobó:

- **Fondo negro** con texto claro. Que no haya letras oscuras sobre fondo oscuro.
- **Fondo animado** temático en canvas (en el ejemplo: hélices de ADN en 3D, letras de nucleótidos flotando y luces suaves). Las tarjetas son translúcidas para que el fondo se vea. Respeta `prefers-reduced-motion`.
- La animación debe verse **natural**: objetos que llegan, se mueven, se doblan y se separan con suavidad. Nada de diapositivas que cambian de golpe.

Banco de preguntas: apunta a ≥60 de selección única, ≥40 de completar, ≥45 pares para pareo (los términos pueden repetirse), ≥6 casos de desarrollo y ≥2 análisis de imágenes. Mezcla preguntas de memoria con **casos de aplicación** ("si una mutación impide X, ¿qué pasa?"). Formato de las partes: `references/examen-formato.md`.

Antes de entregar:
- Revisa la sintaxis del script con `node --check`.
- Toma capturas con Playwright en varios momentos de la animación, en el examen, en "Leer todo" y en un celular (390 px) sin scroll horizontal.
- Prueba que cada formato de examen se genere y que su total sea correcto, y que **al elegir un formato la hoja cambie al instante**.
- Revisa el texto visible de todas las pestañas (y de `DEF`, `STEPS`, `CAPS`, las preguntas y `SUM`) en busca de referencias personales o de origen ("tus apuntes", "PPT", "video", minutos como "3:44", "examen anterior", "profesora", "externo"). Debe dar cero.

### Fase 4: Publicar

1. **claude.ai (Artifact):** publica la página con `capabilities: {sample: {}}` para que las preguntas abiertas se corrijan con IA. Sin esa capacidad, la app cae en autoevaluación con respuesta modelo.
2. **GitHub:** arma un `index.html` completo con `python3 scripts/build_index.py pagina.html repo/index.html` y agrega un README. Si no puedes crear el repositorio, pide al usuario que lo cree vacío en github.com/new y adjúntalo con `add_repo`. Fíjate bien en el nombre real: el usuario puede usar otro, por ejemplo `transcripcion-de-ADN`.
3. **Vercel:** normalmente este entorno no tiene acceso a Vercel, así que da los pasos al usuario: vercel.com/new → Import del repositorio → Deploy. Desde ahí, cada push publica solo. Compruébalo con `gh api repos/<owner>/<repo>/commits/<sha>/status`. Si aparecen dos proyectos, es que importó dos veces: explícale cómo borrar el sobrante.
4. Explica las diferencias: en Vercel no hay corrección con IA y en claude.ai no se puede imprimir.

## Formato de las respuestas en el chat

- Usa encabezados y tablas para la información de estudio y párrafos cortos para el resto.
- Al terminar un cambio a la app, resume qué cambió, dónde verlo y qué no pudiste verificar.
- Los enlaces de PR o de repositorio deben ser URLs completas.
