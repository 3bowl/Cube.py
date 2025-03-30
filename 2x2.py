import os, random, sys
from platform import system

# if Windows, clear = 'cls'; else, clear = 'clear'
if system() == 'Windows':
    clear = 'cls'
else:
    clear = 'clear'

os.system(clear)

def main():
    solved = '-Solved-'
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x
    a = '\033[0m#'
    b = '\033[0m#'
    c = '\033[0m#'
    d = '\033[0m#'
    # https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
    e = '\033[38;5;202m#'
    f = '\033[38;5;202m#'
    g = '\033[38;5;202m#'
    h = '\033[38;5;202m#'
    i = '\033[38;5;46m#'
    j = '\033[38;5;46m#'
    k = '\033[38;5;46m#'
    l = '\033[38;5;46m#'
    m = '\033[38;5;196m#'
    n = '\033[38;5;196m#'
    o = '\033[38;5;196m#'
    p = '\033[38;5;196m#'
    q = '\033[38;5;21m#'
    r = '\033[38;5;21m#'
    s = '\033[38;5;21m#'
    t = '\033[38;5;21m#'
    u = '\033[38;5;226m#'
    v = '\033[38;5;226m#'
    w = '\033[38;5;226m#'
    x = '\033[38;5;226m#'
    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]
    all_moves = ['U', 'U\'', 'U2', 'R', 'R\'', 'R2', 'F', 'F\'', 'F2', 'L', 'L\'', 'L2', 'B', 'B\'', 'B2', 'D', 'D\'', 'D2']
    rotations = ['x', 'x\'', 'x2', 'y', 'y\'', 'y2', 'z', 'z\'', 'z2']
    movecount = 0
    print_cube(u_, l_, f_, r_, b_, d_, solved, movecount)
    while True:
        print('\033[0mType "scramble" to scramble the cube - Type "solve" to solve the cube instantly - Type "exit" to exit program')
        try:
            move = input().strip().upper().split(' ')
        except EOFError:
            sys.exit('-EXIT-')
            
        for dir in move:
            movecount += 1
            if dir.lower() in rotations:
                movecount -= 1

            if dir == 'U':
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'U\'':
                u_, l_, f_, r_, b_, d_ = u_prime(u_, l_, f_, r_, b_, d_)
            elif dir == 'U2':
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'R':
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'R\'':
                u_, l_, f_, r_, b_, d_ = r_prime(u_, l_, f_, r_, b_, d_)
            elif dir == 'R2':
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'F':
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'F\'':
                u_, l_, f_, r_, b_, d_ = f_prime(u_, l_, f_, r_, b_, d_)
            elif dir == 'F2':
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'L':
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'L\'':
                u_, l_, f_, r_, b_, d_ = l_prime(u_, l_, f_, r_, b_, d_)
            elif dir == 'L2':
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'B':
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'B\'':
                u_, l_, f_, r_, b_, d_ = b_prime(u_, l_, f_, r_, b_, d_)
            elif dir == 'B2':
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'D':
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'D\'':
                u_, l_, f_, r_, b_, d_ = d_prime(u_, l_, f_, r_, b_, d_)
            elif dir == 'D2':
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'x':
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_prime(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'x\'':
                u_, l_, f_, r_, b_, d_ = r_prime(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'x2':
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_prime(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_prime(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'y':
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_prime(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'y\'':
                u_, l_, f_, r_, b_, d_ = u_prime(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'y2':
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_prime(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_prime(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'z':
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_prime(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'z\'':
                u_, l_, f_, r_, b_, d_ = f_prime(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'z2':
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_prime(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_prime(u_, l_, f_, r_, b_, d_)
            elif dir == 'EXIT':
                sys.exit('-EXIT-')
            elif dir == 'SCRAMBLE':
                movecount = 0
                u_, l_, f_, r_, b_, d_ = scramble(u_, l_, f_, r_, b_, d_, all_moves)
            elif dir == 'SOLVE':
                movecount = 0
                u_, l_, f_, r_, b_, d_ = solve_cube(u_, l_, f_, r_, b_, d_)
            else:
                movecount -= 1
                continue

        # displays '-Solved-' when solved
        cube_solved = check_solved(u_, l_, f_, r_, b_, d_)
        if cube_solved:
            solved = '-Solved-'
        else:
            solved = '        '

        print_cube(u_, l_, f_, r_, b_, d_, solved, movecount)


def u_move(u_, l_, f_, r_, b_, d_):
    # U
    a = u_[3]
    b = u_[0]
    c = u_[1]
    d = u_[2]
    # L
    e = f_[0]
    f = f_[1]
    g = l_[2]
    h = l_[3]
    # F
    i = r_[0]
    j = r_[1]
    k = f_[2]
    l = f_[3]
    # R
    m = b_[0]
    n = b_[1]
    o = r_[2]
    p = r_[3]
    # B
    q = l_[0]
    r = l_[1]
    s = b_[2]
    t = b_[3]
    # D
    u = d_[0]
    v = d_[1]
    w = d_[2]
    x = d_[3]
    # Updates the list of each side
    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]
    # Returns updated lists
    return u_, l_, f_, r_, b_, d_


def u_prime(u_, l_, f_, r_, b_, d_):
    # U
    a = u_[1]
    b = u_[2]
    c = u_[3]
    d = u_[0]
    # L
    e = b_[0]
    f = b_[1]
    g = l_[2]
    h = l_[3]
    # F
    i = l_[0]
    j = l_[1]
    k = f_[2]
    l = f_[3]
    # R
    m = f_[0]
    n = f_[1]
    o = r_[2]
    p = r_[3]
    # B
    q = r_[0]
    r = r_[1]
    s = b_[2]
    t = b_[3]
    # D
    u = d_[0]
    v = d_[1]
    w = d_[2]
    x = d_[3]
    # Updates the list of each side
    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]
    # Returns updated lists
    return u_, l_, f_, r_, b_, d_


def r_move(u_, l_, f_, r_, b_, d_):
    a = u_[0]
    b = f_[1]
    c = f_[2]
    d = u_[3]

    e = l_[0]
    f = l_[1]
    g = l_[2]
    h = l_[3]

    i = f_[0]
    j = d_[1]
    k = d_[2]
    l = f_[3]

    m = r_[3]
    n = r_[0]
    o = r_[1]
    p = r_[2]

    q = u_[2]
    r = b_[1]
    s = b_[2]
    t = u_[1]

    u = d_[0]
    v = b_[3]
    w = b_[0]
    x = d_[3]

    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]

    return u_, l_, f_, r_, b_, d_


def r_prime(u_, l_, f_, r_, b_, d_):
    a = u_[0]
    b = b_[3]
    c = b_[0]
    d = u_[3]

    e = l_[0]
    f = l_[1]
    g = l_[2]
    h = l_[3]

    i = f_[0]
    j = u_[1]
    k = u_[2]
    l = f_[3]

    m = r_[1]
    n = r_[2]
    o = r_[3]
    p = r_[0]

    q = d_[2]
    r = b_[1]
    s = b_[2]
    t = d_[1]

    u = d_[0]
    v = f_[1]
    w = f_[2]
    x = d_[3]

    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]

    return u_, l_, f_, r_, b_, d_


def f_move(u_, l_, f_, r_, b_, d_):
    a = u_[0]
    b = u_[1]
    c = l_[1]
    d = l_[2]

    e = l_[0]
    f = d_[0]
    g = d_[1]
    h = l_[3]

    i = f_[3]
    j = f_[0]
    k = f_[1]
    l = f_[2]

    m = u_[3]
    n = r_[1]
    o = r_[2]
    p = u_[2]

    q = b_[0]
    r = b_[1]
    s = b_[2]
    t = b_[3]

    u = r_[3]
    v = r_[0]
    w = d_[2]
    x = d_[3]

    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]

    return u_, l_, f_, r_, b_, d_


def f_prime(u_, l_, f_, r_, b_, d_):
    a = u_[0]
    b = u_[1]
    c = r_[3]
    d = r_[0]

    e = l_[0]
    f = u_[2]
    g = u_[3]
    h = l_[3]

    i = f_[1]
    j = f_[2]
    k = f_[3]
    l = f_[0]

    m = d_[1]
    n = r_[1]
    o = r_[2]
    p = d_[0]

    q = b_[0]
    r = b_[1]
    s = b_[2]
    t = b_[3]

    u = l_[1]
    v = l_[2]
    w = d_[2]
    x = d_[3]

    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]

    return u_, l_, f_, r_, b_, d_


def l_move(u_, l_, f_, r_, b_, d_):
    a = b_[2]
    b = u_[1]
    c = u_[2]
    d = b_[1]

    e = l_[3]
    f = l_[0]
    g = l_[1]
    h = l_[2]

    i = u_[0]
    j = f_[1]
    k = f_[2]
    l = u_[3]

    m = r_[0]
    n = r_[1]
    o = r_[2]
    p = r_[3]

    q = b_[0]
    r = d_[3]
    s = d_[0]
    t = b_[3]

    u = f_[0]
    v = d_[1]
    w = d_[2]
    x = f_[3]

    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]

    return u_, l_, f_, r_, b_, d_


def l_prime(u_, l_, f_, r_, b_, d_):
    a = f_[0]
    b = u_[1]
    c = u_[2]
    d = f_[3]

    e = l_[1]
    f = l_[2]
    g = l_[3]
    h = l_[0]

    i = d_[0]
    j = f_[1]
    k = f_[2]
    l = d_[3]

    m = r_[0]
    n = r_[1]
    o = r_[2]
    p = r_[3]

    q = b_[0]
    r = u_[3]
    s = u_[0]
    t = b_[3]

    u = b_[2]
    v = d_[1]
    w = d_[2]
    x = b_[1]

    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]

    return u_, l_, f_, r_, b_, d_


def b_move(u_, l_, f_, r_, b_, d_):
    a = r_[1]
    b = r_[2]
    c = u_[2]
    d = u_[3]

    e = u_[1]
    f = l_[1]
    g = l_[2]
    h = u_[0]

    i = f_[0]
    j = f_[1]
    k = f_[2]
    l = f_[3]

    m = r_[0]
    n = d_[2]
    o = d_[3]
    p = r_[3]

    q = b_[3]
    r = b_[0]
    s = b_[1]
    t = b_[2]

    u = d_[0]
    v = d_[1]
    w = l_[3]
    x = l_[0]

    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]

    return u_, l_, f_, r_, b_, d_


def b_prime(u_, l_, f_, r_, b_, d_):
    a = l_[3]
    b = l_[0]
    c = u_[2]
    d = u_[3]

    e = d_[3]
    f = l_[1]
    g = l_[2]
    h = d_[2]

    i = f_[0]
    j = f_[1]
    k = f_[2]
    l = f_[3]

    m = r_[0]
    n = u_[0]
    o = u_[1]
    p = r_[3]

    q = b_[1]
    r = b_[2]
    s = b_[3]
    t = b_[0]

    u = d_[0]
    v = d_[1]
    w = r_[1]
    x = r_[2]

    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]

    return u_, l_, f_, r_, b_, d_


def d_move(u_, l_, f_, r_, b_, d_):
    a = u_[0]
    b = u_[1]
    c = u_[2]
    d = u_[3]

    e = l_[0]
    f = l_[1]
    g = b_[2]
    h = b_[3]

    i = f_[0]
    j = f_[1]
    k = l_[2]
    l = l_[3]

    m = r_[0]
    n = r_[1]
    o = f_[2]
    p = f_[3]

    q = b_[0]
    r = b_[1]
    s = r_[2]
    t = r_[3]

    u = d_[3]
    v = d_[0]
    w = d_[1]
    x = d_[2]

    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]

    return u_, l_, f_, r_, b_, d_


