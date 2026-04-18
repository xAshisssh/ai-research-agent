import os

def get_response(topic):
    # Simulated "AI agent reasoning"
    
    summary = f"{topic} is an important concept in modern technology."
    
    recommendations = [
        f"Learn basics of {topic}",
        f"Explore real-world use cases of {topic}",
        f"Build small projects using {topic}"
    ]
    
    explanation = f"I recommended these because they build foundational understanding and practical skills in {topic}."

    return summary, recommendations, explanation


def main():
    topic = input("Enter a topic: ")

    summary, recs, explanation = get_response(topic)

    print("\n--- SUMMARY ---")
    print(summary)

    print("\n--- RECOMMENDATIONS ---")
    for r in recs:
        print("-", r)

    print("\n--- WHY THESE? ---")
    print(explanation)


if __name__ == "__main__":
    main()
