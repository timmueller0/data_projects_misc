# The clusters (i.e., which number is which sector) change at any run! Doublecheck before using!! #
import sklearn
from sklearn.cluster import SpectralClustering

# Convert correlation matrix to distance matrix
np.fill_diagonal(correlations.values, 1)
distance_matrix = 1 - correlations

# Apply Spectral Clustering
spectral = SpectralClustering(n_clusters=5, affinity='precomputed')
clusters = spectral.fit_predict(correlations)

# Add cluster labels to the DataFrame
correlations['Cluster'] = clusters
print(correlations['Cluster'])

# Create a dictionary, assigning ticker symbols to clusters
print(correlations['Cluster'].unique())

stock_clusters = {}
for x in range(5):
    stock_clusters["Cluster {0}".format(x)] = correlations.index[correlations['Cluster'] == x].tolist()

# Make sure that avg_growth dataframe exists
avg_growth = pd.DataFrame(avg_growth, columns=['Average Growth'])

# Cluster 0
# This list contains stock symbols from sectors primarily focused on utilities, real estate, and infrastructure.
# Overall, this list includes companies that tend to offer steady returns through dividends and are viewed as defensive
# or income-generating investments. However, growth prospects might be slower compared to sectors like tech.
# The focus on infrastructure, utilities, and real estate reflects companies that provide essential services,
# making them resilient to economic cycles.

cluster_0_returns = daily_growth.loc[0:,['Date'] + list(stock_clusters["Cluster 0"])]

network_c0 = create_net(cluster_0_returns)
degrees_c0 = pd.DataFrame(network_c0.apply(lambda x: np.nansum(x)), columns=['Degree'])
degrees_c0_growth = pd.merge(left = degrees_c0, right = avg_growth, left_index=True, right_index=True)
print(degrees_c0_growth.corr()) # positive degree - growth correlation

print(stock_clusters["Cluster 0"])
print(degrees_c0_growth['Average Growth'].describe())
print(avg_growth['Average Growth'].describe())

# Cluster 1
# This new list spans a broader range of sectors, with a focus on healthcare, energy, insurance, and industrials.
# This list represents a diversified mix of sectors, with heavy representation in energy, healthcare, and
# insurance/financial services. Energy companies offer high returns when oil prices surge but are volatile;
# healthcare firms offer consistent performance driven by the essential nature of their services; insurance and financial
# services firms provide stability through premiums and transactions. Industrial and aerospace companies, particularly
# in defense, are stable growth sectors supported by government contracts.
# It’s a mix of both growth and income-oriented investments, offering diversification across different economic cycles.

cluster_1_returns = daily_growth.loc[0:,['Date'] + list(stock_clusters["Cluster 1"])]

network_c1 = create_net(cluster_1_returns)
degrees_c1 = pd.DataFrame(network_c1.apply(lambda x: np.nansum(x)), columns=['Degree'])
degrees_c1_growth = pd.merge(left = degrees_c1, right = avg_growth, left_index=True, right_index=True)
print(degrees_c1_growth.corr()) # negative degree - growth correlation

print(stock_clusters["Cluster 1"])
print(degrees_c1_growth['Average Growth'].describe())
print(avg_growth['Average Growth'].describe())

# Cluster 2
# This list spans a broad range of industries, making it quite diverse.
# This list offers significant diversification across industries, with strong representation in financials, industrials,
# and energy. Many of these companies are household names in their respective sectors, like GE, JPM, MCD, UPS, and IBM.
# It includes both cyclical and defensive stocks, providing a mix of growth opportunities (e.g., technology and
# consumer discretionary) and income-generating options (e.g., financials and industrials).
# The diversity in this list makes it robust for various economic environments, with some sectors performing better in
# growth periods (e.g., technology and consumer discretionary) and others offering stability in downturns
# (e.g., financials, healthcare, and energy).

cluster_2_returns = daily_growth.loc[0:,['Date'] + list(stock_clusters["Cluster 2"])]

network_c2 = create_net(cluster_2_returns)
degrees_c2 = pd.DataFrame(network_c2.apply(lambda x: np.nansum(x)), columns=['Degree'])
degrees_c2_growth = pd.merge(left = degrees_c2, right = avg_growth, left_index=True, right_index=True)
print(degrees_c2_growth.corr()) # negative degree - growth correlation

print(stock_clusters["Cluster 2"])
print(degrees_c2_growth['Average Growth'].describe())
print(avg_growth['Average Growth'].describe())

# Cluster 3
# This list leans heavily toward technology, healthcare, and consumer discretionary companies.
# Technology dominates, especially in software, semiconductors, and payment processing, reflecting the modern economy's
# tech-driven focus.
# Healthcare companies, especially those involved in medical devices and biotech, are strongly represented.
# Consumer discretionary brands such as AMZN, NKE, YUM, and TSLA indicate a focus on companies that benefit from long-term
# shifts in consumer behavior.
# Payment processing firms (MA, V, PAYX) and financial services firms like KKR and SPGI emphasize the intersection of
# finance and technology.
# This list is heavily weighted toward growth sectors, with strong representation in tech, healthcare, and consumer
# discretionary, providing substantial exposure to innovation and future trends.

