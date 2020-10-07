import statisticsfrom scipy.stats import skewimport matplotlib.pyplot as pltimport numpyimport randomf = open('var10.txt')lines_from_file = []for line in f.read().splitlines():    lines_from_file.append(float(line))count_of_lines = len(lines_from_file)def lineplot(x_data, y_data, x_label="", y_label="", title=""):    _, ax = plt.subplots()    ax.plot(x_data, y_data, lw=2, color='#000000', alpha=1)    ax.set_title(title)    ax.set_xlabel(x_label)    ax.set_ylabel(y_label)def boxplot(x_data, y_data, base_color="#000000", median_color="#297083", x_label="", y_label="", title=""):    _, ax = plt.subplots()    ax.boxplot(y_data               , patch_artist=True               , medianprops={'color': median_color}               , boxprops={'color': base_color, 'facecolor': base_color}               , whiskerprops={'color': base_color}               , capprops={'color': base_color})    ax.set_ylabel(y_label)    ax.set_xlabel(x_label)    ax.set_title(title)def histogram(data, n_bins, cumulative=False, x_label="", y_label="", title=""):    _, ax = plt.subplots()    ax.hist(data, bins=n_bins, cumulative=cumulative, color='#000000')    ax.set_ylabel(y_label)    ax.set_xlabel(x_label)    ax.set_title(title)lineplot([i for i in range(100)], lines_from_file[:100], '', 'Значения из файла')boxplot([i for i in range(count_of_lines)], lines_from_file)histogram(lines_from_file, 3)histogram(lines_from_file, 15)histogram(lines_from_file, 30)# plt.show()print('------------------------------Числовые характеристики выборки------------------------------')sum_of_lines = sum(lines_from_file)avg_score1 = sum_of_lines / count_of_linesprint('Среднее значение для обычной выборки:\t', avg_score1)def stdev(nums):    diffs = 0    for n in nums:        diffs += (n - avg_score1) ** (2)    return (diffs / (len(nums) - 1)) ** (0.5)print('Стандартное отклонение:\t', stdev(lines_from_file))print('Дисперсия:\t', stdev(lines_from_file) ** 2)print('Медиана:\t', numpy.median(lines_from_file))print('Коэффициент асимметрии:\t', skew(lines_from_file))print('Минимальное значение выборки:\t', min(lines_from_file))print('Максимальное значение выборки:\t', max(lines_from_file))print('------------------------------Работа с пропусками------------------------------')lines_to_grab = random.sample([i for i in range(count_of_lines)], 700)lines_from_file_with_spaces = []for i, line in enumerate(lines_from_file):    if i in sorted(lines_to_grab):        lines_from_file_with_spaces.append(line)sum_of_lines = sum(lines_from_file_with_spaces)avg_score = sum_of_lines / len(lines_from_file)print('Среднее значение для выборки с пропусками:\t', avg_score)def stdev(nums):    diffs = 0    for n in nums:        diffs += (n - avg_score) ** (2)    return (diffs / (len(nums) - 1)) ** (0.5)print('Стандартное отклонение:\t', stdev(lines_from_file_with_spaces))print('Дисперсия:\t', stdev(lines_from_file_with_spaces) ** 2)print('Медиана:\t', numpy.median(lines_from_file_with_spaces))print('Коэффициент асимметрии:\t', skew(lines_from_file_with_spaces))print('Минимальное значение выборки:\t', min(lines_from_file_with_spaces))print('Максимальное значение выборки:\t', max(lines_from_file_with_spaces))print('---------------------------------------------------------------------------------')trash = [i for i in range(300)]www = []for i in trash:    i = avg_score1    www.append(i)new_list_without_spaces = lines_from_file_with_spaces + wwwsum_of_lines = sum(new_list_without_spaces)avg_score = sum_of_lines / count_of_linesprint('Среднее значение для выборки с средним вместо пропусков:\t', avg_score)def stdev(nums):    diffs = 0    for n in nums:        diffs += (n - avg_score) ** (2)    return (diffs / (len(nums) - 1)) ** (0.5)print('Стандартное отклонение:\t', stdev(new_list_without_spaces))print('Дисперсия:\t', stdev(new_list_without_spaces) ** 2)print('Медиана:\t', numpy.median(new_list_without_spaces))print('Коэффициент асимметрии:\t', skew(new_list_without_spaces))print('Минимальное значение выборки:\t', min(new_list_without_spaces))print('Максимальное значение выборки:\t', max(new_list_without_spaces))print('------------------------------Цензурирование данных снизу------------------------------')censorship_lines_with_spaces = []c = (max(lines_from_file) / 3) + (2 * min(lines_from_file) / 3)for i in lines_from_file:    if i > c:        censorship_lines_with_spaces.append(i)sum_of_lines = sum(censorship_lines_with_spaces)avg_score = sum_of_lines / count_of_linesprint('Среднее значение для выборки с цензурированием:\t', avg_score)def stdev(nums):    diffs = 0    for n in nums:        diffs += (n - avg_score) ** (2)    return (diffs / (len(nums) - 1)) ** (0.5)print('Стандартное отклонение:\t', stdev(censorship_lines_with_spaces))print('Дисперсия:\t', stdev(censorship_lines_with_spaces) ** 2)print('Медиана:\t', numpy.median(censorship_lines_with_spaces))print('Коэффициент асимметрии:\t', skew(censorship_lines_with_spaces))print('Минимальное значение выборки:\t', min(censorship_lines_with_spaces))print('Максимальное значение выборки:\t', max(censorship_lines_with_spaces))print('---------------------------------------------------------------------------------')for i in trash:    i = avg_score1    www.append(i)censorship_lines_without_spaces = censorship_lines_with_spaces + wwwsum_of_lines = sum(censorship_lines_without_spaces)avg_score = sum_of_lines / count_of_linesprint('Среднее значение для выборки с цензурированием без пропусков:\t', avg_score)def stdev(nums):    diffs = 0    for n in nums:        diffs += (n - avg_score) ** (2)    return (diffs / (len(nums) - 1)) ** (0.5)print('Стандартное отклонение:\t', stdev(censorship_lines_without_spaces))print('Дисперсия:\t', stdev(censorship_lines_without_spaces) ** 2)print('Медиана:\t', numpy.median(censorship_lines_without_spaces))print('Коэффициент асимметрии:\t', skew(censorship_lines_without_spaces))print('Минимальное значение выборки:\t', min(censorship_lines_without_spaces))print('Максимальное значение выборки:\t', max(censorship_lines_without_spaces))