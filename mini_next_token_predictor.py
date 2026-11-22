import random

sentences = [
    "I love artificial intelligence",
    "I love programming",
    "I enjoy learning Python",
    "I enjoy learning mathematics",
]


def train_model(sentences):
    model = {}
    for sentence in sentences:
        words = sentence.split()
        for i in range(len(words) - 2):
            current_words = (words[i], words[i + 1])
            next_word = words[i + 2]
            if current_words not in model:
                model[current_words] = []
            model[current_words].append(next_word)
    return model


def generated_sentence(model):
    user_input = input("Enter two starting words: ")
    starting_words = user_input.split()
    generated_sentence = starting_words.copy()
    for i in range(5):
        current_words = tuple(generated_sentence[-2:])
        if current_words in model:
            prediction = random.choice(model[current_words])
            generated_sentence.append(prediction)
        else:
            break
    return " ".join(generated_sentence)


def main():
    model = train_model(sentences)
    print("Generated sentence:", generated_sentence(model))


if __name__ == "__main__":
    main()
