
confusion_matrix = [
    [50, 10],  # Row 1: TP, FN
    [5, 35]  # Row 2: FP, TN
]


tp=confusion_matrix[0][0]
fn=confusion_matrix[0][1]
fp=confusion_matrix[1][0]
tn=confusion_matrix[1][1]

Precision=tp/(tp+fp)
Recall=tp/(tp+fn)
f1_score=2*(Precision*Recall)/(Precision+Recall)
print(f'Precision: {Precision:.2f} ')
print(f'Recall: {Recall}')
print(f'F1 Score: {f1_score}')

