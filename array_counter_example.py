
def solution(N, A):
    counter = [0] * N
    current_max = 0
    max_counter = 0
    for i in A:
        x = i - 1
        if i > N: # set max_counter, no need to increment the element counter
            max_counter = current_max
        elif counter[x] < max_counter: #if counter value less than max_counter, set to max_counter and then increment 1
            counter[x] = max_counter + 1
        else: #increment the counter
            counter[x] += 1

        #set max_counter elements which is less
        if i <= N and counter[x] > current_max:
            current_max = counter[x]

    for i in range (0, len(counter)):
        if counter[i] < max_counter:
            counter[i] = max_counter
    print(counter)

arr_size = 5
increment_order = [3, 4, 4, 6, 1, 4, 4]
solution(arr_size, increment_order)

# increment the counter value of array item in the order mentioned in increment_order
# if value increment_order greater than arr_size set the all counter value to max




