nums = [2,11,7,15]
target = 9
soma = 0
lista = []
for i in range(len(nums) - 1):
    if i < len(nums):
        soma = nums[i] + nums[i+1]
        if (soma == target):
            lista.append(i)
            lista.append(i+1)
            print(lista)
    else:
        soma = nums[i]
        if (soma == target):
            lista.append(lista)
    
