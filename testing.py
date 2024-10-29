def Grade_Converter(convert_to, **users):
    if convert_to == "letter_grade":
        letterResults = []
        for user in users:
            def getLetter(score):
                if score < 40.00 and score >= 0:
                    return "F"
                elif score < 50 and score >= 40:
                    return "E"
                elif score >= 50 and score < 60:
                    return "D"
                elif score >=60 and score < 70:
                    return "C"
                elif score >= 70 and score < 85:
                    return "B"
                elif score >= 85 and score < 100:
                    return "A"
                else:
                    return "Invalid Range"
            studentScore = getLetter(users[user])
            letterResults.append((user, studentScore))
        return letterResults
    elif convert_to == "gpa":
        GPAResults = []
        for user in users:
            def gpaProcessing(score):
                if score < 40.00 and score >= 0:
                    return 1
                elif score < 50 and score >= 40:
                    return 1.5
                elif score >= 50 and score < 60:
                    return 2
                elif score >=60 and score < 70:
                    return 2.5
                elif score >= 70 and score < 85:
                    return 3
                elif score >= 85 and score < 100:
                    return 4
                else:
                    return "Invalid Range"
            studentScore = gpaProcessing(users[user])
            GPAResults.append((user, studentScore))
        return GPAResults
print(Grade_Converter(convert_to='gpa', Adam=62, Faiz=91))
print(Grade_Converter(convert_to='letter_grade', Albert=90, Dwi=82, Syahdan=58, Veronica=84))