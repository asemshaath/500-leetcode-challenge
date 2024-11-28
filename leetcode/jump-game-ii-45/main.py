    def jump(self, nums: List[int]) -> int:
        # [3,2,1]
        #  0 1 2 3 4
        #                   
        # curr 0

        goal_ind = len(nums) - 1
        steps = 0

        while goal_ind > 0:
            pre_goal = goal_ind - 1
            point_can_reach = pre_goal

            while pre_goal >= 0:
                # check if pre_goal can reach goal index 
                if nums[pre_goal] + pre_goal >= goal_ind:
                    point_can_reach = pre_goal
                pre_goal -= 1
            goal_ind = point_can_reach
            steps += 1
        
        return steps
