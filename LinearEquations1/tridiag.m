function [x] = tridiag(l, d, u, b)
%TRIDIAG - 追赶法求解三对角线性方程组.
% 对于严格对角占优的 n 维三对角矩阵 A, 一定可以作 Crout 分解然后分别求解两个三角型方程组.
% 对于非严格对角占优矩阵, 如果系数矩阵非奇异, 线性方程组也是有解的.
% 否则, 使用追赶法求解是不稳定的.
%
% 语法: x = tridiag(l, d, u, b)
%
% 输入:
%   l - 三对角矩阵 A 的次对角线向量, 维数为 n-1.
%   d - 三对角矩阵 A 的主对角线向量, 维数为 n.
%   u - 三对角矩阵 A 的上对角线向量, 维数为 n-1.
%   b - 线性方程组 Ax=b 右端常向量, 维数为 n.
%
% 输出:
%   x - 线性方程组 Ax=b 的解向量, 维数为 n.
%
% 示例:
% > a = [9, -2, 2, 4, -9]
% > b = [-10, -1, -11, 1, 2, 9]
% > c = [-2, -2, -11, -8, -1]
% > d = [-6, 13, 15, -2, -1, 9]
% > tridiag(a, b, c, d)
% ans =
%     1.0000   -2.0000   -1.0000    0.0000    0.0000    1.0000
%
    n = length(d);
    if n-1 ~= length(l) || n-1 ~= length(u)
        error("错误! 输入的三个向量无法构成三对角型矩阵!")
    end
    if n ~= length(b)
        error("错误! 线性方程组中方程的个数不等于常数项的个数!")
    end

    % 先求三对角矩阵的 Crout 分解
    u(1) = u(1) / d(1);
    for irow = 2:n-1
        d(irow) = d(irow) - l(irow-1) * u(irow-1);
        u(irow) = u(irow) / d(irow);
    end
    d(n) = d(n) - l(n-1) * u(n-1);

    % 追过程
    b(1) = b(1) / d(1);
    for irow = 2:n
        b(irow) = (b(irow) - l(irow-1) * b(irow-1)) / d(irow);
    end

    % 赶过程
    x(n) = b(n);
    for irow = n-1:-1:1
        x(irow) = b(irow) - u(irow) * x(irow+1);
    end
end
