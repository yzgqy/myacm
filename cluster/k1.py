# -*- coding:utf-8 -*-
from sklearn.cluster import KMeans
# from sklearn.cluster import k_means#这个是先写的，他们两的参数就相差一个数据集，不过还是建议用KMeans
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing


def loadData(filePath):
    dataSet = []
    file = open(filePath, 'r')

    for lines in file.readlines():
        row = []
        # curLine = lines.strip().split()#２维数据
        curLine = lines.strip().split(',')
        for line in curLine:
            x = float(line)
            row.append(x)

        dataSet.append(row)
    file.close()

    return np.mat(dataSet)


if __name__ == '__main__':
    # X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
    # kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    # print(kmeans.labels_);
    # print("评价聚类好坏")
    # print(kmeans.score(X))

    filePath = '/Users/yaya/Desktop/kdata2.txt'
    dataSet = loadData(filePath)
    # print(dataSet)

    # min_max_scaler = MinMaxScaler()
    # standard_scaler = StandardScaler()
    # scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
    # dataSet = scaler.fit_transform(dataSet)

    # print(dataSet)

    # print dataSet
    '''直接调用sklearn中的数据'''
    # dataSet = load_iris().data
    estimator = KMeans(n_clusters=4, max_iter=300, n_init=10).fit(dataSet)  # 构造聚类器
    '''这个是必须写的，相当于上面构造出来，配置好，下面这句调用，当然也可以写到上面去
    fit方法对数据做training 并得到模型'''
    # estimator.fit(dataSet)#聚类

    # 下面是三个属性
    '''把聚类的样本打标签'''
    labelPred = estimator.labels_
    '''显示聚类的质心'''
    centroids = estimator.cluster_centers_
    '''这个也可以看成损失，就是样本距其最近样本的平方总和'''
    inertia = estimator.inertia_

    print("把聚类的样本打标签")
    print(labelPred)
    print("显示聚类的质心")
    print(centroids)
    print("样本距其最近样本的平方总和")
    print(inertia)
    # 这下面是库里包装的方法
    '''返回预测的样本属于的类的聚类中心'''
    print("返回预测的样本属于的类的聚类中心")
    print(estimator.fit_predict(dataSet))
    print(" ")
    print(estimator.predict(dataSet))
    '''这个是返回每个样本与聚类质心的距离'''
    print("每个样本与聚类质心的距离")
    print(estimator.fit_transform(dataSet))
    print(" ")
    print(estimator.transform(dataSet))
    '''这个我觉得和损失一样，评价聚类好坏'''
    print("评价聚类好坏")
    print(estimator.score(dataSet))
