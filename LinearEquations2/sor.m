function [x] = sor(A, b, omega, x0, tol)
%SOR - 松弛迭代法求解线性方程组 Ax=b.
% 当 0 < omega < 1 时称为低松弛迭代法; 当 omega > 1 时, 称为超松弛迭代法.
% 当 omega = 1 时, 就是 Gauss-Seidel 迭代法.
% SOR 迭代法收敛的必要条件是松弛因子 omega 满足 0 < omega < 2.
% 若方程组 Ax=b 的系数矩阵 A 是对称正定的, 则当 0 < omega < 2 时 SOR 迭代法收敛.
% 若方程组 Ax=b 的系数矩阵 A 是严格对角占优的, 则当 0 < omega <= 1 时 SOR 迭代法收敛.
%
% 输入:
%   A - 线性方程组 Ax=b 的系数矩阵. 系数矩阵 A 必须是方阵.
%       对于系数矩阵 A 不为方阵的情形, 可以考虑使用最小二乘法求线性方程组的最小二乘解.
%   b - 线性方程组 Ax=b 的常数向量. 常数项的个数必须与线性方程组中方程的个数相同.
%   omega - 超松弛因子, 影响 SOR 迭代法的收敛性.
%   x0 - 初始迭代向量, 影响迭代次数.
%   tol - double. 迭代精度, 默认值为 1e-9.
%
% 输出:
%   x - 线性方程组 Ax=b 的近似解向量.
%
% 另见: gausseidel.
%
    if nargin < 4
        error("错误! 输入不足! 可以使用 help sor 命令查看相关文档!")
    end
    if size(A, 1) ~= size(A, 2);
        error("错误! 线性方程组的系数矩阵不为方阵!")
    end
    if size(A, 1) ~= length(b)
        error("错误! 线性方程组中方程的个数不等于常数项的个数!")
    end
    if nargin < 5
        tol = 1e-9;
    end

    % 系数矩阵 A 分解 A = D - L - U
    D = diag(diag(A));
    L = -tril(A, -1);
    U = -triu(A, 1);
    % 构造迭代公式 x_{k+1} = Bx_k + f
    C = inv(D - omega * L);
    B = C * [(1 - omega) * D + omega * U];
    f = omega * C * b;
    
    % 迭代
    n = 1;  % 迭代次数
    x = B * x0 + f;
    while norm(x - x0) >= tol
        x0 = x;
        x = B * x0 + f;
        n = n + 1;
    end
end
