class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_table = {} # hash table
        for i in tasks:
            count_table[i] = count_table.get(i,0) + 1
        # print(f"table is {count_table} ")

        # we dont even need to keep the key since we only care for the count
        count_heap = list(count_table.values()) # tracks all counts of each task
        heapq.heapify_max(count_heap)
        waiting_room_heap = []


        curr_cycles=0
        while count_heap or waiting_room_heap:
            #cleanup - moving waiting room tasks to heap so all we can just see which tasks are available each cycle
            curr_cycles += 1

            if count_heap:# if task is in the heap
                #settle current task
                count = heapq.heappop_max(count_heap)-1 #remaining items = works here too
                if count != 0:   
                    heapq.heappush(waiting_room_heap, (curr_cycles + n, count))
            #waiting room holds (time to reset, count of tasks)
            #checks if there are values in waiting room and if the earliest timer task can reset
            while waiting_room_heap and waiting_room_heap[0][0] <= curr_cycles:
                temp = heapq.heappop(waiting_room_heap)
                heapq.heappush_max(count_heap, temp[1]) # only push count of tasks

        return curr_cycles