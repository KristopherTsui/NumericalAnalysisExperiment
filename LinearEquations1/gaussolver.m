function x = gaussolver(A, b)
%GAUSSOLVER - Gauss 消去法求解线性方程组 Ax=b.
% Gauss 消去法只适用于消元过程中主元素非零的线性方程组, 否则消元过程无法进行.
% 当消元过程中主元素和 0 比较接近或者相对于其他元素较小时, 消元过程会产生较大的误差.
% 推荐使用列主元 Gauss 消去法 gausselimpiv.
%
% 语法: x = gaussolver(A, b)
%
% 输入:
%   A - 线性方程组 Ax=b 的系数矩阵. 系数矩阵 A 必须是方阵.
%       对于系数矩阵 A 不为方阵的情形, 可以考虑使用最小二乘法求线性方程组的最小二乘解.
%   b - 线性方程组 Ax=b 的常数向量. 常数项的个数必须与线性方程组中方程的个数相同.
%
% 输出:
%   x - 线性方程组 Ax=b 的解向量.
%
% 示例:
%
%
% 另见: gausselimpiv
%
%
    [nrow, ncol] = size(A);
    if nrow ~= ncol
        error("错误! 线性方程组的系数矩阵不为方阵!")
    end
    if nrow ~= length(b)
        error("错误! 线性方程组中方程的个数不等于常数项的个数!")
    end

    % Gauss 消元过程
    for irow = 1:nrow-1
        if A(irow, irow) == 0
            error("错误! 主元素不能为 0!")
        end
        for jrow = irow+1:nrow
            mul = A(jrow, irow) / A(irow, irow);
            b(jrow) = b(jrow) - mul * b(irow);
            for icol = irow:ncol
                A(jrow, icol) = A(jrow, icol) - mul * A(irow, icol);
            end
        end
    end
    % 回代过程, 解上三角形方程组
    b(nrow) = b(nrow) / A(nrow, ncol);
    for irow = nrow-1:-1:1
        s = 0;
        for icol = irow+1:ncol
            s = s + A(irow, icol) * b(icol);
        end
        b(irow) = (b(irow) - s) / A(irow, irow);
    end
    x = b(:);
end

