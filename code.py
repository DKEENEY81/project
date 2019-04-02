import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 100)


Cases = pd.read_csv('data/Cases2018.csv', encoding='iso-8859-1')

##Examine data, drop columns and labels
unneeded = ['caseId','docketId','lexisCite','term','naturalCourt','docket','chief','caseName','caseIssuesId','voteId','dateDecision', 'decisionType','usCite','sctCite','ledCite', 'issue','issueArea','decisionDirection','decisionDirectionDissent','authorityDecision1','authorityDecision2','lawType','lawSupp','lawMinor','majOpinWriter','majOpinAssigner']
labels = ['declarationUncon', 'caseDisposition', 'caseDispositionUnusual','partyWinning', 'precedentAlteration','voteUnclear','splitVote','majVotes','minVotes']

Cases.drop(unneeded, axis=1, inplace=True)
Cases.drop(labels, axis=1, inplace=True)

#Cases.head()

Cases[['dateArgument','dateRearg']]=Cases[['dateArgument', 'dateRearg']].notnull().astype(int)

# Cases.groupby('respondent').count()

Cases[['petitionerState','adminActionState','threeJudgeFdc','respondentState']] = Cases[['petitionerState','adminActionState','threeJudgeFdc','respondentState',]].fillna(value=0.0)
Cases['respondent'] = Cases[['respondent']].fillna(value=501)
Cases['adminAction'] = Cases[['adminAction']].fillna(value=118.0)
# There was already a code for unidentfiable which i reused for NaN here, 0s for other meaning not specified

# Cases.info()


# Cases[Cases['respondent'].isnull()]
 

#Casting as int32, not sure if this is beneficial or not

Cases.respondent = Cases.respondent.astype(int)
Cases.petitionerState = Cases.petitionerState.astype(int)
Cases.petitioner = Cases.petitioner.astype(int)
Cases.respondentState = Cases.respondentState.astype(int)
Cases.adminAction = Cases.adminAction.astype(int)
Cases.adminActionState = Cases.adminActionState.astype(int)
Cases.jurisdiction = Cases.jurisdiction.astype(int)


#Cases.info()