cluster_3_returns = daily_growth.loc[0:,['Date'] + list(stock_clusters["Cluster 3"])]

network_c3 = create_net(cluster_3_returns)
degrees_c3 = pd.DataFrame(network_c3.apply(lambda x: np.nansum(x)), columns=['Degree'])
degrees_c3_growth = pd.merge(left = degrees_c3, right = avg_growth, left_index=True, right_index=True)
print(degrees_c3_growth.corr()) # positive degree - growth correlation

print(stock_clusters["Cluster 3"])
print(degrees_c3_growth['Average Growth'].describe())
print(avg_growth['Average Growth'].describe())

# Cluster 4
# This list has a strong focus on healthcare, consumer staples, and defensive sectors, with a few notable inclusions in
# aerospace/defense and telecom.
# This portfolio focuses on defensive sectors such as healthcare, consumer staples, and telecom, providing stability and
# resilience in volatile markets. It balances some exposure to cyclical industries like retail and aerospace, while also
# leveraging long-term trends in healthcare innovation and essential consumer products.

cluster_4_returns = daily_growth.loc[0:,['Date'] + list(stock_clusters["Cluster 4"])]

network_c4 = create_net(cluster_4_returns)
degrees_c4 = pd.DataFrame(network_c4.apply(lambda x: np.nansum(x)), columns=['Degree'])
degrees_c4_growth = pd.merge(left = degrees_c4, right = avg_growth, left_index=True, right_index=True)
print(degrees_c4_growth.corr()) # positive degree - growth correlation

print(stock_clusters["Cluster 4"])
print(degrees_c4_growth['Average Growth'].describe())
print(avg_growth['Average Growth'].describe())

# The clusters (i.e., which number is which sector) change at any run! Doublecheck before using!! #
# Clusers 0, 3 and 4 look like promising clusters to choose from, based on degree-growth correlations.
# Cluster 0 has the smallest growth opportunities, but low variance.
# Cluster 3 (Tech and others) has the greatest growth opportunities but high variance
# Cluster 4 (lots of consumer products) has decent growth and intermediate variance.

# Growth probabilities
growth_probability = pd.DataFrame(growth_probability, columns=['Growth Probability'])
print(growth_probability.describe())

growth_probability_c0 = pd.DataFrame(growth_probability.loc[list(stock_clusters["Cluster 0"])])
print(growth_probability_c0.describe()) # Second highest growth probability

growth_probability_c1 = pd.DataFrame(growth_probability.loc[list(stock_clusters["Cluster 1"])])
print(growth_probability_c1.describe()) # Lowest growth probability

growth_probability_c2 = pd.DataFrame(growth_probability.loc[list(stock_clusters["Cluster 2"])])
print(growth_probability_c2.describe()) # Fourth highest growth probability

growth_probability_c3 = pd.DataFrame(growth_probability.loc[list(stock_clusters["Cluster 3"])])
print(growth_probability_c3.describe()) # Highest growth probability

growth_probability_c4 = pd.DataFrame(growth_probability.loc[list(stock_clusters["Cluster 4"])])
print(growth_probability_c4.describe()) # Third highest growth probability

for i in range(4):
    df_name = f'degrees_c{i}_growth'
    print(f"Summary statistics for {df_name}:")
    print(eval(df_name)['Average Growth'].describe())

# Create an empty list to store the data
cluster_data = []

# Loop through the clusters
for i in range(5):
    df1_name = f'degrees_c{i}_growth'
    df2_name = f'growth_probability_c{i}'
    mean_growth = eval(df1_name)['Average Growth'].describe().iloc[1]
    growth_probability = eval(df2_name)['Growth Probability'].describe().iloc[1]
    cluster_data.append({'Cluster': f'degrees_c{i}', 'Mean Growth': mean_growth, 'Growth Probability': growth_probability})

# Convert the list to a DataFrame
mean_growth_df = pd.DataFrame(cluster_data)

# Display the resulting DataFrame
print(mean_growth_df.sort_values('Mean Growth', ascending=False))
print(mean_growth_df.sort_values('Growth Probability', ascending=False))
print(mean_growth_df.sort_values(by=['Mean Growth', 'Growth Probability'], ascending=[False, False]))



print(degrees_c0_growth.corr()) # positive degree - growth correlation
print(degrees_c1_growth.corr()) # positive degree - growth correlation
print(degrees_c2_growth.corr()) # positive degree - growth correlation
print(degrees_c3_growth.corr()) # positive degree - growth correlation
print(degrees_c4_growth.corr()) # positive degree - growth correlation