def d_prime(u_, l_, f_, r_, b_, d_):
    a = u_[0]
    b = u_[1]
    c = u_[2]
    d = u_[3]

    e = l_[0]
    f = l_[1]
    g = f_[2]
    h = f_[3]

    i = f_[0]
    j = f_[1]
    k = r_[2]
    l = r_[3]

    m = r_[0]
    n = r_[1]
    o = b_[2]
    p = b_[3]

    q = b_[0]
    r = b_[1]
    s = l_[2]
    t = l_[3]

    u = d_[1]
    v = d_[2]
    w = d_[3]
    x = d_[0]

    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]

    return u_, l_, f_, r_, b_, d_


def scramble(u_, l_, f_, r_, b_, d_, moves):
    # 11 is God's Number for 2x2 (HTM)
    turn_log = []
    iteration = 0
    while True:
        dir = random.choice(moves)
        turn_log.append(dir)
        
        if iteration > 0:
            if dir[0] != prev_dir[0]:
                iteration += 1
            else:
                turn_log.pop(iteration)
                continue
        else:
            iteration += 1

        prev_dir = turn_log[iteration - 1]

        if dir == 'U':
            u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'U\'':
            u_, l_, f_, r_, b_, d_ = u_prime(u_, l_, f_, r_, b_, d_)
        elif dir == 'U2':
            u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'R':
            u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'R\'':
            u_, l_, f_, r_, b_, d_ = r_prime(u_, l_, f_, r_, b_, d_)
        elif dir == 'R2':
            u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'F':
            u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'F\'':
            u_, l_, f_, r_, b_, d_ = f_prime(u_, l_, f_, r_, b_, d_)
        elif dir == 'F2':
            u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'L':
            u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'L\'':
            u_, l_, f_, r_, b_, d_ = l_prime(u_, l_, f_, r_, b_, d_)
        elif dir == 'L2':
            u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'B':
            u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'B\'':
            u_, l_, f_, r_, b_, d_ = b_prime(u_, l_, f_, r_, b_, d_)
        elif dir == 'B2':
            u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'D':
            u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'D\'':
            u_, l_, f_, r_, b_, d_ = d_prime(u_, l_, f_, r_, b_, d_)
        elif dir == 'D2':
            u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)

        if iteration >= 11:
            break

    return u_, l_, f_, r_, b_, d_


