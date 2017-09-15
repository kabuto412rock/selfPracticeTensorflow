
# coding: utf-8

"""
配置tensorflow_object_detection模型的編譯路徑的腳本程式，
相當於 protoc object_detection/protos/*.proto --python_out=.

注意事項：
    1. 此程式是為了windows打造，並未在OSX/ Linux測試。
    2. 使用Anaconda的Python的話，請在Anaconda prompt中執行此程式。
    3. 請確保執行程式時的目錄是在model-master底下。
    4. 如果你的protobuf是在虛擬環境安裝，請記得先啟動虛擬環境再執行此程式。
"""
import os

proto_list = [
'anchor_generator.proto',
'argmax_matcher.proto',
'bipartite_matcher.proto',
'box_coder.proto',
'box_predictor.proto',
'eval.proto',
'faster_rcnn.proto',
'faster_rcnn_box_coder.proto',
'grid_anchor_generator.proto',
'hyperparams.proto',
'image_resizer.proto',
'input_reader.proto',
'losses.proto',
'matcher.proto',
'mean_stddev_box_coder.proto',
'model.proto',
'optimizer.proto',
'pipeline.proto',
'post_processing.proto',
'preprocessor.proto',
'region_similarity_calculator.proto',
'square_box_coder.proto',
'ssd.proto',
'ssd_anchor_generator.proto',
'string_int_label_map.proto',
'train.proto',
]

# 迭代proto_list
for inx, proto_str in enumerate(proto_list):
    print(inx, proto_str.strip())
    #執行命令
    os.system('protoc object_detection/protos/' + proto_str.strip() + ' --python_out=.')
    
print('如果沒報錯，就是成功！！！')

