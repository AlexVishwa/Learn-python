# import multiprocessing as mp

    
    # Output:
    #1056.2538455391366

class bsort:
    def __init__(self,arr):
        self.arr=arr
    def sort(self,arr):
        self.arr=arr
        for n in range(len(self.arr)-1,0,-1):
            for i in range(n):
                if(self.arr[i]>self.arr[i+1]):
                    temp=self.arr[i+1]
                    self.arr[i+1]=self.arr[i]
                    self.arr[i]=temp
        print("inside sort")
        return self.arr
    def binarys(self,list,x):
        l=0
        r=len(list)-1
        for i in range(len(list)):
            d=(l+r)/2
            if(x==list[d]):
                return d
            if(x<list[d]):
                r=d-1
            else:
                l=d+1
        print("inside binarys")
        return d
    def calcres(self,shoe_sizes):
        sorted_list=bsort.sort(shoe_sizes)
        cmp=0
        rep=0
        print("start")
        for i in range(len(sorted_list)):
            for j in range(len(sorted_list)):
                if(sorted_list[i]==sorted_list[j]):
                    rep+=1
            if(rep>cmp):
                cmp=rep
                d=bsort.binarys(sorted_list,sorted_list[i])
        print("here")
        print(shoe_sizes[d])
        return shoe_sizes[d]
if __name__ == "__main__":
    obj=bsort([2,45,68,34,23,56,78,90,12,34,56,78,90])
shoe_sizes = [2, 45, 68, 34, 23, 56, 78, 90, 12, 34, 56, 78, 90]
    result = obj.calcres(shoe_sizes)
    print("Result:", result)

    # def __init__(self,deg):
    #     self.deg=deg

    # def func1(self,num):
    #     p = 1
    #     for i in range(1, num + 1):
    #         p *= i
    #     return p

    # def compute_chunk(self,start, end, deg):
    #     s = 0
    #     for i in range(start, end, 4):
    #         s += (deg ** i) / func1(self,i)
    #     for j in range(start + 2, end, 4):
    #         s -= (deg ** j) / func1(self,j)
    #     return s

    # def funcnew(deg):
    #     num_processes = mp.cpu_count()
    #     chunk_size = 15000 // num_processes
    #     pool = mp.Pool(processes=num_processes)
        
    #     results = [pool.apply_async(compute_chunk, args=(i, i + chunk_size, deg)) for i in range(0, 15000, chunk_size)]
    #     pool.close()
    #     pool.join()
        
    #     return 1 + sum(result.get() for result in results)

    # if __name__ == "__main__":
    #     pass
        # print(funcnew(45))