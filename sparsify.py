import numpy as np
import scipy.sparse as sp
import networkx as nx
from sklearn import random_projection

# Visualize the test graph
rows, cols = A.nonzero()
edges = zip(rows.tolist(), cols.tolist())
gr = nx.Graph()
gr.add_edges_from(edges)
nx.draw(gr)
plt.show()

transformer = random_projection.SparseRandomProjection()

def construct_matrices(A):
    L = sp.csgraph.laplacian(A)
    



def approximate_resistances(L):
    pass


# Construct a random adjacency matrix for testing
n = 10
m = 20
A = sp.coo_matrix((np.ones(m), (np.random.randint(n, size=m), np.random.randint(n, size=m))), shape=[n, n])