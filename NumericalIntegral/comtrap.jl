"""
    comtrap(func::Function, a::Real, b::Real, n::Integer)

Numerically approximate the integral of func from `a` to `b` using composite trapezoidal rule.

See also [`adapsimp`].

# Arguments

* `func::Function`: `func` is the integrand.
* `a::Real`: `a` is the lower limit of the integration by default.
* `b::Real`: `b` is the upper limit of the integration by default. 

If `a = b`, throw a Warning and return 0; if `a > b`, swap `a` and `b` to ensure `h = (b - a)/n > 0`.

* `n::Integer`: `n` is the number of intervals in equal parts and `n` is greater than or equal to 2.

# Outputs

* `t::Float64`: `t` is the approximation of integral.

# Examples

```julia-repl
julia> comtrap(cos, 0, 2, 1)
Error: n is greater than or equal 2!

julia> comtrap(sin, 0, 0, 4)
Warning: The limits of integration are equal!
0

julia> comsimp(log, 1, 2, 8)
0.3856439099520953
```
"""
function comtrap(func::Function, a::Real, b::Real, n::Integer)
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
    t0 = func(a) + func(b)
    t1 = 0;
    for k = 1:n-1
        x = a + k * h
        t1 = t1 + 2 * func(x)
    end
    t = h * (t0 + t1) / 2
    return t
end
