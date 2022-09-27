
"""
    function:非极大值抑制
    date:2022.7.23

    算法过程:
    1.根据候选框的类别分类概率做排序：A<B<C<D<E<F
    2.先标记最大概率矩形框F是我们要保留下来的
    3.从最大概率矩形框F开始，分别判断A~E与F的IOU是否大于某个设定的阈值，假设B、D与F的重叠度超过阈值，那么就扔掉B、D
    4.从剩下的矩形框A、C、E中，选择概率最大的E，标记为要保留下来的，然后判读E与A、C的重叠度，扔掉重叠度超过设定阈值的矩形框
    5.就这样一直重复下去，直到剩下的矩形框没有了，标记完所有要保留下来的矩形框
"""
import numpy as np


def py_nms(dets, thresh):
    #x1、y1、x2、y2、以及score赋值
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]

    #每一个候选框的面积
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    #order是按照score降序排序的
    order = scores.argsort()[::-1]      # np.argsort()是按照axis排序，返回排序后的下标（升序）

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)          # 该次循环最大的框保留，其他的跟他计算，看是否舍去
        # 计算当前概率最大矩形框与其他矩形框的overlap框的坐标，会用到numpy的broadcast机制，得到的是向量
        # 因为计算的是相交部分，所以x1y1用的是max，x2y2用的是min
        xx1 = np.maximum(x1[i], x1[order[1:]])      # np.maximun用于逐元素比较两个array的大小。
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        # 计算相交框的面积,注意矩形框不相交时w或h算出来会是负数，用0代替
        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h       # inter就是最大score的框与其他框相交面积的大小，不相交的为0
        # 计算IOU：重叠面积/（面积1+面积2-重叠面积）
        ovr = inter / (areas[i] + areas[order[1:]] - inter)

        # 找到重叠度不高于阈值的矩形框索引（高于的话认为是同一个框，只保留最大的，所以舍弃，低于的话说明这是另一个目标了，可以放进去下一次循环）
        inds = np.where(ovr <= thresh)[0]
        # 将order序列更新，由于前面得到的矩形框索引要比矩形框在原order序列中的索引小1，所以要把这个1加回来
        order = order[inds + 1]
    return keep


def main():
    dets = np.array([[30, 20, 230, 200, 1], 
                    [50, 50, 260, 220, 0.9], 
                    [210, 30, 420, 5, 0.8], 
                    [430, 280, 460, 360, 0.7]])
    
    threshold = 0.35
    keeo_dets = py_nms(dets, threshold)     # 返回的是框的下标编号
    print(keeo_dets)
    print(dets[keeo_dets])


if __name__ == '__main__':
    main()




"""
    function:非极大值抑制
    date:2022.9.27
    不用numpy实现
"""
def nms(points, threshold):

    # 1. 计算每个矩形框的面积
    x1 = [point[0] for point in points]
    y1 = [point[1] for point in points]
    x2 = [point[2] for point in points]
    y2 = [point[3] for point in points]
    scores = [point[4] for point in points]
    # areas = list(map(lambda point: (point[2] - point[0] + 1) * (point[3] - point[1] + 1), points))
    areas = [(x2_ - x1_ + 1) * (y2_ - y1_ + 1) for (x1_, y1_, x2_, y2_) in zip(x1, y1, x2, y2)]
    
    # 2. 获得每个矩形框的下标（经过倒序的）
    order = list(zip(scores, range(len(scores))))
    order = sorted(order, key=lambda order:order[0], reverse=True)
    order = [x[1] for x in order]

    # 3. 开始nms
    remain_points = []
    while len(order) > 0:
        i = order[0]
        remain_points.append(i)

        # 计算相交部分的面积x1[order[1:]]

        xx1 = [max(a1, a2) for (a1, a2) in zip([x1[i] for _ in range(len(order) - 1)], [x1[j] for j in order[1:]])]
        yy1 = [max(a1, a2) for (a1, a2) in zip([y1[i] for _ in range(len(order) - 1)], [y1[j] for j in order[1:]])]
        xx2 = [min(a1, a2) for (a1, a2) in zip([x2[i] for _ in range(len(order) - 1)], [x2[j] for j in order[1:]])]
        yy2 = [min(a1, a2) for (a1, a2) in zip([y2[i] for _ in range(len(order) - 1)], [y2[j] for j in order[1:]])]

        # w = list(map(lambda x2, x1: (x2 - x1 + 1), xx2, xx1))
        w = [(x2 - x1 + 1) for (x1, x2) in zip(xx1, xx2)]
        w = [max(0, x) for x in w]
        # h = list(map(lambda y2, y1: (y2 - y1 + 1), yy2, yy1))
        h = [(y2 - y1 + 1) for (y1, y2) in zip(yy1, yy2)]
        h = [max(0, x) for x in h]

        inter = [x * y for (x, y) in zip(w, h)]

        iou = [inter_ / (area1 + area2 - inter_) for (inter_, area1, area2) in zip(inter, [areas[i] for _ in range(len(order) - 1)], [areas[j] for j in order[1:]])]
        
        ious = list(zip(iou, range(len(iou))))
        inds = []
        for aaa in ious:
            if aaa[0] < threshold:
                inds.append(aaa[1] + 1)
        
        new_order = []
        for i in range(len(inds)):
            new_order.append(order[inds[i]])
        order = new_order
    return remain_points


def main():
    points = [[30, 20, 230, 200, 1], 
            [50, 50, 260, 220, 0.9], 
            [210, 30, 420, 5, 0.8], 
            [430, 280, 460, 360, 0.7]]
    
    threshold = 0.35
    remain_points = nms(points, threshold)
    print(remain_points)
    for i in remain_points:
        print(points[i])


if __name__ == '__main__':
    main()