import pandas as pd

"""## Read the data"""

df = pd.read_excel('hw_200.xlsx', index_col=0)

"""## Unit conversion"""

heights_imperial = df['Height(Inches)']
weights_imperial = df['Weight(Pounds)']

heights_metric = heights_imperial * 2.54
weights_metric = weights_imperial * 0.454

"""## Calculate BMI"""

bmis = weights_metric / (heights_metric/100)**2

"""## Create the result"""

result_dict = {
    'Height(cm)': round(heights_metric, 2),
    'Weight(kg)': round(weights_metric, 2),
    'BMI': round(bmis, 2)
    }

result_df = pd.DataFrame(result_dict)

"""## Sort by BMI"""

result_df.sort_values(by='BMI', inplace=True, ignore_index=True)
result_df.index = df.index

"""## Save the result"""

result_df.to_csv('bmi_result.csv')
result_df.to_excel('bmi_result.xlsx')
result_df.to_json('bmi_result.json', indent=2)
result_df.to_html('bmi_result.html')