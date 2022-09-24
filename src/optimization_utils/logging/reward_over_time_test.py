import unittest
from reward_over_time import RewardOverTime

class RewardOverTimeTest(unittest.TestCase):

    def test_reward_mean(self):
        reward = RewardOverTime()
        for i in range(1000):
            reward.update(10)
        
        assert reward.value > 9
        assert reward.value < 10
        
    
    def test_reward_convergence(self):
        reward = RewardOverTime()
        reward.update(5)
        reward.update(15)
        reward.update(20)
        
        assert  10 <= reward.value 
        assert  reward.value <= 18
    

if __name__ == '__main__':
    unittest.main()
