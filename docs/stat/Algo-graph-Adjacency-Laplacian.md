book: [Spectral and Algebraic Graph Theory](http://cs-www.cs.yale.edu/homes/spielman/sagt) Daniel A. Spielman Yale University

## 邻接矩阵 Adjacency matrix

### Spectral Theorem of real symmetric matrices 实对称矩阵的性质

- 参见 [Eigendecomposition of a matrix](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix); [Spectral theorem](https://en.wikipedia.org/wiki/Spectral_theorem).

Theorem 1(**spectral theorem**). Any real symmetric matrix $A \in \mathbb{R}^{n \times n}$ has $n$ unit orthogonal eigenvectors $\Phi_{1}, \Phi_{2}, \cdots, \Phi_{n}$ corresponding to $n$ real eigenvalues $\alpha_{1} \geq \alpha_{2} \geq \cdots \geq \alpha_{n}$, which means $A$ can be decomposed as
$$
A=\sum_{i=1}^{n} \alpha_{1} \Phi_{i} \Phi_{i}^{T}
$$
Theorem 2. For any real symmetric matrix $A \in \mathbb{R}^{n \times n}$ with eigenvalues $\alpha_{1} \geq \alpha_{2} \geq \cdots \geq \alpha_{n}$, it holds that
$$
\alpha_{1}=\max _{x \in \mathbb{R}^{n}} \frac{x^{T} A x}{x^{T} x}
$$
Similarly
$$
\alpha_{n}=\min_{x \in \mathbb{R}^{n}} \frac{x^{T} A x}{x^{T} x}
$$
Moreover, $\Phi_{1}$ maximize the Rayleigh quotient and $\Phi_{n}$ minimize the Rayleigh quotient.

上面第一条定理, 即实对称矩阵的正交分解. 第二条定理则说明, 实对阵矩阵的特征值给定了该矩阵所对应的瑞丽商上界限.

### 邻接矩阵的 Largest eigenvalue

下面的定理说明, 邻接矩阵的最大特征值与节点的度数相关. 当 $\alpha_{1}=d_{\max }$ 时, 说明该图的度分布是完全相同的 (也即 [regular](https://en.wikipedia.org/wiki/Regular_graph))

Lemma 3. For any graph, the largest eigenvalue $\alpha_{1}$ of its adjacency matrix satisfies
$$
d_{a v e} \leq \alpha_{1} \leq d_{\max }
$$
Lemma 4. If $G$ is connected and $\alpha_{1}=d_{\max }$, then $G$ is $d_{\max }$-regular.

### Perron-Frobenius theory

Theorem 5 (**Perron-Frobenius** for undirected graphs). For any connected (weighted) graph $G$, we have

1. $\alpha_{1} \geq-\alpha_{n}$
2. $\alpha_{1}$ has a strictly positive eigenvector 特征向量的每一项都严格大于0
3. $\alpha_{1}>\alpha_{2}$.

- Frobenius 定理说明了连通图上的邻接矩阵的特征值特性.
- 证明思路
    - 第一条. 构造一个向量为最小特征值所对应的特征向量取正, 即 $x(i)=\left|\Phi_{n}(i)\right|$, 则有:
        - $\left|\alpha_{n}\right|=\left|\Phi_{n}^{T} A \Phi_{n}\right|=\left|\sum_{(i, j) \in E} a_{i, j} \Phi_{n}(i) \Phi_{n}(j)\right| \leq \sum_{(i, j) \in E} a_{i, j}\left|\Phi_{n}(i) \Phi_{n}(j)\right|=x^{T} A x \leq \alpha_{1}$.
  
    - 第二条. 构造向量y为 $y(i)=\left|\Phi_{1}(i)\right|$, 类似的, 我们可以得到 $y^{T} A y \geq \Phi_{1}^{T} A \Phi_{1}=\alpha_{1}$, 因此y也是最大特征值所对应的特征向量 (注意一个特征值对应的特征向量可以有很多). 再利用反正法, 假如y的某一元素为0, 则 $0=\alpha_{1} y(i)=(A y)(i)=\sum_{(i, j) \in E} y(j)$ 也即, 所有有边连接的节点的y信号均为0, 又因为图为连通图, 因此y就变为全零向量, 与特征向量的定义矛盾.
    - 第三条. 假设y为第一个特征值所对应的全正的特征向量, 假设 $\Phi_{2}$ 为与y正交的第二个特征值所对应的特征向量, 则该向量中, 一定既有正元和有负元, 因此, 在该连通图上一定有一条边, 使得 $\Phi_{2}(i)<0<\Phi_{2}(j)$. 因此, 令 $z(i)=\left|\Phi_{2}(i)\right|$, 则 $\alpha_{2}=\Phi_{2}^{T} A \Phi_{2}<z^{T} A z \leq \alpha_{1}$ 中的严格小于成立.
  

### 二分图 Bipartite graph

- 二分图定义: 可将节点分为两部分 $L, R$, 使得所有边都在两个集合之间, 不存在集合内的边.
- 进一步指出, 在 Frobenius 定理中, 最大最小特征值互为相反数的情况, 对应的图为二分图.

Theorem 6. For a connected graph, it is bipartite if and only if $\alpha_{1}=-\alpha_{n}$.

- 证明思路
    - 二分到特征值: 针对最大特征向量构造 $x(i)=\left\{\begin{array}{rr}\Phi_{1}(i) & \text { if } i \in L \\ -\Phi_{1}(i) & \text { if } i \in R\end{array}\right.$ , 可知该向量对应的二次型取得 $-\alpha_1$
    - 反过来: 构造一个向量x为 $x(i)=\left|\Phi_{n}(i)\right|$, 则以下不等式成立
        - $-\alpha_{n}=\left|\alpha_{n}\right|=\left|\Phi_{n}^{T} A \Phi_{n}\right|=\left|\sum_{(i, j) \in E} a_{i, j} \Phi_{n}(i) \Phi_{n}(j)\right| \leq x^{T} A x \leq \alpha_{1}$. 根据Frobenius定理, 不等式中的等号都需要成立.
        - 第一个不等式要求所有项同号. 观察到不能为正, 否则最小特征值为正而最大特征值为负了.
        - 要使得第二个不等式等号成立, 则要求累加中的所有项都非0 (见 Frobenius证明第二条).
        - 结合上面两点, 对于有边相连的两个节点, 有 $\Phi_{n}(i) \Phi_{n}(j) < 0$ , 因此可基于ij的符号划分为两类.

## Laplacian 矩阵

- [wiki](https://en.wikipedia.org/wiki/Laplacian_matrix)
- 定义: 度数矩阵减去邻接矩阵 $L = D-A$
- 重要特性
    - 二项式: $\boldsymbol{x}^{T} \boldsymbol{L}_{G} \boldsymbol{x}=\sum_{(a, b) \in E} w_{a, b}(\boldsymbol{x}(a)-\boldsymbol{x}(b))^{2}$ 因此, 可以衡量图上信号的平滑程度 (常数信号则值为零)
    - Incidence 矩阵: $L=B B^{\top}$. 这里 $B_{v e}=\left\{\begin{aligned} 1, & \text { if } v=v_{i} \\-1, & \text { if } v=v_{j} \\ 0, & \text { otherwise } \end{aligned}\right.$ 大小为 $|v| \times|e|$, 每一列实际上是 $\delta_i - \delta_j$ , 对应了 $(i,j)$ 边 (规定 i<j). 注意到, 这里体现了Laplacian是「可加的」, 可以用每一条边所表示的矩阵加起来得到.
- Laplacian 作为 continuous Laplacian 的近似
    - 展示了在一个离散的图上的热传导方程的推导, 证明其温度变化率正是 -L. 实际上, 在连续空间中对应的就是就是热传导方程, 这也是图上拉普拉斯矩阵的由来: 对应了连续空间中的拉普拉斯算子.
- 矩阵特征值与 联通性
    - Laplacian 的最小特征值为 0
    - 第二个特征值不为零, 当且仅当图是联通的;
    - 进一步, 有 Laplacian 有k个特征值为0, 等价于图有k个连通分量.
    - 实际上, (对于连通图) laplacian矩阵的第二个特征值可以衡量其「联通性」, 越大说明联通性越好 (代数联通性).
- 例子: 等效电阻 efficient resistance (参见书  11.7)
    - 对于一个电阻网络, 我们可以计算出 $i_{e x t}=\boldsymbol{L} \boldsymbol{v}$, 这里的i为每一个节点的流出电流大小, v为每个节点的电势. 也就是说, 可以通过电流大小计算出每个点的电势 $\boldsymbol{v}=\boldsymbol{L}^{+} \boldsymbol{i}_{e x t}$ . (注意到由于最小特征值为0, 因此方程有无数解, 这里用的是伪逆)
    - 例如, 我们令 a,b 两点之间有大小为1的电流 (假定的, 电流可表示为 $\boldsymbol{\delta}_{a}-\boldsymbol{\delta}$), 则可以计算出每个节点的电势 $\boldsymbol{v}=\boldsymbol{L}^{+}\left(\boldsymbol{\delta}_{a}-\boldsymbol{\delta}_{b}\right)$. 这样, 两点间的等效电阻为 $\mathrm{R}_{\mathrm{eff}}(a, b) \stackrel{\text { def }}{=}\left(\boldsymbol{\delta}_{a}-\boldsymbol{\delta}_{b}\right)^{T} \boldsymbol{L}^{+}\left(\boldsymbol{\delta}_{a}-\boldsymbol{\delta}_{b}\right)$.
    - 重要的启示: 等效电阻是电阻网络上, 两点之间连通性的有效衡量方式.

