clear;
clc;

% 时间步长
tau = 0.01;
% 空间步长
h = 0.05;
% 网格比
r = tau / h^2;
% 网格节点数
M = 1 / h;
n = 1 / tau;
% 在区域 0 < t < 1, 0 < x < 1 上求解
x = 0:h:1;
t = 0:tau:1;

% 紧差分格式 BU^{k+1} = AU^k+F^k
% 构造系数矩阵 B
b0 = ones(1, M-1) * (5/6 + r);
b1 = ones(1, M-2) * (1/12 - r/2);
% 构造右端矩阵 A
a0 = ones(1, M-1) * (5/6 - r);
a1 = ones(1, M-2) * (1/12 + r/2);
A = diag(a0) + diag(a1, -1) + diag(a1, 1);

% 微分方程的近似解矩阵
U = zeros(M+1, n+1);
% 初值条件 u(x, 0) = exp(-x)
U(:, 1) = exp(-x');
% 边值条件
U(1, :) = exp(t);
U(M+1, :) = exp(-1+t);

% 追赶法逐层求解微分方程的近似解
% BU^{k+1} = AU^k+F^k
for k = 1:n
    F = zeros(M-1, 1);
    F(1) = (1/12+r/2)*U(1, k) - (1/12-r/2)*U(1, k+1);
    F(M-1) = (1/12+r/2)*U(M+1, k) - (1/12-r/2)*U(M+1, k+1);
    U(2:M, k+1) = tridiag(b1, b0, b1, A*U(2:M, k)+F)';
end
U = U';

% 绘制数值解图像
figure(1);
mesh(x, t, U)
title("扩散方程紧差分格式数值解")
xlabel("x")
ylabel("t")

% 绘制误差曲面
figure(2);
[X, T] = meshgrid(x, t);
Z = exp(-X + T);
err = abs(U - Z);
mesh(x, t, err)
title("紧差分格式数值解与解析解的误差曲面")
xlabel("x")
ylabel("t")

