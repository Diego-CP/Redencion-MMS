_base_ = [
    '../_base_/models/encnet_r50-d8_copy.py', '../_base_/datasets/deepglobe_dataset_copy.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_20k_001.py'
]
crop_size = (256, 256)
data_preprocessor = dict(size=crop_size)
model = dict(data_preprocessor=data_preprocessor)