def check_solved(u_, l_, f_, r_, b_, d_):
    if (u_ == [a, b, c, d] or u_ == [e, f, g, h] or u_ == [i, j, k, l] or u_ == [m, n, o, p] or u_ == [q, r, s, t] or u_ == [u, v, w, x]) and (l_ == [a, b, c, d] or l_ == [e, f, g, h] or l_ == [i, j, k, l] or l_ == [m, n, o, p] or l_ == [q, r, s, t] or l_ == [u, v, w, x]) and (f_ == [a, b, c, d] or f_ == [e, f, g, h] or f_ == [i, j, k, l] or f_ == [m, n, o, p] or f_ == [q, r, s, t] or f_ == [u, v, w, x]) and (r_ == [a, b, c, d] or r_ == [e, f, g, h] or r_ == [i, j, k, l] or r_ == [m, n, o, p] or r_ == [q, r, s, t] or r_ == [u, v, w, x]) and (b_ == [a, b, c, d] or b_ == [e, f, g, h] or b_ == [i, j, k, l] or b_ == [m, n, o, p] or b_ == [q, r, s, t] or b_ == [u, v, w, x]) and (d_ == [a, b, c, d] or d_ == [e, f, g, h] or d_ == [i, j, k, l] or d_ == [m, n, o, p] or d_ == [q, r, s, t] or d_ == [u, v, w, x]):
        return True
    else:
        return False
    

