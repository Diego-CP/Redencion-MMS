## Desarrollo de aplicaciones avanzadas de ciencias computacionales (Gpo 301)

### Equipo 3: Redención

<img src="https://github.com/Diego-CP/Redencion-MMS/assets/70560259/e6c2aa44-b929-48c1-8152-71a57f767234" alt="PEDRO" width="300"/>
<br> Ariadne Alvarez Reyes                  | A01652080
<br> Diego Corrales Pinedo                  | A01781631
<br> Salvador Salgado Normandia             | A01422874

### Servidor para procesamiento

> [!IMPORTANT]
> IP: 10.49.37.230
> <br> Usuario: reto3
> <br> Contraseñas: R3t03
> <br> command: `ssh reto3@10.49.38.0` , `scp /folder/file.png reto3@10.49.38.0:~/mmsegmentation`

### Modelos

| Modelo  | Ventajas                                                                                                                                                   | Desventajas                                                                                                                                         | TL;DR                                                                                                                                                                                                                                 | Resultados                                                | Métodos Utilizados                                   | Limitaciones                                                                                                                                                                                                                                         | Contribuciones                                                                                                                                                                                                                                                                                               |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Deeplab | Incorpora la estructura de Atrous (dilated convolutions).                                                                                                  | Requiere poder computacional significativo.                                                                                                         | Deeplab es un modelo líder en la tarea de segmentación semántica.                                                                                                                                                                     | Precisión alta, Eficiencia computacional                  | Métodos de Atrous, Redes Neuronales Convolucionales  | Depende de recursos de hardware significativos.                                                                                                                                                                                                      | Contribuye a la mejora del rendimiento de la segmentación semántica en diversas aplicaciones.                                                                                                                                                                                                                |
| CGNET   | Eficiencia computacional gracias a su arquitectura ligera.                                                                                                 | Puede no ser tan preciso como otros modelos más complejos.                                                                                          | CGNET es un modelo ligero que prioriza la eficiencia computacional sin sacrificar demasiado la precisión.                                                                                                                             | Velocidad rápida, Eficiencia computacional                | Red Neuronal Convolucional, Eficiencia computacional | Menor precisión en comparación con modelos más complejos.                                                                                                                                                                                            | Contribuye a la eficiencia en aplicaciones móviles y en tiempo real.                                                                                                                                                                                                                                         |
| FCN     | Puede manejar entradas de tamaño variable.                                                                                                                 | Puede ser menos eficiente en términos de velocidad.                                                                                                 | FCN es un modelo versátil que puede manejar entradas de tamaño variable y proporciona segmentación en tiempo real.                                                                                                                    | Adaptabilidad, Flexibilidad                               | Red Neuronal Convolucional, Adaptabilidad            | Puede ser menos eficiente para aplicaciones en tiempo real con altos requisitos de velocidad.                                                                                                                                                        | Contribuye a la adaptabilidad de los modelos de segmentación para diversas aplicaciones.                                                                                                                                                                                                                     |
| CCNET   | La memoria de la GPU 11 veces menor a un bloque no local, al igual que tiene alta eficiencia computacional reduciendo los FLOPs en un 85%                  | CCNet puede ser sensible a la configuración de parámetros, lo que puede requerir experimentación y ajuste fino para obtener los mejores resultados. | Propone un módulo de atención recurrente en cruz para recolectar la información contextual de todos los píxeles en su camino en cruz, obteniendo así información contextual de la imagen completa de manera muy efectiva y eficiente. | La característica Criss Cross otorga una gran eficiencia. | Red Neuronal Convolucional, Adaptabilidad            | El uso de Criss-Cross requiere de una efectiva configuración para para obtener una eficiencia optima y evitar esfuerzos exesivos en al usar el modelo                                                                                                | Con la implementación de Criss-Cross, este modelo mejora de manera significativa la toma de información cotnextual de manera más precisa.                                                                                                                                                                    |
| ENCNET  | Mejora los resultados de segmentación semántica al capturar información contextual global y resaltar los mapas de características dependientes de la clase | Requiere de una mayor capacidad de computación en comparación a otros modelos como lo es FCN                                                        | FCN es un modelo versátil que puede manejar entradas de tamaño variable y proporciona segmentación en tiempo real.                                                                                                                    | Adaptabilidad, Flexibilidad                               | Red Neuronal Convolucional, Adaptabilidad            | Dado que el módulo se centra en capturar información contextual global, puede tener dificultades con los detalles finos dentro de una imagen, lo que podría afectar la calidad de la segmentación en áreas donde la delimitación precisa es crítica. | Mejora significativamente el rendimiento de las tareas de segmentación semántica al aprovechar la información contextual global y enfatizar las características específicas de cada clase, lo que en última instancia mejora la capacidad del modelo para etiquetar con precisión los píxeles de una imagen. |

