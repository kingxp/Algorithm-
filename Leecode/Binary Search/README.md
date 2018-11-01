Binary Search 二分查找

要求：
1.线性表必须采用顺序存储结构（vector的结构就可以）
2.表中原始按关键字有序排列

一般的程序
while(low<=high)
        {
            int mid=low+(high-low)/2;
            if(array[mid]>target)
                high=mid-1;
            else if(array[mid]<target)
            low=mid+1;
            else
                return mid;
        }
    return-1;

难点：
1.中间点的选择：
	选择的可能有两个，第一个是前中 (left+right)/2 第二个是后中 (left+right+1)/2
	选择的这两种可能，一般最好选择后中，前中很有可能出现循环出不来的情况
	
2.循环终止点的选择：
	选择的可能有两个，第一个是left>right,第二个是left>=right
	一般选择left>right

3.跳出循环后，选择是返回-1

