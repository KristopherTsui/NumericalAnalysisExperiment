function s = adapsimp(func, a, b, tol)
%ADAPSIMP - 自适应 Simpson 积分公式数值求解 func 在区间 [a, b] 上的定积分.
%
% 语法 - s = adapsimp(func, a, b, tol)
%
% 输入:
%   func - 被积函数. func 是一个函数句柄或者匿名函数.
%   a - double. a 默认为积分下限.
%   b - double. b 默认为积分上限.
%       如果 a = b, 抛出积分上下限相等的警告并赋 s = 0.
%       如果 a > b, 交换 a 和 b 的值保证 h = (b - a) / n > 0.
%   tol - double. tol 是积分近似值的精度. 默认值为 1e-9.
%
% 输出:
%   s - double. s 是积分的近似值.
%
% 示例:
% > adapsimp(@sin, 0, 0)
% 警告! 积分上下限相等!
% ans =
%   0
% > adapsimp(@(x) exp(-x^2), 1, 0)
% ans = 
%   0.746824132833815
% > adapsimp(@(x) exp(-x^2), 0, 1, 1e-6)
% ans = 
%   0.746824257435730
%
% 另见: simpson, comsimp
%
%
    if a == b
        disp("警告! 积分上下限相等!")
        s = 0;
        return;
    elseif a > b
        c = a;
        a = b;
        b = c;
    end
    if nargin == 3
        tol = 1e-9;
    end

    c = (a + b) / 2;
    s0 = (b - a) * (feval(func, a) + 4 * feval(func, c) + feval(func, b)) / 6;
    s1 = (c - a) * (feval(func, a) + 4 * feval(func, (a+c)/2) + feval(func, c)) / 6;
    s2 = (b - c) * (feval(func, c) + 4 * feval(func, (c+b)/2) + feval(func, b)) / 6;
    if abs(s1+s2-s0) < 15 * tol
        s = s1 + s2;
    else
        s1 = adapsimp(func, a, c, tol/2);
        s2 = adapsimp(func, c, b, tol/2);
        s = s1 + s2;
    end
end
