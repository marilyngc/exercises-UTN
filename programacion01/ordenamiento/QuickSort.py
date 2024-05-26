def quick_sort(array,low,high):
    if low < high:
        #dividir y acomodar pivote
        pivote = partition(array,low,high)
        
        quick_sort(array,low, pivote - 1)
        quick_sort(array, pivote + 1,high)