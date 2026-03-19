#Replace all the zeros with 1. 

def rep(N):
    N=str(N)
    N=N.replace('0', '1')
    return int(N)

if __name__ == "__main__":
    N=102
    print(rep(N))