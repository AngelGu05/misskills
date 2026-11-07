# Cómo trabajar con las fuentes del estudiante

## Video de YouTube
1. `scripts/youtube_transcript.sh "<url>" <carpeta>` descarga los subtítulos (manuales o automáticos, en español o inglés) y los deja como texto con marcas de tiempo.
2. Si sale `403`/`Tunnel connection failed` o `ENOTFOUND www.youtube.com`, la red del entorno bloquea YouTube. No insistas. Ofrece:
   - que el usuario abra el video → descripción → **"Mostrar transcripción"** → copie y pegue todo el panel; o
   - permitir `www.youtube.com` (y `*.googlevideo.com` si hace falta el audio) en la configuración de red del entorno.
3. **Huecos**: revisa la diferencia entre marcas de tiempo consecutivas. Un salto de más de unos 8 s con una frase cortada ("en lo que sería la región" → 13 s → "intergénico…") es contenido que falta. Repórtalo así:
   > Falta de **3:44 a 3:57**: el texto salta de "…" a "…". Ahí probablemente se explica X.
   Si el usuario vuelve a pegar el mismo tramo, explícale que la transcripción de YouTube tampoco lo tiene y que hay que **escucharlo** en el video (o mandar una captura de la animación).
4. Errores típicos del subtitulado automático en ciencias: nombres propios de moléculas mal escritos ("tat boox", "tvp", "si metil guanosina", "esposoma", "sping", "polia"). Corrígelos en la explicación y lístalos al final.

## Explicación "sin información externa"
- Organízala por secciones con marcas de tiempo (`## 3. Título (2:24 – 4:15)`), con viñetas que lleven cifras y nombres exactos.
- Marca cada hueco con ⚠️ en su lugar.
- Cierra con un "resumen del recorrido completo" numerado.
- Ofrece complementar con información externa marcada 🔶.

## PPT
`python3 scripts/extract_pptx.py clase.pptx salida/` imprime el texto y las notas de cada diapositiva y guarda las imágenes en `salida/` con el número de diapositiva. **Lee también las tablas** (el script las imprime con `|`): en un PPT real la tabla de "Tipos de ARN" traía datos (proporciones, tamaño, peso molecular) que no salían leyendo solo los cuadros de texto, y por no verla se "corrigió" por error un apunte que estaba bien. **Mira cada imagen**: los diagramas pueden ser de otro contexto (por ejemplo, un esquema de bacterias en una clase de eucariotas) y traen datos que no están en el texto (tipos de ARN, anticodón).

## Fotos de apuntes (ZIP de WhatsApp, imágenes)
- Descomprime en una carpeta nueva y propia. Lee cada foto.
- Transcribe la letra a mano con cuidado. Si una palabra no se entiende, dilo en lugar de adivinar.
- Busca: errores conceptuales, términos inventados o mal copiados, signos de pregunta del propio estudiante ("Sitio: ?") y notas al margen.

## Entregable de la Fase 2
1. **Tabla de correcciones**: lo que dicen tus apuntes | corrección | fuente.
2. **Avisos de contexto**: diagramas de otro organismo, términos que no aparecen en ninguna fuente.
3. **Apuntes completos** por tema, con etiquetas 🎥 📊 ✍️ 🔶.
4. Una línea final con lo que no se revisó (por ejemplo, enlaces del PPT que el entorno no puede abrir).
