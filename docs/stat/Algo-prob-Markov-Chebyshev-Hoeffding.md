



## 三个重要的概率不等式

- Markov’s inequality
    - If $X$ is a nonnegative random variable, then for all $t>0$,
    $$
    \mathbb{P}[X \geq t] \leq \frac{\mathbb{E}[X]}{t}
    $$
    - 对于一个取值为正的随机变量, 其取值大于数字t的概率有上界, 即其期望与t的比值.
    - 直观理解: 随机变量取值的分布收到其期望的约束. 例如, 假如取t为两倍期望, 可知该随机变量比t大的概率至多为二分之一.
    - 证明思路: 定义一个随机变量 $I= \begin{cases}1 & \text { if } X \geq t \\ 0 & \text { if } X<t\end{cases}$ . 可知其期望为 $X \ge t$ 的概率. 利用 $t I \leq X$ 的关系, 两边去期望即可
- Chebyshev’s inequality
    - For all $t>0$,
    $$
    \mathbb{P}[|X-\mathbb{E}[X]| \geq t] \leq \frac{\operatorname{Var}[X]}{t^{2}}
    $$
    - 理解: 一个随机变量记录其期望较远的概率受到其方差的约束.
    - 证明思路: 利用平方函数的非负部分递增的性质, 可知 $\mathbb{P}[|X-\mathbb{E}[X]| \geq t]=\mathbb{P}\left[(X-\mathbb{E}[X])^{2} \geq t^{2}\right]$, 然后利用 Markov 即可.
- Chernoff-Hoeffding
    - Lemma 3. Let $X_{1}, X_{2}, \cdots, X_{n}$ be $n$ independent random variables, such that $a_{i} \leq X_{i} \leq b_{i}$ for all $i$, and let $X=\sum_{i=1}^{n} X_{i}$, then
    $$
    \mathbb{P}[|X-\mathbb{E}[X]| \geq t] \leq 2 \cdot e^{-\frac{2 t^{2}}{\sum_{i=1}^{n}\left(b_{i}-a_{i}\right)^{2}}}
    $$
    - 理解: 相较于 Chebyshev, 这里考虑的是随机变量之和的分布界限.
    - 注意: 当t较大的时候, 该不等式相较于 Chebyshev 提供了更好的下界. 以n个独立的等概率0-1 bernoulli分布之和为例, 可知其期望和方差分别为 $\frac{n}{2}$ 和 $\frac{n}{4}$. 分别代入可得到下界. 观察, 可知当t为 $\Theta(\sqrt{n})$ 级别时两下界差别不大; 然而若t为 $\Theta({n})$ 级别, 则两者分别提供了 $\Theta(1/n)$, $\Theta(\exp{-n})$ 级别的下界.



## Morris’s algorithm

定义 Morris 算法:

1. initialize: $s \leftarrow 0$
2. update: if the bit is 1 , increment $s$ with probability $1 / 2^{s}$
3. estimate: output $\tilde{m}=2^{s}-1$

说明

- 问题的定义比较简单: 对于一个bit流, 统计其中1出现的个数. 相较于全部记录所花的空间复杂度为 $O(\log(m))$,  这里的空间复杂度为 $O(\log(s))$. 可以证明, 其为 $O(\log \log m)$ with high probability.
- 算法的直觉: 我们仅记录计数m中的 1,2,4,8... 这些事件. 那略过的这些事件怎么进行记录? 通过随机变量来使得在期望上是比较接近的.

### Correctness 证明

- Expectation of $\tilde{m}$

