function x = bisect(func, a, b, tol, MAX_ITER)
%BISECT - 二分法求方程 func(x)=0 的近似根.
% 二分法对所有的方程都收敛, 但其是线性收敛的.
%
% 语法: x = bisect(func, a, b, tol, MAX_ITER)
%
% 输入:
%   func - 函数句柄或匿名函数. func 代表了方程 func(x)=0.
%   a - double, 二分法有根区间端点.
%   b - double, 二分法有根区间端点.
%       有根区间 [a,b] 是指端点处的函数值异号, 即 func(a)*func(b)<0.
%   tol - double. 二分法迭代精度, 默认值为 1e-9.
%   MAX_ITER - integer. 二分法最大迭代次数, 默认值为 1000.
%
% 输出:
%   x - double. x 是方程 func(x)=0 的近似根.
%
% 示例:
% > format long
% > bisect(@(x) exp(x)+x^2-4, -2.3, -1.6)
% ans =
%   -1.964635598007589
% > bisect(@(x) exp(x)+x^2-4, 1.5, 0.8, 1e-6)
% ans =
%   1.058006572723389
% > bisect(@sin, -1, 2, eps, 10)
% ans =
%   -0.000976562500000
%
% 另见:
%
%
    if nargin < 3
        error("错误! 输入不足! 可以使用 help bisect 命令查看相关文档!")
    end
    % 判断 [a,b] 是否为有根区间
    fa = feval(func, a);
    fb = feval(func, b);
    if fa * fb > 0
        error("错误! 区间 [a,b] 内可能不存在方程的根!")
    end
    % 处理输入
    if nargin < 4
        tol = 1e-9;
    end
    if nargin < 5
        MAX_ITER = 1000;
    end
    % 二分法迭代
    for n = 1:MAX_ITER
        c = (a + b) / 2;
        fc = feval(func, c);
        % 判断是否满足精度要求或者 func 在 c 处近似为 0.
        if abs((b-a)/2) < tol || abs(fc) < eps
            break;
        elseif fa * fc < 0
            % 新的有根区间为 [a, c]
            b = c;
            fb = fc;
        else
            % 新的有根区间为 [c, b]
            a = c;
            fa = fc;
        end
    end
    x = c;
end
