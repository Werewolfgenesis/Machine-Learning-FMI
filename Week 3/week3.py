import pandas as pd


file = pd.read_csv('Desktop/survey_results_public.csv')

#was the survey easy
ease_responces = file['SurveyEase'].value_counts(normalize=True).map(lambda x: f'{round(x*100, 2)}%')
print(ease_responces)
#76.98% found it ez

print(file.columns)


