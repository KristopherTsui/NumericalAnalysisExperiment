function x = newtraph(func, dfunc, x0, tol, MAX_ITER)
%NEWTRAPH - Newton-Raphson 法求解方程 func(x)=0 的近似根.
% Newton-Raphson 法是不动点迭代法的一种.
% Newton-Raphson 法对于单根的情况至少是平方收敛的, 而对有重根的情况仅有线性收敛.
% 当遇到重根时, 如果知道根的重数 m, 可以将迭代公式修改为
%                   x* = x - m * func(x)/dfunc(x)
% 如果不知道根的重数, 注意到如果 x* 是 func(x) 的 m 重根, 则 x* 是 dfunc(x) 的 m-1 重根.
% 考虑去重根, 即 x* 是 func(x)/dfunc(x) 的单根, 再对新的函数 func(x)/dfunc(x) 应用 Newton
% -Raphson 法即可达到平方收敛.
%
% 语法 - x = newtraph(func, dfunc, x0, tol, MAX_ITER)
%
% 输入:
%   func - 函数句柄或匿名函数. func 代表了方程 func(x)=0.
%   dfunc - 函数句柄或匿名函数. dfunc 是 func 的导函数.
%   x0 - double. Newton-Raphson 法选取的初始值.
%       初始值的选取会影响到 Newton-Raphson 法的收敛速度.
%   tol - double. Newton-Raphson 法迭代精度, 默认值为 1e-9.
%   MAX_ITER - integer. Newton-Raphson 法的最大迭代次数, 默认值为 1000.
%
% 输出:
%   x - double, 方程 func(x)=0 的近似根.
%
% 示例:
% > format long
% > f = @(x) x^3 - 5*x;
% > df = @(x) 3*x^2 - 5;
% > newtraph(f, df, 1.2)
% ans = 
%   -2.236067977499790
% > newtraph(f, df, -1.1, 1e-6)
% ans = 
%   2.236067977598409
%
% 另见:
%
%
    % 处理输入
    if nargin < 3
        error("错误! 输入不足! 可以通过 help newtraph 命令查看相关文档.")
    end
    if nargin < 4
        tol = 1e-9;
    end
    if nargin < 5
        MAX_ITER = 1000;
    end
    % Newton-Raphson 迭代法
    for n = 1:MAX_ITER
        x1 = x0 - feval(func, x0) / feval(dfunc, x0);
        % 计算绝对误差
        err = abs(x1-x0);
        x0 = x1;    % 更新迭代数列
        % 循环终止条件, 误差达到精度或者 func 在 x0 处近似为 0
        if err < tol || abs(feval(func, x0)) < eps
            break;
        end
    end
    x = x0;
end
