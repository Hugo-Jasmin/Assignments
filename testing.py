def Grade_Converter(convert_to, **users):
    if convert_to == "letter_grade":
        GPAresults = []
        for user in users:
            def getLetter(user):
                if users["user"] < 40.00 and users["user"] >= 0:
                    user_Score = "F"
                elif users["user"] < 50 and users["user"] >= 40:
                    user_Score = "E"
                elif users["user"] >= 50 and users["user"] < 60:
                    user_Score = "D"
                elif users["user"] >=60 and users["user"] < 70:
                    user_Score = "C"
                elif users["user"] >= 70 and users["user"] < 85:
                    user_score = "B"
                elif users["user"] >= 85 and users["user"] < 100:
                    user_Score = "A"
                else:
                    user_Score = "Invalid Range"
                GPAresults.append(user, user_Score)
        return GPAresults
print(Grade_Converter(convert_to='letter_grade', Albert=90, Dwi=82, Syahdan=58, Veronica=84))
