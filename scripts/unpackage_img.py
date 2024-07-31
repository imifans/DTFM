import numpy as np
from PIL import Image
import os

# 加载 .npz 文件
data = np.load('/tmp/openai-2024-07-29-21-31-15-891614/samples_64x256x256x3.npz')

# 访问数组
array1 = data['arr_0']

# 获取图片数量
num_images = array1.shape[0]

# 确定当前路径
output_dir = '../saved_images'
os.makedirs(output_dir, exist_ok=True)  # 创建目录（如果不存在）

# 保存每一张图片
for i in range(num_images):
    img = Image.fromarray(array1[i].astype(np.uint8))  # 转换为 PIL 图像
    img.save(os.path.join(output_dir, f'image_{i}.png'))  # 保存为 PNG 文件

print(f"Saved {num_images} images to {output_dir}.")