Claim 4. $\mathbb{E}[\tilde{m}]=\mathbb{E}\left[2^{s}-1\right]=m$.
Proof. It is sufficient to show $\mathbb{E}\left[2^{s}\right]=m+1$. Let $s_{t}$ denote the value of $s$ after $t$ 1's have arrived and before the $(t+1)$-th 1 arrives. We next show that $\mathbb{E}\left[2^{s_{t}}\right]=t+1$.
$$
\begin{aligned}
\mathbb{E}\left[2^{s_{t}}\right] &=\sum_{i=1}^{\infty} \mathbb{E}\left[2^{s_{t}} \mid s_{t-1}=i\right] \cdot \mathbb{P}\left[s_{t-1}=i\right] \\
&=\sum_{i=1}^{\infty}\left(2^{i+1} \cdot \frac{1}{2^{i}}+2^{i} \cdot\left(1-\frac{1}{2^{i}}\right)\right) \cdot \mathbb{P}\left[s_{t-1}=i\right] \\
&=\sum_{i=1}^{\infty}\left(2^{i}+1\right) \cdot \mathbb{P}\left[s_{t-1}=i\right] \\
&=\sum_{i=1}^{\infty} 2^{i} \cdot \mathbb{P}\left[s_{t-1}=i\right]+\sum_{i=1}^{\infty} \mathbb{P}\left[s_{t-1}=i\right] \\
&=\mathbb{E}\left[2^{s_{t-1}}\right]+1 .
\end{aligned}
$$
Since $\mathbb{E}\left[2^{s_{0}}\right]=1$, we have $\mathbb{E}\left[2^{s_{t}}\right]=t+1$ by the above equation.

- Variance of $\tilde{m}$

Claim 5. $\operatorname{Var}\left[2^{s}\right]=\frac{m^{2}}{2}-\frac{m}{2} \leq \frac{m^{2}}{2}$
Proof. Next we analyze the variance of $2^{s_{t}}$. By definition $\operatorname{Var}\left[2^{s_{t}}\right]=\mathbb{E}\left[2^{2 s_{t}}\right]-\mathbb{E}\left[2^{s_{t}}\right]^{2}$. The value of $\mathbb{E}\left[2^{s_{t}}\right]$ has already been calculated above, and thus we only need to calculate $\mathbb{E}\left[2^{2 s_{t}}\right]$.
$$
\begin{aligned}
\mathbb{E}\left[2^{2 s_{t}}\right] &=\sum_{i=1}^{\infty} \mathbb{E}\left[2^{2 s_{t}} \mid s_{t-1}=i\right] \cdot \mathbb{P}\left[s_{t-1}=i\right] \\
&=\sum_{i=1}^{\infty}\left(2^{2 i+2} \cdot \frac{1}{2^{i}}+2^{2 i} \cdot\left(1-\frac{1}{2^{i}}\right)\right) \cdot \mathbb{P}\left[s_{t-1}=i\right] \\
&\left.=\sum_{i=1}^{\infty}\left(2^{i+2}+2^{2 i}-2^{i}\right) \cdot \mathbb{P}\left[s_{t-1}=i\right]\right) \\
&=3 \cdot \sum_{i=1}^{\infty} 2^{i} \cdot \mathbb{P}\left[s_{t-1}=i\right]+\sum_{i=1}^{\infty} 2^{2 i} \cdot \mathbb{P}\left[s_{t-1}=i\right] \\
&=3 \cdot \mathbb{E}\left[2^{s_{t-1}}\right]+\mathbb{E}\left[2^{2 s_{t-1}}\right] \\
&=\mathbb{E}\left[2^{2 s_{t-1}}\right]+3 t
\end{aligned}
$$
Since $2^{2 s_{0}}=1$, we have
$$
\mathbb{E}\left[2^{2 s_{t}}\right]=1+3+2 \cdot 3+\cdots+3 t=1+3 \cdot \frac{t(t+1)}{2}=\frac{3}{2} t^{2}+\frac{3}{2} t+1 .
$$
Hence, $\operatorname{Var}\left[2^{s_{t}}\right]=\frac{3}{2} t^{2}+\frac{3}{2} t+1-(t+1)^{2}=\frac{t^{2}}{2}-\frac{t}{2} \leq \frac{t^{2}}{2}$



### Morris+: 多次取平均

直接采用上述策略得到的结果误差很大 (主要是因为方差较大). 利用 Chebyshev 不等式, 有
$$
\mathbb{P}[|\tilde{m}-m| \geq \varepsilon m] \leq \frac{m^{2} / 2}{\varepsilon^{2} m^{2}}=\frac{1}{2 \varepsilon^{2}}
$$

