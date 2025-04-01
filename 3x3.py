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
    global a_e, b_e, c_e, d_e, e_e, f_e, g_e, h_e, i_e, j_e, k_e, l_e, m_e, n_e, o_e, p_e, q_e, r_e, s_e, t_e, u_e, v_e, w_e, x_e
    global u_center, l_center, f_center, r_center, b_center, d_center
    # Corners #
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

    # Edges #

    a_e = '\033[0m#'
    b_e = '\033[0m#'
    c_e = '\033[0m#'
    d_e = '\033[0m#'
    # https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
    e_e = '\033[38;5;202m#'
    f_e = '\033[38;5;202m#'
    g_e = '\033[38;5;202m#'
    h_e = '\033[38;5;202m#'
    i_e = '\033[38;5;46m#'
    j_e = '\033[38;5;46m#'
    k_e = '\033[38;5;46m#'
    l_e = '\033[38;5;46m#'
    m_e = '\033[38;5;196m#'
    n_e = '\033[38;5;196m#'
    o_e = '\033[38;5;196m#'
    p_e = '\033[38;5;196m#'
    q_e = '\033[38;5;21m#'
    r_e = '\033[38;5;21m#'
    s_e = '\033[38;5;21m#'
    t_e = '\033[38;5;21m#'
    u_e = '\033[38;5;226m#'
    v_e = '\033[38;5;226m#'
    w_e = '\033[38;5;226m#'
    x_e = '\033[38;5;226m#'

    # Centers #

    u_center = '\033[0m#'
    l_center = '\033[38;5;202m#'
    f_center = '\033[38;5;46m#'
    r_center = '\033[38;5;196m#'
    b_center = '\033[38;5;21m#'
    d_center = '\033[38;5;226m#'

    # assigns the stickers to each face
    # indices 0-3 are corners, 4-7 are edges, 8 is centers
    u_ = [a, b, c, d, a_e, b_e, c_e, d_e, u_center]
    l_ = [e, f, g, h, e_e, f_e, g_e, h_e, l_center]
    f_ = [i, j, k, l, i_e, j_e, k_e, l_e, f_center]
    r_ = [m, n, o, p, m_e, n_e, o_e, p_e, r_center]
    b_ = [q, r, s, t, q_e, r_e, s_e, t_e, b_center]
    d_ = [u, v, w, x, u_e, v_e, w_e, x_e, d_center]
    # all moves used in scrambling
    all_moves = ['U', 'U\'', 'U2', 'R', 'R\'', 'R2', 'F', 'F\'', 'F2', 'L', 'L\'', 'L2', 'B', 'B\'', 'B2', 'D', 'D\'', 'D2']
    rotations = ['x', 'x\'', 'x2', 'y', 'y\'', 'y2', 'z', 'z\'', 'z2']
    movecount = 0
    print_cube(u_, l_, f_, r_, b_, d_, solved, movecount)
    while True:
        print('\033[0mType "scramble" to scramble the cube - Type "solve" to solve the cube instantly - Type "exit" to exit program')
        try:
            move = input().strip().split(' ')
        except EOFError:
            sys.exit('-EXIT-')
            
        for dir in move:
            movecount += 1
            if dir.lower() in rotations:
                movecount -= 1

            if dir == 'U':
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'U\'':
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'U2':
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'R':
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'R\'':
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'R2':
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'F':
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'F\'':
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'F2':
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'L':
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'L\'':
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'L2':
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'B':
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'B\'':
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'B2':
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'D':
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'D\'':
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'D2':
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
            # wide moves
            elif dir == 'u':
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'u\'':
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'u2':
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'r':
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'r\'':
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'r2':
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'f':
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'f\'':
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'f2':
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'l':
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'l\'':
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'l2':
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'b':
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'b\'':
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'b2':
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'd':
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'd\'':
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
            elif dir == 'd2':
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
            #
            elif dir.upper() == 'M':
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
            elif dir.upper() == 'M\'':
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
            elif dir.upper() == 'M2':
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
            elif dir.upper() == 'E':
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
            elif dir.upper() == 'E\'':
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
            elif dir.upper() == 'E2':
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
            elif dir.upper() == 'S':
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
            elif dir.upper() == 'S\'':
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
            elif dir.upper() == 'S2':
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'x':
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'x\'':
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'x2':
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = m_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'y':
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'y\'':
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'y2':
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = e_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'z':
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'z\'':
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
            elif dir.lower() == 'z2':
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = s_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
                u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
            elif dir.upper() == 'EXIT':
                sys.exit('-EXIT-')
            elif dir.upper() == 'SCRAMBLE':
                movecount = 0
                u_, l_, f_, r_, b_, d_ = scramble(u_, l_, f_, r_, b_, d_, all_moves)
            elif dir.upper() == 'SOLVE':
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
    # Corners #
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

    # Edges #
    # U
    a_e = u_[7]
    b_e = u_[4]
    c_e = u_[5]
    d_e = u_[6]
    # L
    e_e = f_[4]
    f_e = l_[5]
    g_e = l_[6]
    h_e = l_[7]
    # F
    i_e = r_[4]
    j_e = f_[5]
    k_e = f_[6]
    l_e = f_[7]
    # R
    m_e = b_[4]
    n_e = r_[5]
    o_e = r_[6]
    p_e = r_[7]
    # B
    q_e = l_[4]
    r_e = b_[5]
    s_e = b_[6]
    t_e = b_[7]
    # D
    u_e = d_[4]
    v_e = d_[5]
    w_e = d_[6]
    x_e = d_[7]

    # Centers #
    u_center = u_[8]
    l_center = l_[8]
    f_center = f_[8]
    r_center = r_[8]
    b_center = b_[8]
    d_center = d_[8]

    # Updates the list of each side
    u_ = [a, b, c, d, a_e, b_e, c_e, d_e, u_center]
    l_ = [e, f, g, h, e_e, f_e, g_e, h_e, l_center]
    f_ = [i, j, k, l, i_e, j_e, k_e, l_e, f_center]
    r_ = [m, n, o, p, m_e, n_e, o_e, p_e, r_center]
    b_ = [q, r, s, t, q_e, r_e, s_e, t_e, b_center]
    d_ = [u, v, w, x, u_e, v_e, w_e, x_e, d_center]
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

    # Edges #
    # U
    a_e = u_[4]
    b_e = f_[5]
    c_e = u_[6]
    d_e = u_[7]
    # L
    e_e = l_[4]
    f_e = l_[5]
    g_e = l_[6]
    h_e = l_[7]
    # F
    i_e = f_[4]
    j_e = d_[5]
    k_e = f_[6]
    l_e = f_[7]
    # R
    m_e = r_[7]
    n_e = r_[4]
    o_e = r_[5]
    p_e = r_[6]
    # B
    q_e = b_[4]
    r_e = b_[5]
    s_e = b_[6]
    t_e = u_[5]
    # D
    u_e = d_[4]
    v_e = b_[7]
    w_e = d_[6]
    x_e = d_[7]

    # Centers #
    u_center = u_[8]
    l_center = l_[8]
    f_center = f_[8]
    r_center = r_[8]
    b_center = b_[8]
    d_center = d_[8]

    # Updates the list of each side
    u_ = [a, b, c, d, a_e, b_e, c_e, d_e, u_center]
    l_ = [e, f, g, h, e_e, f_e, g_e, h_e, l_center]
    f_ = [i, j, k, l, i_e, j_e, k_e, l_e, f_center]
    r_ = [m, n, o, p, m_e, n_e, o_e, p_e, r_center]
    b_ = [q, r, s, t, q_e, r_e, s_e, t_e, b_center]
    d_ = [u, v, w, x, u_e, v_e, w_e, x_e, d_center]

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

    # Edges #
    # U
    a_e = u_[4]
    b_e = u_[5]
    c_e = l_[5]
    d_e = u_[7]
    # L
    e_e = l_[4]
    f_e = d_[4]
    g_e = l_[6]
    h_e = l_[7]
    # F
    i_e = f_[7]
    j_e = f_[4]
    k_e = f_[5]
    l_e = f_[6]
    # R
    m_e = r_[4]
    n_e = r_[5]
    o_e = r_[6]
    p_e = u_[6]
    # B
    q_e = b_[4]
    r_e = b_[5]
    s_e = b_[6]
    t_e = b_[7]
    # D
    u_e = r_[7]
    v_e = d_[5]
    w_e = d_[6]
    x_e = d_[7]

    # Centers #
    u_center = u_[8]
    l_center = l_[8]
    f_center = f_[8]
    r_center = r_[8]
    b_center = b_[8]
    d_center = d_[8]

    # Updates the list of each side
    u_ = [a, b, c, d, a_e, b_e, c_e, d_e, u_center]
    l_ = [e, f, g, h, e_e, f_e, g_e, h_e, l_center]
    f_ = [i, j, k, l, i_e, j_e, k_e, l_e, f_center]
    r_ = [m, n, o, p, m_e, n_e, o_e, p_e, r_center]
    b_ = [q, r, s, t, q_e, r_e, s_e, t_e, b_center]
    d_ = [u, v, w, x, u_e, v_e, w_e, x_e, d_center]

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

    # Edges #
    # U
    a_e = u_[4]
    b_e = u_[5]
    c_e = u_[6]
    d_e = b_[5]
    # L
    e_e = l_[7]
    f_e = l_[4]
    g_e = l_[5]
    h_e = l_[6]
    # F
    i_e = f_[4]
    j_e = f_[5]
    k_e = f_[6]
    l_e = u_[7]
    # R
    m_e = r_[4]
    n_e = r_[5]
    o_e = r_[6]
    p_e = r_[7]
    # B
    q_e = b_[4]
    r_e = d_[7]
    s_e = b_[6]
    t_e = b_[7]
    # D
    u_e = d_[4]
    v_e = d_[5]
    w_e = d_[6]
    x_e = f_[7]

    # Centers #
    u_center = u_[8]
    l_center = l_[8]
    f_center = f_[8]
    r_center = r_[8]
    b_center = b_[8]
    d_center = d_[8]

    # Updates the list of each side
    u_ = [a, b, c, d, a_e, b_e, c_e, d_e, u_center]
    l_ = [e, f, g, h, e_e, f_e, g_e, h_e, l_center]
    f_ = [i, j, k, l, i_e, j_e, k_e, l_e, f_center]
    r_ = [m, n, o, p, m_e, n_e, o_e, p_e, r_center]
    b_ = [q, r, s, t, q_e, r_e, s_e, t_e, b_center]
    d_ = [u, v, w, x, u_e, v_e, w_e, x_e, d_center]

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

    # Edges #
    # U
    a_e = r_[5]
    b_e = u_[5]
    c_e = u_[6]
    d_e = u_[7]
    # L
    e_e = l_[4]
    f_e = l_[5]
    g_e = l_[6]
    h_e = u_[4]
    # F
    i_e = f_[4]
    j_e = f_[5]
    k_e = f_[6]
    l_e = f_[7]
    # R
    m_e = r_[4]
    n_e = d_[6]
    o_e = r_[6]
    p_e = r_[7]
    # B
    q_e = b_[7]
    r_e = b_[4]
    s_e = b_[5]
    t_e = b_[6]
    # D
    u_e = d_[4]
    v_e = d_[5]
    w_e = l_[7]
    x_e = d_[7]

    # Centers #
    u_center = u_[8]
    l_center = l_[8]
    f_center = f_[8]
    r_center = r_[8]
    b_center = b_[8]
    d_center = d_[8]

    # Updates the list of each side
    u_ = [a, b, c, d, a_e, b_e, c_e, d_e, u_center]
    l_ = [e, f, g, h, e_e, f_e, g_e, h_e, l_center]
    f_ = [i, j, k, l, i_e, j_e, k_e, l_e, f_center]
    r_ = [m, n, o, p, m_e, n_e, o_e, p_e, r_center]
    b_ = [q, r, s, t, q_e, r_e, s_e, t_e, b_center]
    d_ = [u, v, w, x, u_e, v_e, w_e, x_e, d_center]

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

    # Edges #
    # U
    a_e = u_[4]
    b_e = u_[5]
    c_e = u_[6]
    d_e = u_[7]
    # L
    e_e = l_[4]
    f_e = l_[5]
    g_e = b_[6]
    h_e = l_[7]
    # F
    i_e = f_[4]
    j_e = f_[5]
    k_e = l_[6]
    l_e = f_[7]
    # R
    m_e = r_[4]
    n_e = r_[5]
    o_e = f_[6]
    p_e = r_[7]
    # B
    q_e = b_[4]
    r_e = b_[5]
    s_e = r_[6]
    t_e = b_[7]
    # D
    u_e = d_[7]
    v_e = d_[4]
    w_e = d_[5]
    x_e = d_[6]

    # Centers #
    u_center = u_[8]
    l_center = l_[8]
    f_center = f_[8]
    r_center = r_[8]
    b_center = b_[8]
    d_center = d_[8]

    # Updates the list of each side
    u_ = [a, b, c, d, a_e, b_e, c_e, d_e, u_center]
    l_ = [e, f, g, h, e_e, f_e, g_e, h_e, l_center]
    f_ = [i, j, k, l, i_e, j_e, k_e, l_e, f_center]
    r_ = [m, n, o, p, m_e, n_e, o_e, p_e, r_center]
    b_ = [q, r, s, t, q_e, r_e, s_e, t_e, b_center]
    d_ = [u, v, w, x, u_e, v_e, w_e, x_e, d_center]

    return u_, l_, f_, r_, b_, d_


