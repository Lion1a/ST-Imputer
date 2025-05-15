import pandas as pd
import numpy as np
import pickle


def calculate_mean_and_std(file_path):
    """
    读取包含时间和多个经纬度值的逗号分隔文本文件，并计算每一列的平均值和标准差。

    参数:
    - file_path: 文件路径，指向文本文件。

    返回:
    - 一个包含每一列平均值和标准差的元组（两个 NumPy 数组）。
    """
    try:
        # 读取数据，使用逗号作为分隔符
        df = pd.read_csv(file_path, header=None)

        # 计算每一列的平均值和标准差
        means = df.iloc[:, 1:].mean().to_numpy()
        stds = df.iloc[:, 1:].std().to_numpy()
        # 用 1 替代标准差中的 NaN 值
        stds = np.nan_to_num(stds, nan=1)

        return (means, stds)
    except FileNotFoundError:
        print("错误：文件未找到，请检查路径。")
    except pd.errors.EmptyDataError:
        print("错误：文件为空。")
    except Exception as e:
        print(f"发生错误：{e}")


def save_to_pickle(means, stds, pickle_path):
    """
    将平均值和标准差 NumPy 数组保存到 pickle 文件中。

    参数:
    - means: 平均值 NumPy 数组。
    - stds: 标准差 NumPy 数组。
    - pickle_path: pickle 文件路径。
    """
    try:
        with open(pickle_path, 'wb') as file:
            pickle.dump([means, stds], file)
        print(f"数据已成功保存到 {pickle_path}")
    except Exception as e:
        print(f"发生错误：{e}")


# 使用示例
file_path = './data/0.25deg_4D_5×5_4rows_2/GLODAPv2.2023_140E-145E_30N-35N_0.25deg14_2.txt'
pickle_path = './data/0.25deg_4D_5×5_4rows_2/oxygen_meanstd_2.pkl'

# 计算平均值和标准差
means, stds = calculate_mean_and_std(file_path)

# 如果计算成功，保存结果到 pickle 文件
if means is not None and stds is not None:
    save_to_pickle(means, stds, pickle_path)
