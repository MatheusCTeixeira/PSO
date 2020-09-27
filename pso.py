import numpy as np

class PSO:
    def __init__(self, n_particles, n_dimensions, aceleration_const, bounds):
        self._n_particles = n_particles
        self._n_dimensions = n_dimensions
        self._acceleration = aceleration_const
        self._bounds = bounds
        self._particles = np.random.random(size=(n_particles, n_dimensions))


    def fit(max_iters, g, f):
        ac1, ac2 = self._acceleration
        v_min, v_max = self._bounds
        best_individual = None
        self._v = np.random.uniform(v_min, v_max, self._particles.shape)

        for t in range(max_iters):
            # find best individuas from population
            pop = [(i, g(x)) for x in self._particles]
            pop.sort(key=lambda x: x[1], reverse=True)
            best_individual = self._particles[pop[0][0]]

            pop.sort(key=lambda x:x[0]) # avoid re-evalute fitness
            for i in range(self._n_particles):
                # find best neighbor
                l, r = (i - 1) % self._n_particles, (i + 1) % self._n_particles
                best_neighbor = self._particles[l if pop[l][1] < pop[r][1] else r]
                
                # calculate velocity
                x = self._particles[i]
                dv = self._v[i] + ac1 * (best_individual - x) +
                                  ac2 * (best_neighbor   - x)
                dv = np.clip(dv, v_min, v_max) # keep on range
                self._particles[i] += dv

            # TODO create a temporary new population to store parcial operation
            # while the current iteration is running.


                
def main():
    pass


if __name__ == "__main__":
    main()
