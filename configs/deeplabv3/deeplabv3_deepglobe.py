_base_ = [
    '../_base_/models/deeplabv3_r50-d8.py', '../_base_/datasets/deepglobe_dataset.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_1k.py'
]
crop_size = (512, 1024)
data_preprocessor = dict(size=crop_size)
model = dict(data_preprocessor=data_preprocessor)
