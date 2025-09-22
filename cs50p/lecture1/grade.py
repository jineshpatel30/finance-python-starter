score = int(input("score: "))

if score >= 90:
#if 90 <= score <= 100:
#if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80:
#elif 80 <= score <90:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
