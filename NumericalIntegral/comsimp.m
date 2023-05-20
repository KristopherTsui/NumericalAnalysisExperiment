function s = comsimp(func, a, b, n)
%COMSIMP - 复合 Simpson 公式数值求解函数 func 在区间 [a, b] 上的定积分.
%
% 语法: s = comsimp(func, a, b, n)
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
%   s - double. s 是积分的近似值.
%
% 示例:
% > comsimp(@log, 1, 2, 1)
% 错误! n 不小于 2!
% > comsimp(@cos, 0, 0, 4)
% 警告! 积分上下限相等!
% ans =
%   0
% > comsimp(@sin, 0, pi/2, 4)
% ans =
%   1.000134584974194
% > comsimp(@(x) exp(-x^2), 1, 0, 4)
% ans =
%   0.746855379790987
%
% 另见: simpson, adapsimp
%
%
    if n < 2
        error("错误! n 不小于 2!")
    end
    if a == b
        disp("警告! 积分上下限相等!")
        s = 0;
        return;
    elseif a > b
        c = a;
        a = b;
        b = c;
    end

    h = (b - a) / n;
    s0 = func(a) + func(b);
    s1 = 0;     % summation of f(x_{2k-1})
    s2 = 0;     % summation of f(x_{2k})
    for k = 1:n-1
        x = a + k * h;
        if rem(k , 2) == 0
            s2 = s2 + func(x);
        else
            s1 = s1 + func(x);
        end
    end
    s = h * (s0 + 4 * s1 + 2 * s2) / 3;
end
