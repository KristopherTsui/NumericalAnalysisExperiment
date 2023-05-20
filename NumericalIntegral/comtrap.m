function t = comtrap(func, a, b, n)
%COMTRAP - 复合梯形公式数值求解函数 func 在区间 [a, b] 上的定积分.
%
% 语法: t = comtrap(func, a, b, n)
%
% 输入:
%   func - 被积函数. func 是一个函数句柄或者匿名函数.
%   a - double. a 默认为积分下限.
%   b - double. b 默认为积分上限.
%       如果 a = b, 抛出积分上下限相等的警告并赋 s = 0.
%       如果 a > b, 交换 a 和 b 的值保证 h = (b - a) / n > 0.
%   n - integer. n 是积分区间等分数. n 不小于 2.
%
% 输出:
%   t - double. t 是积分的近似值.
%
% 示例:
% > comsimp(@cos, 0, 2, 1)
% 错误! n 不小于 2!
% > comsimp(@sin, 0, 0, 4)
% 警告! 积分上下限相等!
% ans =
%   0
% > comsimp(@log, 1, 2, 8)
% ans =
%   0.385643909952095
%
% 另见: comsimp
%
%
    if n < 2
        error("错误! n 不小于 2!")
    end
    if a == b
        disp("警告! 积分上下限相等!")
        t = 0;
        return;
    elseif a > b
        c = a;
        a = b;
        b = c;
    end

    h = (b - a) / n;
    t0 = feval(func, a) + feval(func, b);
    t1 = 0;
    for k = 1:n-1
        x = a + k * h;
        t1 = t1 + 2 * feval(func, x);
    end
    t = h * (t0 + t1) / 2;
end
