"""
    comsimp(func::Function, a::Real, b::Real, n::Integer)

Numerically approximate the integral of func from `a` to `b` using Simpson's composite rule.

See also [`simpson`], [`adapsimp`].

# Arguments

* `func::Function`: `func` is the integrand.
* `a::Real`: `a` is the lower limit of the integration by default.
* `b::Real`: `b` is the upper limit of the integration by default. 

If `a = b`, throw a Warning and return 0; if `a > b`, swap `a` and `b` to ensure `h = (b - a)/n > 0`.

* `n::Integer`: `n` is the number of intervals in equal parts and `n` is greater than or equal to 2.

# Outputs

* `s::Float64`: `s` is the approximation of integral.

# Examples

```julia-repl
julia> comsimp(log, 1, 2, 1)
Error! The Simpson's composite rule requires the interval to be divided into at
least two parts.

julia> comsimp(cos, 0, 0, 4)
Warning! The limits of integration are equal!
0

julia> comsimp(sin, 0, pi/2, 4)
1.0001345849741938

julia> comsimp(x->exp(-x^2), 1, 0, 4)
0.7468553797909873
```
"""
function comsimp(func::Function, a::Real, b::Real, n::Integer)
    if n < 2
        @error "n is greater than or equal to 2!"
        return
    end
    if a == b
        @warn "The limits of integration are equal!"
        return 0
    elseif a > b
        a, b = b, a
    end

    h = (b - a) / n
    s0 = func(a) + func(b)
    s1 = 0      # summation of f(x_{2k-1})
    s2 = 0      # summation of f(x_{2k})
    for k = 1:n-1
        x = a + k * h
        if rem(k, 2) == 0
            s2 = s2 + func(x)
        else
            s1 = s1 + func(x)
        end
    end
    s = h * (s0 + 4 * s1 + 2 * s2) / 3
    return s
end
