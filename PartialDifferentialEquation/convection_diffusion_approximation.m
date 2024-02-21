clear;
clc;

% 对流系数
a = 1;
% 扩散系数
nu = 0.001;

% 时间步长
tau = 0.005;
% 空间步长
h = 0.02;
% 判断稳定性条件
lambda = a * tau / h;
mu = nu * tau / h^2;
if (lambda + 2 * mu) >= 1
    warning("警告! 当前选取的时间步长和空间步长不满足稳定性条件!")
end

% 在区域 0 < t < 1, 0 < x < 1 上求解
x = 0:h:1;
t = 0:tau:1;
% 网格节点数
M = 1 / h;
n = 1 / tau;

% 迎风差分格式 U^{k+1}=BU^k+F^k
% 构造迭代矩阵 B
b0 = ones(1, M-1) * (1 - lambda - 2 * mu);
b1 = ones(1, M-2) * mu;
b2 = ones(1, M-2) * (lambda + mu);
B = diag(b0) + diag(b1, 1) + diag(b2, -1);

% 微分方程的近似解矩阵
U = zeros(M+1, n+1);
% 初值条件 u(x, 0) = exp(x)
U(:, 1) = exp(x');
% 边值条件
U(1, :) = exp(-0.999*t);
U(M+1, :) = exp(1-0.999*t);
% 迭代逐层求解对流扩散方程的近似解
for k = 1:n
    F = zeros(M-1, 1);
    F(1) = (lambda + mu) * U(1, k);
    F(M-1) = mu * U(M+1, k);
    U(2:M, k+1) = B * U(2:M, k) + F;
end
U = U';

% 绘制数值解图像
figure(1);
mesh(x, t, U)
title("对流扩散方程迎风差分格式数值解")
xlabel("x")
ylabel("t")

% 绘制误差曲面
figure(2);
[X, T] = meshgrid(x, t);
Z = exp(X-0.999*T);
err = abs(U - Z);
mesh(x, t, err)
title("迎风差分格式数值解与解析解的误差曲面")
xlabel("x")
ylabel("t")

