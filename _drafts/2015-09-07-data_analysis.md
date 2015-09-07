**学习前需要安装的python包**
    
    pip install numpy matplotlib pandas

## pandas的学习

    + 从csv文件中数据
        
        import pandas
        data = pandas.read_csv(csv_path, sep=’;’, encoding=”utf8”, parse_date=[“Date”], index_col=”Date”)

        上述的参数中,设置编码为utf8,各列以;进行分割,解析Date列的数据,同时设置Date列为索引列
    + 选择其中的某一列
        
        data[colume]读取其中的某一个列的数据
    + css
    + css
