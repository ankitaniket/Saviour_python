sample_list = []
with open('input.txt','r') as f:
    l1 = f.read().split(', ')
    sample_list = [int(i) for i in l1]
    
    


print("Original list ", sample_list)

length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times
for i in range(3):
    # get indexes
    indexes = slice(start, end)
    
    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i+1, list_chunk)
    
    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size
