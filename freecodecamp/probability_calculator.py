
# !!! SUCCESS !!!
# PERFECTION


import random
import copy


class Hat:

    def __init__(self, **kwarg):
        contents = []
        for key in kwarg.keys():
            for i in range(kwarg[key]):
                contents.append(key)
        self.contents = contents


    def draw(self, balls):
        contents = self.contents
        if balls >= len(contents):
            return contents

        sample = []
        for x in range(balls):
            index = random.randrange(len(contents))
            ball = contents[index]
            sample.append(ball)
            contents = contents[0:index] + contents[index + 1:]

        self.contents = contents
        return sample


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for z in range(num_experiments):
            ex = copy.copy(hat)
            samp = ex.draw(num_balls_drawn)
            success = True
            for key in expected_balls.keys():
                if samp.count(key) < expected_balls[key]:
                    success = False
                    break
            if success:
                count += 1

    return count / num_experiments


hat1 = Hat(black=2, yellow=3, purple=5, orange=4)
probability = experiment(hat=hat1, 
                  expected_balls={"purple":2,"orange":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)