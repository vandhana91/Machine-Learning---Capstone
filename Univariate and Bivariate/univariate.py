class Univariate():
    import pandas as pd
    import numpy as np
    def univariate(dataset,quan):
        import pandas as pd
        import numpy as np
        descriptive = pd.DataFrame(index = ['Mean','Median','Mode','Q1:25%','Q2:50%','Q3:75%','99%','Q4:100%',
                                       'IQR','1.5rule','Lesser','Greater','Min','Max','Skew','Kurtosis','Variance'],
                               columns = quan)
        
        for columnname in quan:
            descriptive[columnname]['Mean'] = dataset[columnname].mean()
            descriptive[columnname]['Median'] = dataset[columnname].median()
            descriptive[columnname]['Mode'] = dataset[columnname].mode()[0]
            descriptive[columnname]['Q1:25%'] = dataset.describe()[columnname]['25%']
            descriptive[columnname]['Q2:50%'] = dataset.describe()[columnname]['50%']
            descriptive[columnname]['Q3:75%'] = dataset.describe()[columnname]['75%']
            descriptive[columnname]['99%'] = np.percentile(dataset[columnname],99)
            descriptive[columnname]['Q4:100%'] = dataset.describe()[columnname]['max']
            descriptive[columnname]['IQR']= descriptive[columnname]['Q3:75%'] - descriptive[columnname]['Q1:25%']
            descriptive[columnname]['1.5rule'] = 1.5 * descriptive[columnname]['IQR']
            descriptive[columnname]['Lesser'] = descriptive[columnname]['Q1:25%'] - descriptive[columnname]['1.5rule']
            descriptive[columnname]['Greater'] = descriptive[columnname]['Q3:75%'] + descriptive[columnname]['1.5rule']
            descriptive[columnname]['Min'] = dataset[columnname].min()
            descriptive[columnname]['Max'] = dataset[columnname].max()
            descriptive[columnname]['Skew'] = dataset[columnname].skew()
            descriptive[columnname]['Kurtosis'] = dataset[columnname].kurtosis()
            descriptive[columnname]['Variance'] = dataset[columnname].var()
            descriptive[columnname]['STD'] = dataset[columnname].std()
            
        return descriptive