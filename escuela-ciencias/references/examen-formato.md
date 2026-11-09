# Formatos de examen (referencia)

Sacados de exámenes reales de Biología que mandó el usuario. Úsalos como **formato**. El contenido sale del tema que se está estudiando, más lo que esos exámenes revelen sobre el tema (ver "Contenido" abajo).

**Nombres en la app:** "Examen 1", "Examen 2", "Examen 3"… Nunca uses "como la profesora", "bimestral", "parcial del año pasado" ni nombres de personas o del colegio: el usuario lo pidió así.

## Examen 1 (100 pts en la app; el original valía 115)

| Parte | Tipo | Puntos | Cómo se ve |
|---|---|---|---|
| I | **Selección única** | 25 (2,5 c/u) | Una tabla con una casilla a la izquierda para la **letra en mayúscula** y el enunciado con opciones a–d. Mezcla memoria con **casos** y preguntas "¿cuál es FALSA?". |
| II | **Completar espacios** | 40 | Una tabla de dos columnas. Muchas preguntas tienen subpartes **a., b., c.** ("En relación a X, diga: a… b… c…"). |
| III | **Análisis de imágenes** | 30 | (a) Un diagrama con **estructuras numeradas** y una tabla de nombre y función. (b) **Dos imágenes A y B**: "Explique la consecuencia…". |
| IV | **Desarrollo** | 5 | Un **caso de la vida real**: "Explica científicamente por qué…". |

El original también tenía "Desarrolle y complete el cuadro" (10 pts): una tabla con imágenes donde se pone el nombre (1 pt) y la explicación (2 pts).

## Examen 2 (80 pts)

| Parte | Tipo | Puntos | Cómo se ve |
|---|---|---|---|
| I | **Completar espacios** | 30 | Igual que arriba. Algunas preguntas valen 2 pts ("Explique la importancia…", "c. importancia (2 puntos)"). |
| II | **Pareo** | 25 (1 c/u en el original) | Arriba, un cuadro con **opciones con código de dos letras** ("PT. finalización", "IR. TATA", "JD. ARN polimerasa"…). Abajo, una tabla con una casilla para el código y el enunciado. **"Las opciones pueden repetirse o no utilizarse."** |
| III | **Desarrollo** | 5 | "Explique… ¿Cómo logra…?" |
| IV | **Análisis de imágenes** | 20 | Un dibujo con **dos procesos** a partir del ADN (1 = replicación, 2 = transcripción): nombre de cada proceso, nombre de las partes señaladas a–d, enzimas y su trabajo, y **"Explique los pasos del proceso 2"**, donde se esperan los 5 pasos del PPT. |

## Contenido que revelan los exámenes
- Los exámenes pueden **mezclar temas** (replicación + transcripción). Incluye solo el tema que se estudia, salvo que el usuario pida otro, pero usa los enunciados que tocan el tema como fuente nueva: márcalos con la etiqueta **"Examen"**.
- Aparecen datos que no estaban en el video ni en el PPT (p53, Rb, receptor de estrógeno, unidad Svedberg). Agrégalos con la etiqueta "Examen" y di de dónde podrían venir (por ejemplo, la lectura recomendada en el PPT).
- **Fíjate en lo que la profesora marcó como incorrecto.** En un examen, "5′ a 3′" para "dirección en que se forma la cadena de ARN" se marcó incorrecto, aunque es lo científicamente correcto. No cambies la ciencia: avísale al estudiante y sugiérele escribir ambas direcciones (molde 3′→5′, ARN 5′→3′) o preguntar. "Marca la región de inicio" como importancia de la TATA también se marcó mal: espera **quién se une y para qué**.
- El estudiante pierde más puntos en preguntas de **aplicar o razonar** y en las de "importancia". Incluye muchas de esas.

## Formatos que ofrece la app
Examen 1 · Examen 2 · Solo selección única · Solo completar · Solo pareo · Combinar algunos (el usuario marca las partes) · Combinar todos. Largo: corto, normal o largo (no aplica a Examen 1 y 2, que tienen tamaño fijo).

Puntos: selección 2,5 c/u · completar 2,5 por espacio (40 fijos en Examen 1, 30 en Examen 2) · pareo 2,5 c/u · imágenes 30 · procesos 20 · desarrollo 5 por caso. **El total se calcula y se muestra antes de crear el examen y debe coincidir con la suma.**

Si el usuario manda un examen nuevo con otro formato, agrégalo como "Examen 3" en `PRESETS` y `FIXED`, con su orden de partes.

Para corregir respuestas cortas: sin tildes ni mayúsculas y aceptando sinónimos (claves en `k`). Usa `not` para evitar falsos aciertos ("no molde" ≠ "molde") y `'&a,b,c'` cuando se piden **varios** nombres a la vez ("replicación, transcripción y traducción").