def solve_cube(u_, l_, f_, r_, b_, d_):
    u_ = [a, b, c, d]
    l_ = [e, f, g, h]
    f_ = [i, j, k, l]
    r_ = [m, n, o, p]
    b_ = [q, r, s, t]
    d_ = [u, v, w, x]
    return u_, l_, f_, r_, b_, d_


def print_cube(u_, l_, f_, r_, b_, d_, solved, movecount):
    os.system(clear)
    print(f'''\033[0m- Cube.py -
          
    {u_[0]} {u_[1]}\033[0m         {solved}          U U          Movecount: {movecount}
    {u_[3]} {u_[2]}\033[0m                           U U
{l_[0]} {l_[1]} {f_[0]} {f_[1]} {r_[0]} {r_[1]} {b_[0]} {b_[1]}\033[38;5;202m               L L\033[38;5;46m F F\033[38;5;196m R R\033[38;5;21m B B
{l_[3]} {l_[2]} {f_[3]} {f_[2]} {r_[3]} {r_[2]} {b_[3]} {b_[2]}\033[38;5;202m               L L\033[38;5;46m F F\033[38;5;196m R R\033[38;5;21m B B
    {d_[0]} {d_[1]}\033[38;5;226m                           D D
    {d_[3]} {d_[2]}\033[38;5;226m                           D D
''')
    

main()
