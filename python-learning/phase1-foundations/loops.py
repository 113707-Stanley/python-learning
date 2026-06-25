topics = ["Python", "Git", "API Testing", "Playwright", "Postman", "JMeter", "SQL", "JavaScript"]
number = 1
print(f"\nHere are the topics I will be learning in the next 8 weeks:")
for topic in topics:
    if topic == "Postman":
        continue
    if topic == "SQL":
        break
    print(f"\nTopic number : {number}. {topic}")
    number += 1
total_topics = len(topics)
print(f"\n That's {total_topics} topics in total.")
print(f"\nI am excited to learn all of these topics and apply them in my work!")