def m_move(u_, l_, f_, r_, b_, d_):
    a = u_[0]
    b = u_[1]
    c = u_[2]
    d = u_[3]

    e = l_[0]
    f = l_[1]
    g = l_[2]
    h = l_[3]

    i = f_[0]
    j = f_[1]
    k = f_[2]
    l = f_[3]

    m = r_[0]
    n = r_[1]
    o = r_[2]
    p = r_[3]

    q = b_[0]
    r = b_[1]
    s = b_[2]
    t = b_[3]

    u = d_[0]
    v = d_[1]
    w = d_[2]
    x = d_[3]

    # Edges #
    # U
    a_e = b_[6]
    b_e = u_[5]
    c_e = b_[4]
    d_e = u_[7]
    # L
    e_e = l_[4]
    f_e = l_[5]
    g_e = l_[6]
    h_e = l_[7]
    # F
    i_e = u_[4]
    j_e = f_[5]
    k_e = u_[6]
    l_e = f_[7]
    # R
    m_e = r_[4]
    n_e = r_[5]
    o_e = r_[6]
    p_e = r_[7]
    # B
    q_e = d_[6]
    r_e = b_[5]
    s_e = d_[4]
    t_e = b_[7]
    # D
    u_e = f_[4]
    v_e = d_[5]
    w_e = f_[6]
    x_e = d_[7]

    # Centers #
    u_center = b_[8]
    l_center = l_[8]
    f_center = u_[8]
    r_center = r_[8]
    b_center = d_[8]
    d_center = f_[8]

    # Updates the list of each side
    u_ = [a, b, c, d, a_e, b_e, c_e, d_e, u_center]
    l_ = [e, f, g, h, e_e, f_e, g_e, h_e, l_center]
    f_ = [i, j, k, l, i_e, j_e, k_e, l_e, f_center]
    r_ = [m, n, o, p, m_e, n_e, o_e, p_e, r_center]
    b_ = [q, r, s, t, q_e, r_e, s_e, t_e, b_center]
    d_ = [u, v, w, x, u_e, v_e, w_e, x_e, d_center]

    return u_, l_, f_, r_, b_, d_