### Comandos para la creación del ambiente y el entrenamiento

1. Crear ambiente openmmlab
   <br> `conda create --name openmmlab python=3.10`
   <br> `conda activate openmmlab`

2. Installar pythorch con la versión especificada
   <br> `conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=11.8 -c pytorch -c nvidia`
   <br> `pip install ftfy`
   <br> `pip install fsspec`
   <br> `conda install pytorch torchvision -c pytorch`

3. Installar ambiente mmcv
   <br> `pip install -U openmim`
   <br> `mim install mmengine`
   <br> `mim install "mmcv==2.1.0"`

4. Clonar este repositorio
   <br> `git clone -b master https://github.com/Diego-CP/Redencion-MMS`

5. Ubicar la carpeta en la que se va a trabajar
   <br> _CAMBIAR A CARPETA BASE CON cd_
   <br> `pip install -v -e .`

6. Paquetes de visualización
   <br> `pip install tensorboardX`
   <br> `pip install future tensorboard`

7. Entrenar
   <br> Comando para empezar a entrenar
   <br> DEEPLAB `python tools/train.py configs/deeplabv3/deeplabv3_deepglobe.py`
   <br> FCN `python tools/train.py configs/fcn/fcn_r50-d8_4xb2-40k_deepglobe-256x256.py`
   <br> PSPNet `python tools/train.py configs/pspnet/pspnet_deepglobe.py`
   <br> ENCNET `python tools/train.py configs/encnet/encnet_deepglobe.p`
   <br> CCNET `python tools/train.py configs/ccnet/ccnet_deepglobe.py`

8. Visualizar durante el entrenamiento
   <br> `tensorboard --logdir=<path_a_directorio_log> (ej. work_dirs\encnet_deepglobe\20240604_194534\vis_data)`

### Comandos para probar el modelo

- DeepLabV3 `python demo/image_demo.py data/deepglobe/test/<imagen_a_probar> configs/deeplabv3/deeplabv3_deepglobe.py work_dirs/deeplabv3_deepglobe/iter_20000.pth --device cuda:0 --out-file test_results/deeplabv3/<nombre_de_archivo_de_salida>`
- PSPNet `python demo/image_demo.py data/deepglobe/test/<imagen_a_probar> configs/pspnet/pspnet_deepglobe.py work_dirs/pspnet_deepglobe/iter_20000.pth --device cuda:0 --out-file test_results/pspnet/<nombre_de_archivo_de_salida>`
- FCN `python demo/image_demo.py data/deepglobe/test/810262_sat.jpg configs/fcn/fcn_r50-d8_deepglobe.py work_dirs/fcn_deepglobe/iter_20000.pth --device cuda:0 --out-file 810262_output.jpg`
- ENCNET `python demo/image_demo.py data/deepglobe/test/810262_sat.jpg configs/encnet/encnet_deepglobe.py work_dirs/fcn_deepglobe/iter_20000.pth --device cuda:0 --out-file 810262_output.jpg`
- CCNET `python demo/image_demo.py data/deepglobe/test/810262_sat.jpg configs/ccnet/ccnet_deepglobe.py work_dirs/ccnet_deepglobe/iter_20000.pth --device cuda:0 --out-file 810262_output.jpg`

### Scripts utilizados para el preprocesamiento

Estos scripts se pueden encontrar en la carpeta PreprocessingScripts:
- ImageSeparator: Used to separate the images (.jpg) from the masks (.png).
- NewImageClassConverter: Used to conver the masks (.png) to grayscale using the method seen in class.
- ImageResize: Used to downsize the images and masks to 256x256.

Se aplicaron de la siguiente manera.
1. ImageSeparator. Para separar las imágenes de las máscaras. Luego se dividieron en val_dir y img_dir manualmente, tomando las primeras 160 imágenes (y sus máscaras correspondientes) en orden de nombre para ponerlas en val_dir.

2. ImageResize a las imágenes (.jpg) en img_dir.

3. a. ImageResize a las máscaras (.png) en ann_dir. <br>
 b. NewImageClassConverter para convertir las máscaras reducidas a grayscale.

4. ImageResize a las imágenes en Test.
