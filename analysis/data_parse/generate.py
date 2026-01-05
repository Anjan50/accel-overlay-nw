import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files
df = pd.read_csv('finalized_bitrate.csv')
confidence_df = pd.read_csv('confidence_bitrate.csv')

# Filter out columns containing "RPS-7" or "RPS-7+"
df = df.loc[:, ~df.columns.str.contains('RPS-7')]
confidence_df = confidence_df.loc[:, ~confidence_df.columns.str.contains('RPS-7')]

# Reorder the columns
columns_order = ['Replicas', 'Baseline', 'RPS', 'RPS+', 'RFS', 'RFS+']
df = df[columns_order]
confidence_df = confidence_df[columns_order]

# Set the 'Replicas' column as the index
df.set_index('Replicas', inplace=True)
confidence_df.set_index('Replicas', inplace=True)

# Define textures for the bars
textures = ['/', '\\', '+', '', '|', '.', '-']

# Generate the bar chart with extended length, error bars, thicker bars, and textures
# ax = df.plot(kind='bar', yerr=confidence_df.values.T, figsize=(18, 5), capsize=4, width=0.8, color='none', edgecolor='black', linewidth=2)
ax = df.plot(kind='bar', yerr=confidence_df.values.T, figsize=(15, 5), capsize=4, width=0.9, edgecolor='black', linewidth=2)


# Apply textures to each bar group
counter = 0
for bar in ax.patches:
    bar.set_hatch(textures[counter // 5])
    counter += 1

# Add labels with increased font size
plt.xlabel('Replicas', fontsize=18)
plt.ylabel('Normalized Average Bitrate', fontsize=18)

# Set the y-axis scale to start from 0.8
plt.ylim(0.9, df.values.max() + 0.1)

# Position the legend to avoid interfering with the bars, increase font size, and increase legend box size
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=16, prop={'size': 16})

# Rotate the x-axis labels and increase font size
plt.xticks(rotation=0, fontsize=20)
plt.yticks(fontsize=20)

# Reduce whitespace around the plot
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('bitrateresults1.png')

plt.clf()
plt.cla()

# Define the data groups
data_groups = [("1_idle", "16_idle"), ("1_soft", "16_soft")]

for group in data_groups:
    fig, axes = plt.subplots(1, 2, figsize=(30, 10))
    fig.subplots_adjust(wspace=5)  # Add padding between the two bar charts

    for ax, data in zip(axes, group):
        df = pd.read_csv(f'finalized_{data}.csv')
        confidence_df = pd.read_csv(f'confidence_{data}.csv')

        # Filter out rows containing "RPS-7" or "RPS-7+"
        df = df[~df['Type'].str.contains('RPS-7')]
        confidence_df = confidence_df[~confidence_df['Type'].str.contains('RPS-7')]

        # Reorder the rows
        rows_order = ['Baseline', 'RPS', 'RPS+', 'RFS', 'RFS+']
        df = df.set_index('Type').reindex(rows_order).reset_index()
        confidence_df = confidence_df.set_index('Type').reindex(rows_order).reset_index()

        # Set the 'Type' column as the index
        df.set_index('Type', inplace=True)
        confidence_df.set_index('Type', inplace=True)
        df.plot(kind='bar', yerr=confidence_df.values.T, ax=ax, capsize=4, width=0.9, edgecolor='black', linewidth=2)

        counter = 0
        for bar in ax.patches:
            bar.set_hatch(textures[counter // 7])
            counter += 1

        ax.set_xlabel('Type', fontsize=28)
        title = "idle %" if "idle" in data else "soft %"
        ax.set_ylabel(title, fontsize=28)

        ax.set_ylim(0, 100)
        
        # Only add legend to the second plot in each group
        if "16_" in data:
            ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=30, prop={'size': 30})
        else:
            ax.get_legend().remove()

        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, fontsize=30)
        ax.tick_params(axis='y', labelsize=30)

    axes[0].annotate('(a) 1 Replica', xy=(0.5, -0.5), xycoords='axes fraction', fontsize=28, ha='center')
    axes[1].annotate('(b) 16 Replicas', xy=(0.5, -0.5), xycoords='axes fraction', fontsize=28, ha='center')

    plt.tight_layout(pad=2.0)
    plt.savefig(f'{group[0]}_{group[1]}.png')

    plt.clf()
    plt.cla()

