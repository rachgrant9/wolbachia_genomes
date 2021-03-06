import pandas as pd
import sys

df=pd.read_csv(sys.argv[1], sep='\t')
nan=df[df.representation == 'enriched']
nan.sort_values(by=["log2_mean(TAXON/others)"])
anno=pd.read_csv('../kinfin 1/cluster_domain_annotation.IPR.txt', sep='\t')
merged = pd.merge(anno, nan, on='#cluster_id')
merged.to_csv('superD_enriched.annotated.csv', index=False)
