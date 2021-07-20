import csv


# 直接读取文件
def read_csv_all(file_name):
    """按行读取csv数据"""
    file = open(file_name, "r")
    line_data = csv.reader(file)
    csv_dataset = list(line_data)
    return csv_dataset


# 读取CSV 去除空行
def read_csv(file_name):
    """按行读取csv数据，去掉空行数据"""
    csv_dataset = list()
    with open(file_name, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if not row:
                continue
            csv_dataset.append(row)
    return csv_dataset


# 集合字符串 转成 浮点型
def convert_str_to_float(dataset, column):
    """ 集合字符串 转成 浮点型 """
    # 集合截取 从index 1-n
    dataset = dataset[1:]
    for row in dataset:
        # strip 去除字符串前后空格
        row[column] = float(row[column].strip())


# 主函数执行入口
def main():
    file_path_name = "data/diabetes.csv"
    dataset = read_csv(file_path_name)
    for i in range(len(dataset[0])):
        convert_str_to_float(dataset, i)
    print(dataset)


if __name__ == '__main__':
    main()