def e_move(u_, l_, f_, r_, b_, d_):
    a = u_[0]
    b = u_[1]
    c = u_[2]
    d = u_[3]

    e = l_[0]
    f = l_[1]
    g = l_[2]
    h = l_[3]

    i = f_[0]
    j = f_[1]
    k = f_[2]
    l = f_[3]

    m = r_[0]
    n = r_[1]
    o = r_[2]
    p = r_[3]

    q = b_[0]
    r = b_[1]
    s = b_[2]
    t = b_[3]

    u = d_[0]
    v = d_[1]
    w = d_[2]
    x = d_[3]

    # Edges #
    # U
    a_e = u_[4]
    b_e = u_[5]
    c_e = u_[6]
    d_e = u_[7]
    # L
    e_e = l_[4]
    f_e = b_[5]
    g_e = l_[6]
    h_e = b_[7]
    # F
    i_e = f_[4]
    j_e = l_[5]
    k_e = f_[6]
    l_e = l_[7]
    # R
    m_e = r_[4]
    n_e = f_[5]
    o_e = r_[6]
    p_e = f_[7]
    # B
    q_e = b_[4]
    r_e = r_[5]
    s_e = b_[6]
    t_e = r_[7]
    # D
    u_e = d_[4]
    v_e = d_[5]
    w_e = d_[6]
    x_e = d_[7]

    # Centers #
    u_center = u_[8]
    l_center = b_[8]
    f_center = l_[8]
    r_center = f_[8]
    b_center = r_[8]
    d_center = d_[8]

    # Updates the list of each side
    u_ = [a, b, c, d, a_e, b_e, c_e, d_e, u_center]
    l_ = [e, f, g, h, e_e, f_e, g_e, h_e, l_center]
    f_ = [i, j, k, l, i_e, j_e, k_e, l_e, f_center]
    r_ = [m, n, o, p, m_e, n_e, o_e, p_e, r_center]
    b_ = [q, r, s, t, q_e, r_e, s_e, t_e, b_center]
    d_ = [u, v, w, x, u_e, v_e, w_e, x_e, d_center]

    return u_, l_, f_, r_, b_, d_