- 显然没啥用. 因此, 可以多次重复取平均.
- 具体而言, 我们希望 $\mathbb{P}[|\tilde{m}-m| \geq \varepsilon m] \leq \delta \text { for some small } \delta<1$.
- 因此, 我们可以取重复次数 $\ell=\frac{1}{\varepsilon^{2} \delta}$.
- 这样, 算法的时间复杂度为 $O\left(\frac{1}{\varepsilon^{2} \delta} \log \log m\right)$.
- 称该算法为 Morris+$(\varepsilon, \delta)$. 这里的 $\epsilon$ 表示的是相对误差, 而 $\delta$ 表示错误率 (相对误差误差超过了界限).



### The median trick 进一步优化

- 所谓 median trick, 就是运行一系列不太好的  Morris+$(\varepsilon, \delta)$ 算法 (错误率 $\delta$ 较大, 例如为 1/3); 然后取这些结果的中位数.
    - 这里的intuition在于, 通过运行一系列虽然不太靠谱的算法 (期望是正确的, 但是方差较大), 总有一些可以得到正确解 (在误差范围内).
    - 通过取中位数而非均值, 将每次运行 Morris+ 算法的结果是否正确看成是独立的事件. 从而可以采用更紧的 Hoffding 下界.
- 从结果来看, 将算法的时间复杂度从  $O\left(\frac{1}{\varepsilon^{2} \delta} \log \log m\right)$ 下降为 $O\left(\frac{1}{\varepsilon^{2}} \log \log m \log \frac{1}{\delta}\right)$. 注意到这里优化的对象的错误率, 引入了一个对数项, 而优化的原因在于, Hoffding 不等式中的指数项.

**The median trick**: The dependence on $\delta$ can be further improved by the Median Trick, which works as follows. We run $h$ (to be determined later) independent copies of Morris $+(\varepsilon, 1 / 3)$, and let $\tilde{m}_{1}, \cdots, \tilde{m}_{h}$ be their outputs; the final output $\tilde{m}=\operatorname{Median}\left\{\tilde{m}_{1}, \cdots, \tilde{m}_{h}\right\}$. Note that the total space is $O\left(\frac{h}{\varepsilon^{2}} \log \log m\right)$. How large $h$ should be?

By the guarantee of Morris $+(\varepsilon, 1 / 3)$, we have $\mathbb{P}\left[\left|m-\tilde{m}_{i}\right| \geq \varepsilon m\right] \leq 1 / 3$ for all $i \in[1, h]$. For each $i \in[1, h]$, define
$$
I_{i}= \begin{cases}1 & \text { If }\left|m-\tilde{m}_{i}\right| \geq \varepsilon m \\ 0 & \text { Otherwise }\end{cases}
$$
Let $I=\sum_{i=1}^{h} I_{i}$, which is the total number Morris $+(\varepsilon, 1 / 3)$ which are "wrong". Since $\mathbb{E}\left[I_{i}\right] \leq 1 / 3$,
$$
\mathbb{E}[I] \leq h / 3
$$
By Chernoff-Hoeffding,
$$
\mathbb{P}[|I-\mathbb{E}[I]| \geq h / 6] \leq 2 \cdot e^{-\frac{h^{2} / 18}{h}}=2 \cdot e^{-h / 18}
$$
By setting $h=O\left(\log \frac{1}{\delta}\right)$, the above probability is smaller than $\delta$.
Let $\mathcal{A}$ denote the event $|I-\mathbb{E}[I]|<h / 6$. Conditioned on $\mathcal{A}$, we have
$$
I<h / 6+\mathbb{E}[I] \leq h / 6+h / 3=h / 2
$$
This means that for at least half of $h$ copies of Morris+ are correct. Consequently, the median of them must be correct, i.e., $|\tilde{m}-m| \leq \varepsilon m$ (why?). This occurs whenever $\mathcal{A}$ happens, the probability of which is at least $1-\delta$ for $h=O\left(\log \frac{1}{\delta}\right)$. The total space is thus $O\left(\frac{1}{\varepsilon^{2}} \log \log m \log \frac{1}{\delta}\right)$.
