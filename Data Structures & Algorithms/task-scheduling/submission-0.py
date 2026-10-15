class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        initially, I thought about creating a set and hash table for all tasks
        then a PQ to imitate task scheduling
        But,
        I thought of a hash freq max heap and a cooldown dict and pq list
        The issue there is how to keep track of the cooldown dict and 
        where does the items we pop from hash freq go
        
        After looking deeper into the problem
        I decided on 
        2 heaps:
            min_heap - waiting room where all popped tasks go: (cooldown, count)
            max heap - PQ where all tasks are ready to cycle (count)
        timer variable
            it will count the total cycles
        
        tasks = ["X","X","Y","Y"], n = 2
        cycles = 0:
        count_heap[ 2, 2 ]
        waiting_room_heap[]
        completed[]
        1:
        [2]
        [[1+2,2-1]] = [[3,1]]
        [x]
        2:
        []
        [[3,1], [4,1]]
        [x,y]
        3:
        []
        []
        [x,y,_]
        '''        
        #setup of maxheap
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
        
            while waiting_room_heap and waiting_room_heap[0][0] <= curr_cycles:
                temp = heapq.heappop(waiting_room_heap)
                heapq.heappush_max(count_heap, temp[1])

        return curr_cycles








        