def s_move(u_, l_, f_, r_, b_, d_):
    a = u_[0]
    b = u_[1]
    c = u_[2]
    d = u_[3]

    e = l_[0]
    f = l_[1]
    g = l_[2]
    h = l_[3]

    i = f_[0]
    j = f_[1]
    k = f_[2]
    l = f_[3]

    m = r_[0]
    n = r_[1]
    o = r_[2]
    p = r_[3]

    q = b_[0]
    r = b_[1]
    s = b_[2]
    t = b_[3]

    u = d_[0]
    v = d_[1]
    w = d_[2]
    x = d_[3]

    # Edges #
    # U
    a_e = u_[4]
    b_e = l_[4]
    c_e = u_[6]
    d_e = l_[6]
    # L
    e_e = d_[7]
    f_e = l_[5]
    g_e = d_[5]
    h_e = l_[7]
    # F
    i_e = f_[4]
    j_e = f_[5]
    k_e = f_[6]
    l_e = f_[7]
    # R
    m_e = u_[7]
    n_e = r_[5]
    o_e = u_[5]
    p_e = r_[7]
    # B
    q_e = b_[4]
    r_e = b_[5]
    s_e = b_[6]
    t_e = b_[7]
    # D
    u_e = d_[4]
    v_e = r_[4]
    w_e = d_[6]
    x_e = r_[6]

    # Centers #
    u_center = l_[8]
    l_center = d_[8]
    f_center = f_[8]
    r_center = u_[8]
    b_center = b_[8]
    d_center = r_[8]

    # Updates the list of each side
    u_ = [a, b, c, d, a_e, b_e, c_e, d_e, u_center]
    l_ = [e, f, g, h, e_e, f_e, g_e, h_e, l_center]
    f_ = [i, j, k, l, i_e, j_e, k_e, l_e, f_center]
    r_ = [m, n, o, p, m_e, n_e, o_e, p_e, r_center]
    b_ = [q, r, s, t, q_e, r_e, s_e, t_e, b_center]
    d_ = [u, v, w, x, u_e, v_e, w_e, x_e, d_center]

    return u_, l_, f_, r_, b_, d_


