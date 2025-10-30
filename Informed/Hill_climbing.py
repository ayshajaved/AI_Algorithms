class HillClimber:
    def __init__(self, start_x, step_size=0.1, max_iterations=1000):
        self.x = start_x
        self.step_size = step_size
        self.max_iterations = max_iterations

    def f(self, x):
        return -(x - 3)**2 + 9   # Parabola with maximum at x = 3

    def climb(self):
        for _ in range(self.max_iterations):
            next_x = self.x + self.step_size
            prev_x = self.x - self.step_size

            if self.f(next_x) > self.f(self.x):
                self.x = next_x
            elif self.f(prev_x) > self.f(self.x):
                self.x = prev_x
            else:
                break  # stop climbing if no better neighbor found

        return self.x, self.f(self.x)


class Main:
    def run():
        hill = HillClimber(start_x=-5.0)    
        x_max, f_max = hill.climb()
        print("Starting at x =", -5.0)
        print("Maximum found at x =", round(x_max, 2), "with f(x) =", round(f_max, 2))

if __name__ == "__main__":  
    Main.run()