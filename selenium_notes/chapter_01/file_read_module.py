import xlrd


def readtext(path):
    """
    读取txt配置文件
    :param path: 需要读取的txt文件路径
    :return: 返回json数据格式
    """
    result = []
    info = []
    config = open(path, 'r')
    # info = {j: i.split("=")[index + 1].strip("\n") for i in config for index, j in enumerate(i.split("=")) if
    #         index == 0}
    # result.append(info)
    for line in config:
        line = line.strip().split("=")
        info.append(line)
    result.append(dict(info))
    config.close()
    return result


class OperationExcel:
    def __init__(self, path, sheet):
        """
        注意:此方法需要求修改Excel表格格式为文本格式
        :param path: Excel文件路径
        :param sheet: 指定sheet名称
        """

        self.xl = xlrd.open_workbook(path)
        self.sh = self.xl.sheet_by_name(sheet)
        # 获取第一行作为key值
        self.keys = self.sh.row_values(0)
        # 获取总行数
        self.rowNum = self.sh.nrows
        # 获取总列数
        self.colNum = self.sh.ncols

    def read_excel_row(self):
        """
        读取指定行数据
        :return: 返回一个字典
        """
        # 获取表头作为字典的键
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                values = self.sh.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

# if __name__ == '__main__':
#     # filePath = r"D:\PythonLen\test.txt"
#     filePath = r'E:\PythonFiles\cloudvastAutoTest\data\TestData.xlsx'
#     xl = OperationExcel(filePath, "sheet1")
#     di = xl.read_excel_row()
#     # di = readtext(filePath)
#     print(di)
