'''Create a program that simulates a medical diagnosis system.
Consider symptoms input by the user and use nested if statements to suggest
 possible illnesses or conditions.


symptoms=input("Enter the symptoms that you have ")
symptom={
    'cough':['cold', 'flu', 'pneumonia', 'tuberculosis'],
    'fever':['cold', 'flu', 'dengue', 'malaria'],
    'headache':['cold', 'migraine', 'tension headache'],
    'heart_attack':['shortness_of_breath', 'cold_sweat', 'nausea'],
    'stroke':['difficulty_with_speech','loss_of_vision','confusion','severe_headache']

    }

if symptoms in symptom:
    print("You are suffering from:")
    for disease in symptom[symptoms]:
        print(disease)
        '''
symptoms = input("Enter the symptoms that you have ").split(',')
symptom = {
    'cough': ['cold', 'flu', 'pneumonia', 'tuberculosis'],
    'fever': ['cold', 'flu', 'dengue', 'malaria'],
    'headache': ['cold', 'migraine', 'tension headache'],
    'heart_attack': ['shortness_of_breath', 'cold_sweat', 'nausea'],
    'stroke': ['difficulty_with_speech', 'loss_of_vision', 'confusion', 'severe_headache']
}

lst = []
for symp in symptoms:
    for illness, symptoms_list in symptom.items():
        if symp in symptoms_list:
            lst.append(illness)
            break

if lst:
    for disease in lst:
        print("You may be suffering from:")
        print(disease)
else:
    print("No matching illness found based on the symptoms you entered.")