def scramble(u_, l_, f_, r_, b_, d_, moves):
    # 20 is God's Number for 3x3 (HTM)
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
            u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'U2':
            u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = u_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'R':
            u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'R\'':
            u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'R2':
            u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = r_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'F':
            u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'F\'':
            u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'F2':
            u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = f_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'L':
            u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'L\'':
            u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'L2':
            u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = l_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'B':
            u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'B\'':
            u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'B2':
            u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = b_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'D':
            u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'D\'':
            u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
        elif dir == 'D2':
            u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)
            u_, l_, f_, r_, b_, d_ = d_move(u_, l_, f_, r_, b_, d_)

        if iteration >= 11:
            break

    return u_, l_, f_, r_, b_, d_


def check_solved(u_, l_, f_, r_, b_, d_):
    if ((u_ == [a, b, c, d, a_e, b_e, c_e, d_e, u_center] or u_ == [e, f, g, h, e_e, f_e, g_e, h_e, l_center] or u_ == [i, j, k, l, i_e, j_e, k_e, l_e, f_center] or u_ == [m, n, o, p, m_e, n_e, o_e, p_e, r_center] or u_ == [q, r, s, t, q_e, r_e, s_e, t_e, b_center] or u_ == [u, v, w, x, u_e, v_e, w_e, x_e, d_center]) and
        (l_ == [a, b, c, d, a_e, b_e, c_e, d_e, u_center] or l_ == [e, f, g, h, e_e, f_e, g_e, h_e, l_center] or l_ == [i, j, k, l, i_e, j_e, k_e, l_e, f_center] or l_ == [m, n, o, p, m_e, n_e, o_e, p_e, r_center] or l_ == [q, r, s, t, q_e, r_e, s_e, t_e, b_center] or l_ == [u, v, w, x, u_e, v_e, w_e, x_e, d_center]) and
        (f_ == [a, b, c, d, a_e, b_e, c_e, d_e, u_center] or f_ == [e, f, g, h, e_e, f_e, g_e, h_e, l_center] or f_ == [i, j, k, l, i_e, j_e, k_e, l_e, f_center] or f_ == [m, n, o, p, m_e, n_e, o_e, p_e, r_center] or f_ == [q, r, s, t, q_e, r_e, s_e, t_e, b_center] or f_ == [u, v, w, x, u_e, v_e, w_e, x_e, d_center]) and
        (r_ == [a, b, c, d, a_e, b_e, c_e, d_e, u_center] or r_ == [e, f, g, h, e_e, f_e, g_e, h_e, l_center] or r_ == [i, j, k, l, i_e, j_e, k_e, l_e, f_center] or r_ == [m, n, o, p, m_e, n_e, o_e, p_e, r_center] or r_ == [q, r, s, t, q_e, r_e, s_e, t_e, b_center] or r_ == [u, v, w, x, u_e, v_e, w_e, x_e, d_center]) and
        (b_ == [a, b, c, d, a_e, b_e, c_e, d_e, u_center] or b_ == [e, f, g, h, e_e, f_e, g_e, h_e, l_center] or b_ == [i, j, k, l, i_e, j_e, k_e, l_e, f_center] or b_ == [m, n, o, p, m_e, n_e, o_e, p_e, r_center] or b_ == [q, r, s, t, q_e, r_e, s_e, t_e, b_center] or b_ == [u, v, w, x, u_e, v_e, w_e, x_e, d_center]) and
        (d_ == [a, b, c, d, a_e, b_e, c_e, d_e, u_center] or d_ == [e, f, g, h, e_e, f_e, g_e, h_e, l_center] or d_ == [i, j, k, l, i_e, j_e, k_e, l_e, f_center] or d_ == [m, n, o, p, m_e, n_e, o_e, p_e, r_center] or d_ == [q, r, s, t, q_e, r_e, s_e, t_e, b_center] or d_ == [u, v, w, x, u_e, v_e, w_e, x_e, d_center])):
            return True
    else:
        return False
    

