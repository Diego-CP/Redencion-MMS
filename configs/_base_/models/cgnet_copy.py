# model settings
norm_cfg = dict(type='SyncBN', eps=1e-03, requires_grad=True)
data_preprocessor = dict(
    type='SegDataPreProcessor',
    mean=[0.4089, 0.3800, 0.2826],
    std=[0.1112, 0.0890, 0.0800],
    bgr_to_rgb=True,
    pad_val=0,
    seg_pad_val=255)
model = dict(
    type='EncoderDecoder',
    data_preprocessor=data_preprocessor,
    backbone=dict(
        type='CGNet',
        norm_cfg=norm_cfg,
        in_channels=3,
        num_channels=(32, 64, 128),
        num_blocks=(3, 21),
        dilations=(2, 4),
        reductions=(8, 16)),
    decode_head=dict(
        type='FCNHead',
        in_channels=256,
        in_index=2,
        channels=256,
        num_convs=0,
        concat_input=False,
        dropout_ratio=0,
        num_classes=7,
        norm_cfg=norm_cfg,
        loss_decode=dict(
            type='CrossEntropyLoss',
            use_sigmoid=False,
            loss_weight=1.0,
            class_weight=[55.68959465460004, 9.006538451016333, 1.7436412216779034, 12.447446612739096, 9.272298479849635, 33.8297979266833, 12.611318258881342])),
    # model training and testing settings
    train_cfg=dict(sampler=None),
    test_cfg=dict(mode='whole'))
