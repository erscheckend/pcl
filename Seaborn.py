import argparse
import json
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_sentiment(file_path):
    with open(file_path) as file:
        characters_data = json.load(file)

    # Set Seaborn style
    sns.set(style="whitegrid")

    # Iterate over each character
    for character_data in characters_data:
        name = character_data['name']
        averages_data = character_data['averages']

        # Convert character's data to a Pandas DataFrame
        df = pd.DataFrame(averages_data)

        # Plotting sentiment for each character using Seaborn's lineplot
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='chapter', y='average', data=df, marker='o', linestyle='-', color='b')
        plt.title(f'Sentiment of {name} over time')
        plt.xlabel('Chapter')
        plt.ylabel('Sentiment Score')

        # Save the lineplot as an image file for each character
        output_path_lineplot = f'{name}_sentiment_lineplot.png'
        plt.savefig(output_path_lineplot)
        print(f"Lineplot saved as {output_path_lineplot}")

        # Show the lineplot (non-blockingly)
        plt.show(block=False)

        # Create a boxplot for each character
        plt.figure(figsize=(12, 8))
        sns.boxplot(x="chapter", y="average", data=df, palette="Set3")
        plt.title(f'Sentiment Distribution Over Chapters for {name}')
        plt.xlabel('Chapter')
        plt.ylabel('Sentiment Score')

        # Save the boxplot as an image file for each character
        output_path_boxplot = f'{name}_sentiment_boxplot.png'
        plt.savefig(output_path_boxplot)
        print(f"Boxplot saved as {output_path_boxplot}")

        # Show the boxplot (non-blockingly)
        plt.show(block=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot sentiment analysis results.")
    parser.add_argument("file_path", help="Path to the JSON file with sentiment data")

    args = parser.parse_args()
    plot_sentiment(args.file_path)
