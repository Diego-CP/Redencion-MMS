## Desarrollo de aplicaciones avanzadas de ciencias computacionales (Gpo 301)
### Equipo 3: Redención
<br> Ariadne Alvarez Reyes                  | A01652080
<br> Diego Corrales Pinedo                  | A01781631
<br> Salvador Salgado Normandia             | A01422874

### Servidor para procesamiento
<br> IP: 10.49.37.230
<br> Usuario: reto3
<br> Contraseñas: R3t03
<br> command: scp /folder/file.png reto3@10.49.37.230:~/mmsegmentation

### Modelos
| Deeplab| CGNET    | FCN     |
|----------------|--------------|-------------|
|    | 	 |  |
|  |   |  |
|   |   |   |

### Comandos para la creación del ambiente y el entrenamiento
conda create --name openmmlab python=3.10
conda activate openmmlab

conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=11.8 -c pytorch -c nvidia

pip install ftfy
pip install fsspec

conda install pytorch torchvision -c pytorch

pip install -U openmim
mim install mmengine
mim install "mmcv==2.1.0"

git clone -b master https://github.com/Diego-CP/Redencion-MMS

*CAMBIAR A CARPETA BASE CON cd*
pip install -v -e .

python tools/train.py configs/deeplabv3/deeplabv3_deepglobe.py

