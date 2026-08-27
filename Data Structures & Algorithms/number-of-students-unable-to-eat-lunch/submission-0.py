class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        

        # students = [1,1,0,0], sandwiches = [0,1,0,1]
        
        #populate the queue
        queue = deque(students)

        stop = True
        
        # sandwiches we use the stack methods
        queue_sandwiches = deque(sandwiches)

        i = 0
        while i < len(queue):
            
            # front student
            front_student = queue[0]

            # top sandwich
            top_sandwich = queue_sandwiches[0]
            i+=1
            if top_sandwich == front_student:
                queue.popleft()
                queue_sandwiches.popleft()
                i = 0
            else:
                # student at front goes to the back
                queue.append(queue.popleft())
            

        
        return len(queue)