def solve_cube(u_, l_, f_, r_, b_, d_):
    u_ = [a, b, c, d, a_e, b_e, c_e, d_e, u_center]
    l_ = [e, f, g, h, e_e, f_e, g_e, h_e, l_center]
    f_ = [i, j, k, l, i_e, j_e, k_e, l_e, f_center]
    r_ = [m, n, o, p, m_e, n_e, o_e, p_e, r_center]
    b_ = [q, r, s, t, q_e, r_e, s_e, t_e, b_center]
    d_ = [u, v, w, x, u_e, v_e, w_e, x_e, d_center]
    return u_, l_, f_, r_, b_, d_


def print_cube(u_, l_, f_, r_, b_, d_, solved, movecount):
    os.system(clear)
    print(f'''\033[0m- Cube.py -
          
      {u_[0]} {u_[4]} {u_[1]}\033[0m         {solved}                U U U          Movecount: {movecount}
      {u_[7]} {u_[8]} {u_[5]}\033[0m                                 U U U
      {u_[3]} {u_[6]} {u_[2]}\033[0m                                 U U U
{l_[0]} {l_[4]} {l_[1]} {f_[0]} {f_[4]} {f_[1]} {r_[0]} {r_[4]} {r_[1]} {b_[0]} {b_[4]} {b_[1]}\033[38;5;202m               L L L\033[38;5;46m F F F\033[38;5;196m R R R\033[38;5;21m B B B
{l_[7]} {l_[8]} {l_[5]} {f_[7]} {f_[8]} {f_[5]} {r_[7]} {r_[8]} {r_[5]} {b_[7]} {b_[8]} {b_[5]}\033[38;5;202m               L L L\033[38;5;46m F F F\033[38;5;196m R R R\033[38;5;21m B B B
{l_[3]} {l_[6]} {l_[2]} {f_[3]} {f_[6]} {f_[2]} {r_[3]} {r_[6]} {r_[2]} {b_[3]} {b_[6]} {b_[2]}\033[38;5;202m               L L L\033[38;5;46m F F F\033[38;5;196m R R R\033[38;5;21m B B B
      {d_[0]} {d_[4]} {d_[1]}\033[38;5;226m                                 D D D
      {d_[7]} {d_[8]} {d_[5]}\033[38;5;226m                                 D D D
      {d_[3]} {d_[6]} {d_[2]}\033[38;5;226m                                 D D D
''')
    

main()
