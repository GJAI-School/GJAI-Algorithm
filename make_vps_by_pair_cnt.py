def make_vps(now_idx, open_cnt, close_cnt, vps_str):
    if open_cnt == 0 and close_cnt == 0: # now_idx >= len(vps_str):
       print("".join(vps_str))
    else:
        if open_cnt > 0:
            vps_str[now_idx] = '('
            make_vps(now_idx+1, open_cnt-1, close_cnt+1, vps_str)
        if close_cnt > 0:
            vps_str[now_idx] = ')'
            make_vps(now_idx+1, open_cnt, close_cnt-1, vps_str)

pair_cnt = int(input())
vps_str = [""] * (pair_cnt*2)

make_vps(0, pair_cnt, 0, vps_str)
