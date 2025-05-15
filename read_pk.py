import pickle
import numpy as np
def load_pickle_file(file_path):
    """
    读取 pickle 文件并返回其内容。

    参数:
    - file_path: 文件路径，指向 pickle 文件。

    返回:
    - 文件中存储的 Python 对象。
    """
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        print("错误：文件未找到，请检查路径。")
    except pickle.PickleError as e:
        print(f"错误：pickle 文件读取出错：{e}")
    except Exception as e:
        print(f"发生错误：{e}")

# 使用示例
file_path = './data/0.25deg_4D_5×5/oxygen_meanstd_2.pkl'
data = load_pickle_file(file_path)
print(len(data[0]))
if np.isnan(data[1]).any():
    print(" self.train_std::发现 NaN 值!")
    nan_indices = np.where(np.isnan(data[1]))[0]
    print("NaN 值的位置:", nan_indices)
