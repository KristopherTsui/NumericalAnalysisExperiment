function s = simpson(func, a, b)
%SIMPSON - Simpson 公式数值近似求解函数 func 在区间 [a,b] 上的定积分.
%
% 语法: s = simpson(func, a, b)
%
% 输入:
%   func - 被积函数. func 是一个函数句柄或者匿名函数.
%   a - double. a 默认为积分下限.
%   b - double. b 默认为积分上限.
%       如果 a = b, 抛出积分上下限相等的警告并赋 s = 0.
%       如果 a > b, 交换 a 和 b 的值保证 h = (b - a) / 2 > 0.
%
% 输出:
%   s - double. s 是积分的近似值.
%
% 示例:
% > simpson(@cos, 0, 0)
% 警告! 积分上下限相等!
% ans =
%   0
% > simpson(@sin, 0, pi/2)
% ans =
%   1.002279877492210
% > simpson(@(x) exp(-x^2), 1, 0)
% ans =
%   0.747180428909510
%
% 另见: comsimp, adapsimp
%
%
    if a == b
        disp("警告! 积分上下限相等!");
        s = 0;
        return;
    elseif a > b
        c = a;
        a = b;
        b = c;
    end
    h = (b - a) / 2;
    s = h * (func(a) + 4 * func(a + h) + func(b)) / 3;
end
