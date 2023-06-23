import numpy as np
from sklearn.utils.linear_assignment_ import linear_assignment

class NearestNeighborDistanceMetric:
    def __init__(self, metric, matching_threshold, budget=None):
        self.metric = metric
        self.matching_threshold = matching_threshold
        self.budget = budget

    def distance(self, items, targets):
        # Implementa el cálculo de la distancia entre `items` y `targets`
        pass

    def match(self, items, targets):
        if len(targets) == 0 or len(items) == 0:
            return [], [], list(range(len(targets)))

        cost_matrix = self.distance(items, targets)
        indices = linear_assignment(cost_matrix)

        matches, unmatched_items, unmatched_targets = [], [], []
        for item, target in indices:
            if cost_matrix[item, target] > self.matching_threshold:
                unmatched_items.append(item)
                unmatched_targets.append(target)
            else:
                matches.append((item, target))

      unmatched_items += [i for i in range(len(items)) if i not in [item for item, _ in indices]]
        unmatched_targets += [i for i in range(len(targets)) if i not in [target for _, target in indices]]

        return matches, unmatched_items, unmatched_targets
