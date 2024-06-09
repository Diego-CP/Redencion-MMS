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

### Conclusiones

En el ámbito de la segmentación semántica, la elección del modelo adecuado depende de los requisitos específicos de la aplicación y de los recursos disponibles. Cada modelo tiene sus propias ventajas y desventajas que deben ser consideradas:

1. **Deeplab** es reconocido como un modelo líder debido a su alta precisión en la segmentación semántica. Utiliza convoluciones atrous para mejorar la resolución de las características, lo que lo hace ideal para aplicaciones que requieren una segmentación detallada y precisa. Sin embargo, este nivel de detalle y precisión viene a un costo significativo en términos de recursos computacionales, lo que lo hace menos adecuado para entornos con limitaciones de hardware.

2. **CCNET**

3. **FCN (Fully Convolutional Network)** ofrece una gran adaptabilidad, siendo capaz de manejar entradas de tamaño variable y proporcionando segmentación en tiempo real. Sin embargo, su eficiencia en términos de velocidad puede no ser tan alta como la de modelos más optimizados para el rendimiento. Aun así, su versatilidad y capacidad para segmentar imágenes en tiempo real lo hacen adecuado para diversas aplicaciones donde la flexibilidad es esencial.

En resumen, Deeplab al ser el primer modelo, fue el más adecuado para obtener la mayor precisión posible y cuenta con los recursos computacionales necesarios. Por otro lado, CGNET es la mejor opción para aplicaciones móviles y entornos con recursos limitados, donde la eficiencia es clave. Finalmente, FCN ofrece una solución balanceada con una buena capacidad de adaptación y segmentación en tiempo real, aunque con posibles limitaciones en velocidad comparado con CGNET. La selección del modelo debe basarse en una evaluación cuidadosa de las necesidades específicas de la aplicación y los recursos disponibles.

4. **ENCNET**

5. **PSPNET**

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
   <br> comando para empezar a entrenar
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
