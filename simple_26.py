#coding=utf-8

'''
题目：删除排序数组中的重复项
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成

解题思路：由于是排序数组，所有直接倒序遍历，比较前后两个数，如果后面的数与前面的数相同，就直接删除后面的数
'''



def delete(list):
    for i in range(len(list)-1, 0, -1):
        if list[i] == list[i-1]:
            list.remove(list[i])
    print list
	

#delete([1,2,2,2,3,3,4])
#[1,2,3,4]

