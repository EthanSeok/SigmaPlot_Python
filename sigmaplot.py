import pandas as pd
from scipy.optimize import differential_evolution
import matplotlib.pyplot as plt
import seaborn as sns
import os
from tqdm import tqdm


def func(parameters, *data):
    y0, a, b = parameters
    x, y = data
    result = 0
    for i in range(len(x)):
        result += ((y0 + a * x[i] / (b + x[i])) - y[i])**2

    return result ** 0.5


def cal(infile, s):
    s_df = pd.melt(infile, id_vars=['Ca'], value_vars=[f"{s}-1", f"{s}-2", f"{s}-3", f"{s}-4"], var_name='S', value_name=f'{s}')
    bounds = [(-10, -1), (10, 100), (200, 1000)]
    x = s_df['Ca'].values
    y = s_df[f'{s}'].values
    args = (x, y)

    results = differential_evolution(func, bounds, args=args)
    # print(f"{s} results:", results.x)
    return results, s, s_df


def plot(infile, output_dir, filename):
    fig, ax = plt.subplots(figsize=(9.4,6))
    x = infile['Ca'].sort_values(ascending=True).values
    s_values = ['S1', 'S2', 'S3', 'S4'] if 'S4-1' in infile.columns else ['S1', 'S2', 'S3']
    An_dict = {}
    color_list = ['#7f0000', '#006837', '#feb24c', '#253494']

    with tqdm(total=len(s_values), desc=f'{filename}', unit='image') as pbar:
        for i, (s, label) in enumerate(zip(s_values, ['Ca vs 1-1 - 1-4 \n', 'Ca vs 2-1 - 2-4 \n', 'Ca vs 3-1 - 3-4 \n', 'Ca vs 4-1 - 4-4 \n'] if 'S4-1' in infile.columns else ['Ca vs 1-1 - 1-4 \n', 'Ca vs 2-1 - 2-4 \n', 'Ca vs 3-1 - 3-4 \n'])):
            An = []
            results, s , s_df = cal(infile, s)
            y0 = results.x[0]
            a = results.x[1]
            b = results.x[2]
            for j in range(len(x)):
                An.append((y0 + a * x[j] / (b + x[j])))
            An_dict[s] = An
            grouped = s_df.groupby('Ca').agg({s: ['mean', 'sem']})
            grouped.columns = ['S1_mean', 'S1_std']
            grouped.reset_index(inplace=True)
            x = grouped['Ca']
            y = grouped['S1_mean']
            yerr = grouped['S1_std']
            sns.lineplot(x=x, y=An, color=color_list[i], legend=False, linewidth=1.5, alpha=0.84)
            ax.errorbar(x=x, y=y, yerr=yerr, label=f"{label} {y0:.3f}+{a:.3f}*x/({b:.4f}+x)", color=color_list[i], fmt='o', capsize=6, markersize=7.5)
            pbar.update(1)
    ax.set(ylim=(-10, 40))
    ax.set_ylabel('$A(μmol/m^2/s)$')
    ax.set(xlim=(-100, 1600))
    ax.set_xlabel('$Ca(μmol/mol)$')
    ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
    fig.subplots_adjust(right=0.68)
    fig.savefig(os.path.join(f'{output_dir}/{filename}.png'), dpi=300)


def main():
    output_dir = "output/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    method = input('파일을 개별 입력하겠습니까? ex) yes or no : ')

    if method == 'yes':
        filename = input('파일 이름을 입력하시오: ')
        infile = pd.read_excel(f'input/{filename}')
        plot(infile, output_dir, filename)

    elif method == 'no':
        file_paths = [f'input/{x}' for x in os.listdir("input/") if x.endswith(".xlsx") or x.endswith(".csv")]
        for file_path in file_paths:
            if file_path.endswith(".xlsx"):
                infile = pd.read_excel(file_path)
            elif file_path.endswith(".csv"):
                infile = pd.read_csv(file_path)
            filename = os.path.splitext(os.path.basename(file_path))[0]
            plot(infile, output_dir, filename)


if __name__ == '__main__':
    main()