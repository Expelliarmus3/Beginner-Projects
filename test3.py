def dup(nums):
    ls = []
    for items in nums:
        if items not in ls:
            ls.append(items)
    return ls
    return len(ls)
    
    
nums=[2,2]
ls=dup(nums)
print(ls)