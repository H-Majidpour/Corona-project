import matplotlib.pyplot as plt
import numpy as np




def random_color(number):
    colors = []
    i = 0
    while i<number:
        this_color = list(np.random.choice(range(100), size=3))
        tmp_color = []
        tmp_color.append(this_color[0]/100)
        tmp_color.append(this_color[1]/100)
        tmp_color.append(this_color[2]/100)
        colors.append(tmp_color)

        i += 1

    return colors





def get_plot(country, totalcases):
    number_of_countres = 10
    tmp_country = []
    totalcases_int = []

    for i in range(0, number_of_countres):
        string_number = totalcases[i]
        if ',' in string_number:
            tmp_list = string_number.split(",")
            string_number = tmp_list[0] + tmp_list[1] + tmp_list[2]
            totalcases_int.append(int(string_number))
        else:
            totalcases_int.append(int(string_number))

        tmp_country.append(country[i])

    country = tmp_country


    plot_src = "statics/DB/plot.png"
    register = range(0, number_of_countres)
    plt.figure(figsize= (8, 10))
    b = plt.barh(register, totalcases_int,height=.8, color=tuple(random_color(number_of_countres)))
    plt.yticks(register, country)
    plt.title("Statistics of 10 countries involved in Corona")
    plt.legend(b, country, fontsize = 14)
    plt.savefig(plot_src)

    return plot_src