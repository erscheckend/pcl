import json
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys

"""
ChatGPT laid the basis for this code since we were unfamiliar with Seaborn.
We adjusted it to get the graphs together the way we want them.
To run on Windows: python3 Seaborn.py [Path to file with the averages] [Path to file with all values]
These JSON files should be created by running the Part2.py
From the JSON files, we manually deleted the values for "King", as they were only a side effect of the grep.
"""

def plot_sentiment_averages(file_path):
    with open(file_path) as file:
        data = json.load(file)

    sns.set(style='whitegrid')

    for entry in data:
        name = entry['name']
        averages_data = entry['averages']

        df = pd.DataFrame(averages_data)

        #make a lineplot for the averages
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='chapter', y='average', data=df, marker='o', linestyle='-', color='b')
        plt.title(f'Sentiment of {name} over time')
        plt.xlabel('Chapter')
        plt.ylabel('Sentiment Score')

        #save it
        output_path_lineplot = f'{name}_averages_lineplot.png'
        plt.savefig(output_path_lineplot)
        print(f'Lineplot saved as {output_path_lineplot}')

        plt.show(block=False)

def plot_sentiment_all_values(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    sns.set(style='whitegrid')

    df_list = []  # Initialize df_list outside the loop

    for entry in data:
        name = entry['name']

        for chapter_data in entry['data']:
            chapter = chapter_data['chapter']
            values = chapter_data['values']
            df_list.append({'name': name, 'chapter': chapter, 'values': values})

    df = pd.DataFrame(df_list)

    df = df.explode('values')

    # make a lineplot
    plt.figure(figsize=(15, 5))
    sns.lineplot(x='chapter', y='values', hue='name', data=df)
    plt.title(f'Line plot')
    plt.xlabel('Chapter')
    plt.ylabel('Sentiment Score')

    output_path_lineplot = f'All_values_lineplot.png'
    plt.savefig(output_path_lineplot)
    print(f'Lineplot saved as {output_path_lineplot}')

    plt.show(block=False)

    # make a boxplot
    plt.figure(figsize=(15, 5))
    sns.boxplot(x='chapter', y='values', hue='name', data=df)
    plt.title(f'Box plot')
    plt.xlabel('Chapter')
    plt.ylabel('Sentiment Score')

    output_path_boxplot = f'All_values_boxplot.png'
    plt.savefig(output_path_boxplot)
    print(f'Boxplot saved as {output_path_boxplot}')

    plt.show(block=False)

    # make a violinplot
    plt.figure(figsize=(15, 5))
    sns.violinplot(x='chapter', y='values', hue='name', data=df)
    plt.title(f'Violin plot')
    plt.xlabel('Chapter')
    plt.ylabel('Sentiment Score')

    output_path_violinplot = f'All_values_violinplot.png'
    plt.savefig(output_path_violinplot)
    print(f'Violinplot saved as {output_path_violinplot}')

    plt.show(block=False)

def main():
    if len(sys.argv) != 3:
        print('How to use: python script.py [path to averages JSON file] [path to all values JSON file]')
        sys.exit(1)

    averages_file_path = sys.argv[1]
    all_values_file_path = sys.argv[2]

    plot_sentiment_averages(averages_file_path)
    plot_sentiment_all_values(all_values_file_path)

if __name__ == '__main__':
    main()
