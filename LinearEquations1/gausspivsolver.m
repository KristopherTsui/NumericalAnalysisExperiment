function x = gausspivsolver(A, b)
%GAUSSPIVSOLVER - Gauss 列主元消去法求解线性方程组 Ax=b.
%
% 语法: x = gausspivsolver(A, b)
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
% 另见: gaussolver
%
%
    [nrow, ncol] = size(A);
    if nrow ~= ncol
        error("错误! 线性方程组的系数矩阵不为方阵!")
    end
    if nrow ~= length(b)
        error("错误! 线性方程组中方程的个数不等于常数项的个数!")
    end
    
    for irow = 1:nrow-1
        % 列主元的选取
        colvec = abs(A(irow:nrow, irow));
        [~, ind] = max(colvec);
        ind = ind + irow - 1;
        % 交换当前行与列主元所在行
        if ind ~= irow
            for icol = irow:ncol
                swap = A(irow, icol);
                A(irow, icol) = A(ind, icol);
                A(ind, icol) = swap;
            end
            swap = b(irow);
            b(irow) = b(ind);
            b(ind) = swap;
        end
        % 消元法
        for jrow = irow+1:nrow
            mult = A(jrow, irow) / A(irow, irow);
            b(jrow) = b(jrow) - mult * b(irow);
            for icol = irow:ncol
                A(jrow, icol) = A(jrow, icol) - mult * A(irow, icol);
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

