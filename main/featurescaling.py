# 从数据集中找到列数据 最大值与最小值
def find_list_max_min(dataset):
    max_min = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        max_val = max(col_values)
        min_val = min(col_values)
        max_min.append([max_val, min_val])
    return max_min


# 数据标准化 x^ = x-min(x)/max(x)-min(x)
def max_min_normalization(dataset, max_min):
    for row in dataset:
        for i in range(len(row)):
            max_val = max_min[i][0]
            min_val = max_min[i][1]
            row[i] = (row[i]-min_val)/(max_val-min_val)


# average dataset col values 平均值
def average_dataset(dataset):
    avg = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        sum_val = sum(col_values)
        length = len(col_values)
        avg_val = sum_val/length
        avg.append(avg_val)
    return avg


# Standardization


# 主函数执行入口
def main():
    dataset = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]
    avg_dataset = average_dataset(dataset)
    print(avg_dataset)


if __name__ == '__main__':
    main()