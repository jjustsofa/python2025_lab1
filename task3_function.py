def funct(m):
    plot_list = [['-' for i in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            if i+ 3 * j==m-1:
                plot_list[i][j] = "!"
            if  i==m-1:
                plot_list[i][j] = j
            if  j==0:
                plot_list[i][j] = abs(i - m+1)

    for i in range(m):
        for j in range(m):
            print(plot_list[i][j], end="")
        print()
funct(10)
